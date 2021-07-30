#######################################
# IMPORTS
#######################################
from Sansam.Error.Error_String_With_Arrows import Error_String_With_Arrows

#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789'


#######################################
# ERRORS
#######################################

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}--> {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.line + 1}'
        result += '\n\n' + Error_String_With_Arrows(self.pos_start.ftext, self.pos_start, self.pos_end)
        return result


class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'अवैध अक्षर', details)


class InvalidSyntaxError(Error):
    def __init__(self, pos_start, pos_end, details=''):
        super().__init__(pos_start, pos_end, 'क्रमभङ्ग', details)


class RunTimeError(Error):
    def __init__(self, pos_start, pos_end, details, context):
        super().__init__(pos_start, pos_end, 'चलनकालिकदोष', details)
        self.context = context

    def as_string(self):
        result = self.generate_traceback()
        result += f'{self.error_name}: {self.details}'
        result += '\n\n' + Error_String_With_Arrows(self.pos_start.ftext, self.pos_start, self.pos_end)
        return result

    def generate_traceback(self):
        result = ''
        pos = self.pos_start
        ctx = self.context

        while ctx:
            result = f' सञ्चिका {pos.fn}, पङ्क्ति {str(pos.line + 1)}, in {ctx.display_name}\n' + result
            pos = ctx.parent_entry_pos
            ctx = ctx.parent

        return 'Traceback (अधिकतम अपूर्व आहू गत):\n' + result
        # (most recent call last)


#######################################
# POSITION
#######################################

class Position:
    def __init__(self, index, line, col, fn, ftext):
        self.index = index
        self.line = line
        self.col = col
        self.fn = fn
        self.ftext = ftext

    def advance(self, current_char=None):
        self.index += 1
        self.col += 1

        if current_char == '\n':
            self.line += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.index, self.line, self.col, self.fn, self.ftext)


#######################################
# TOKENS
#######################################

T_INT = 'अंकम्'
T_FLOAT = 'चरः'
T_PLUS = 'योजनम्'
T_MINUS = 'ऊन'
T_MUL = 'गुणता'
T_DIV = 'भेद'
T_POW = '^'
T_LPAREN = '('
T_RPAREN = ')'
T_EOF = 'समन्त'
T_KEYWORD = 'KEYWORD'

class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end

    def __repr__(self):
        if self.value:
            return f'{self.type}->{self.value}'
        return f'{self.type}'


#######################################
# LEXER
#######################################

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(T_PLUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(T_MINUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(T_MUL, pos_start=self.pos))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(T_DIV, pos_start=self.pos))
                self.advance()
            elif self.current_char == '^':
                tokens.append(Token(T_POW, pos_start=self.pos))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(T_LPAREN, pos_start=self.pos))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(T_RPAREN, pos_start=self.pos))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        tokens.append(Token(T_EOF, pos_start=self.pos))
        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0
        pos_start = self.pos.copy()

        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(T_INT, int(num_str), pos_start, self.pos)
        else:
            return Token(T_FLOAT, float(num_str), pos_start, self.pos)


#######################################
# NODES
#######################################

class NumberNode:
    def __init__(self, tok):
        self.tok = tok

        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end

    def __repr__(self):
        return f'{self.tok}'


class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

        self.pos_start = self.left_node.pos_start
        self.pos_end = self.right_node.pos_end

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'


class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node

        self.pos_start = self.op_tok.pos_start
        self.pos_end = self.node.pos_end

    def __repr__(self):
        return f'({self.op_tok}, {self.node})'

class IfNode:
    def __init__(self, cases, else_case):
        self.cases = cases
        self.else_case = else_case

        self.pos_start = self.cases[0][0].pos_start
        self.pos_end = (self.else_case or self.cases[len(self.cases)-1][0]).pos_end




#######################################
# PARSE RESULT
#######################################

class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None

    def register(self, res):
        if isinstance(res, ParseResult):
            if res.error:
                self.error = res.error
            return res.node

        return res

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        self.error = error
        return self


