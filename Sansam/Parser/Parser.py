import Sansam.Parser.ParseResult as pr
import Sansam.Parser.Nodes as nodes
import Sansam.Error.Errors as error
import Sansam.Lexer.Token as token


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_index = -1
        self.advance()

    def advance(self, ):
        self.tok_index += 1
        self.update_current_tok()
        return self.current_tok

    def reverse(self, amount=1):
        self.tok_index -= amount
        self.update_current_tok()
        return self.current_tok

    def update_current_tok(self):
        if self.tok_index > -1 and self.tok_index < len(self.tokens):
            self.current_tok = self.tokens[self.tok_index]

    def parse(self):
        res = self.statements()
        if not res.error and self.current_tok.type != token.T_EOF:
            return res.failure(error.InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "अपेक्षित '+', '-', '*' वा '/'"
            ))
        return res

    ###################################

    def atom(self):
        res = pr.ParseResult()
        tok = self.current_tok

        if tok.type in (token.T_INT, token.T_FLOAT):
            res.register_advancement()
            self.advance()
            return res.success(nodes.NumberNode(tok))

        elif tok.type == token.T_IDENTIFIER:
            res.register_advancement()
            self.advance()
            return res.success(nodes.VarAccessNode(tok))

        elif tok.matches(token.T_KEYWORD, 'असत्यम्') or tok.matches(token.T_KEYWORD, 'सत्यम्'):
            res.register_advancement()
            self.advance()
            return res.success(nodes.BooleanNode(tok))

        elif tok.type == token.T_LPAREN:
            res.register_advancement()
            self.advance()
            expr = res.register(self.expr())
            if res.error:
                return res
            if self.current_tok.type == token.T_RPAREN:
                res.register_advancement()
                self.advance()
                return res.success(expr)
            else:
                return res.failure(error.InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "अपेक्षित ')'"
                ))

        elif tok.type == token.T_LSQUARE:
            list_expr = res.register(self.list_expr())
            if res.error: return res
            return res.success(list_expr)


        return res.failure(error.InvalidSyntaxError(
            tok.pos_start, tok.pos_end,
            "अपेक्षित अंकम्, चरः, '+', '-','!*', '[', वा  '('"
        ))

    def list_expr(self):
        res = pr.ParseResult()
        element_nodes = []
        pos_start = self.current_tok.pos_start.copy()

        if self.current_tok.type != token.T_LSQUARE:
            return res.failure(error.InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"अपेक्षित '['"
            ))

        res.register_advancement()
        self.advance()

        if self.current_tok.type == token.T_RSQUARE:
            res.register_advancement()
            self.advance()
        else:
            element_nodes.append(res.register(self.expr()))
            if res.error:
                return res.failure(error.InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "अपेक्षित ']',अंकम्, चरः, '+', '-','[', वा  '('"
                ))

            while self.current_tok.type == token.T_COMMA:
                res.register_advancement()
                self.advance()

                element_nodes.append(res.register(self.expr()))
                if res.error: return res

            if self.current_tok.type != token.T_RSQUARE:
                return res.failure(error.InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"अपेक्षित ',' वा ']'"
                ))

            res.register_advancement()
            self.advance()

        return res.success(nodes.ListNode(
            element_nodes,
            pos_start,
            self.current_tok.pos_end.copy()
        ))

    def factorial(self):
        res = pr.ParseResult()
        tok = self.current_tok

        if tok.type in (token.T_INT, token.T_IDENTIFIER):
            node = res.register(self.atom())
            if res.error:
                return res
            if self.current_tok.type == token.T_FACT:
                tok = self.current_tok
                res.register_advancement()
                self.advance()
                return res.success(nodes.FactorialNode(node, tok))
            return res.success(node)


        return self.atom()

    def power(self):
        return self.bin_op(self.factorial, (token.T_POW,), self.factor)


    def factor(self):
        res = pr.ParseResult()
        tok = self.current_tok

        if tok.type in (token.T_PLUS, token.T_MINUS):
            res.register_advancement()
            self.advance()
            factor = res.register(self.factor())
            if res.error:
                return res
            return res.success(nodes.UnaryOpNode(tok, factor))

        return self.power()

    def term(self):
        return self.bin_op(self.factor, (token.T_MUL, token.T_DIV))

    def arith_expr(self):
        return self.bin_op(self.term, (token.T_PLUS, token.T_MINUS))

    def comp_expr(self):
        res = pr.ParseResult()

        if self.current_tok.matches(token.T_KEYWORD, 'न') or self.current_tok.type == token.T_NOT:
            op_tok = self.current_tok
            res.register_advancement()
            self.advance()

            node = res.register(self.comp_expr())
            if res.error:
                return res

            return res.success(nodes.UnaryOpNode(op_tok, node))

        node = res.register(self.bin_op(self.arith_expr, (token.T_ISG, token.T_ISEQ, token.T_ISNEQ, token.T_ISL,
                                                          token.T_ISLEQ, token.T_ISGEQ)))

        if res.error:
            return res.failure(error.InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "अपेक्षित अंकम्, चरः, '+', '-','!','न','[' वा  '('"
            ))

        return res.success(node)

    def expr(self):
        res = pr.ParseResult()

        if self.current_tok.type == token.T_IDENTIFIER:
            var_name = self.current_tok
            res.register_advancement()
            self.advance()

            if self.current_tok.type == token.T_EQU:
                res.register_advancement()
                self.advance()

                expr = res.register(self.expr())
                if res.error:
                    return res

                return res.success(nodes.VarAssignNode(var_name, expr))

            else:
                self.reverse()

        node = res.register(self.bin_op(self.comp_expr, ((token.T_KEYWORD, 'च'), (token.T_KEYWORD, 'वा'))))

        if res.error:
            res.failure(error.InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "अपेक्षित अंकम्, चरः, identifier, '+', '-', '[' वा '('"
            ))

        return res.success(node)

    def statements(self):
        res = pr.ParseResult()
        statements = []
        pos_start = self.current_tok.pos_start.copy()

        while self.current_tok.type == token.T_NL:
            res.register_advancement()
            self.advance()

        statement = res.register(self.expr())
        if res.error:
            return res
        statements.append(statement)

        more_statements = True

        while True:
            newline_count = 0
            while self.current_tok.type == token.T_NL:
                res.register_advancement()
                self.advance()
                newline_count += 1

            if newline_count == 0:
                more_statements = False

            if not more_statements:
                break

            statement = res.try_register(self.expr())
            if not statement:
                self.reverse(res.to_reverse_count)
                more_statements = False
                continue

            statements.append(statement)

        return res.success(nodes.ListNode(
            statements, pos_start, self.current_tok.pos_end.copy()
        ))

    ###############################################################

    def bin_op(self, func_1, ops, func_2=None):
        if func_2 is None:
            func_2 = func_1

        res = pr.ParseResult()
        left = res.register(func_1())
        if res.error:
            return res

        while self.current_tok.type in ops or (self.current_tok.type, self.current_tok.value) in ops:
            op_tok = self.current_tok
            res.register_advancement()
            self.advance()
            right = res.register(func_2())
            if res.error:
                return res
            left = nodes.BinOpNode(left, op_tok, right)

        return res.success(left)