#######################################
# PARSER
#######################################

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_index = -1
        self.advance()

    def advance(self, ):
        self.tok_index += 1
        if self.tok_index < len(self.tokens):
            self.current_tok = self.tokens[self.tok_index]
        return self.current_tok

    def parse(self):
        res = self.expr()
        if not res.error and self.current_tok.type != T_EOF:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "अपेक्षित '+', '-', '*' वा '/'"
            ))
        return res

    ###################################

    def atom(self):
        res = ParseResult()
        tok = self.current_tok

        if tok.type in (T_INT, T_FLOAT):
            res.register(self.advance())
            return res.success(NumberNode(tok))

        elif tok.type == T_LPAREN:
            res.register(self.advance())
            expr = res.register(self.expr())
            if res.error:
                return res
            if self.current_tok.type == T_RPAREN:
                res.register(self.advance())
                return res.success(expr)
            else:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "अपेक्षित ')'"
                ))
        return res.failure(InvalidSyntaxError(
            tok.pos_start, tok.pos_end,
            "अपेक्षित अंकम्, चरः, '+', '-', वा  '(' "
        ))

    def power(self):
        return self.bin_op(self.atom, (T_POW,), self.factor)

    def factor(self):
        res = ParseResult()
        tok = self.current_tok

        if tok.type in (T_PLUS, T_MINUS):
            res.register(self.advance())
            factor = res.register(self.factor())
            if res.error:
                return res
            return res.success(UnaryOpNode(tok, factor))

        return self.power()

    def term(self):
        return self.bin_op(self.factor, (T_MUL, T_DIV))

    def expr(self):
        return self.bin_op(self.term, (T_PLUS, T_MINUS))

    ###################################

    def bin_op(self, func_1, ops, func_2=None):
        if func_2 is None:
            func_2 = func_1
        res = ParseResult()
        left = res.register(func_1())
        if res.error:
            return res

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            res.register(self.advance())
            right = res.register(func_2())
            if res.error:
                return res
            left = BinOpNode(left, op_tok, right)

        return res.success(left)


#######################################
# RUNTIME RESULT
#######################################

class RunTimeResult:
    def __init__(self):
        self.value = None
        self.error = None

    def register(self, res):
        if res.error:
            self.error = res.error
        return res.value

    def success(self, value):
        self.value = value
        return self

    def failure(self, error):
        self.error = error
        return self


#######################################
# Values
#######################################

class Number:
    def __init__(self, value, pos_start=None, pos_end=None, context=None):
        self.value = value
        # self.set_pos()
        # self.set_context()
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.context = context

    # def set_pos(self, pos_start=None, pos_end=None):
    #     self.pos_start = pos_start
    #     self.pos_end = pos_end
    #     return self
    #
    # def set_context(self, context=None):
    #     self.context = context
    #     return self

    def addition(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value, context=self.context), None

    def subtraction(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value, context=self.context), None

    def multiplication(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value, context=self.context), None

    def division(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RunTimeError(other.pos_start, other.pos_end, "विभाजन सह शून्य दोष", self.context)

            return Number(self.value / other.value, context=self.context), None

    def exponential(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value, context=self.context), None

    def __repr__(self):
        return str(self.value)


#######################################
# CONTEXT
#######################################

class Context:
    def __init__(self, display_name, parent=None, parent_entry_pos=None):
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_pos = parent_entry_pos


#######################################
# INTERPRETER
#######################################
class Interpreter:
    def visit(self, node, context):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node, context)

    #################################

    def visit_NumberNode(self, node, context):
        return RunTimeResult().success(Number(node.tok.value, node.pos_start, node.pos_end, context))

    def visit_BinOpNode(self, node, context):
        res = RunTimeResult()
        left = res.register(self.visit(node.left_node, context))
        if res.error:
            return res

        right = res.register(self.visit(node.right_node, context))
        if res.error:
            return res

        if node.op_tok.type == T_PLUS:
            result, error = left.addition(right)

        if node.op_tok.type == T_MINUS:
            result, error = left.subtraction(right)

        if node.op_tok.type == T_MUL:
            result, error = left.multiplication(right)

        if node.op_tok.type == T_DIV:
            result, error = left.division(right)

        if node.op_tok.type == T_POW:
            result, error = left.exponential(right)

        if error:
            return res.failure(error)
        else:
            return res.success(result)

    def visit_UnaryOpNode(self, node, context):
        res = RunTimeResult()
        number = res.register(self.visit(node.node, context))
        if res.error:
            return res

        error = None

        if node.op_tok.type == T_MINUS:
            number, error = Number(0).subtraction(number)
        if error:
            return res.failure(error)
        else:
            return res.success(number)


#######################################
# RUN
#######################################

def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error

    # Run Program
    interpreter = Interpreter()
    context = Context('<program>')
    result = interpreter.visit(ast.node, context)

    return result.value, result.error
