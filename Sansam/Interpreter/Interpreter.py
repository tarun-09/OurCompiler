import Sansam.Interpreter.RunTimeResult as rtr
import Sansam.Error.Errors as errors
import Sansam.Values.Number as num
import Sansam.Lexer.Token as token
import Sansam.Values.Boolean as boolean
import Sansam.Values.String as string
import Sansam.Values.List as list
import Sansam.Values.Function as func
import Sansam.Values.Dictionary as dict


class Interpreter:
    def visit(self, node, context):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)

    def no_visit_method(self, node, context):
        raise Exception(f"No visit_{type(node).__name__} method defined")

    ###################################

    def visit_NumberNode(self, node, context):
        return rtr.RunTimeResult().success(
            num.Number(node.tok.value).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_StringNode(self, node, context):
        return rtr.RunTimeResult().success(
            string.String(node.tok.value).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_ListNode(self, node, context):
        res = rtr.RunTimeResult()
        elements = []

        for element_node in node.element_nodes:
            elements.append(res.register(self.visit(element_node, context)))
            if res.should_return():
                return res

        return res.success(
            list.List(elements).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_DictionaryNode(self, node, context):
        res = rtr.RunTimeResult()
        elements = {}

        for key_node in node.element_nodes:
            key = res.register(self.visit(key_node, context))
            if res.should_return(): return res
            value = res.register(self.visit(node.element_nodes[key_node], context))
            if res.should_return(): return res

            elements[key] = value

        return res.success(
            dict.Dictionary(elements).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_ForNode(self, node, context):
        res = rtr.RunTimeResult()
        elements = []

        if node.start_value_node:
            start_value = res.register(self.visit(node.start_value_node, context))
            if res.should_return():
                return res
        else:
            start_value = num.Number(0)

        end_value = res.register(self.visit(node.end_value_node, context))
        if res.should_return():
            return res
        if node.step_value_node:
            step_value = res.register((self.visit(node.step_value_node, context)))
            if res.should_return():
                return res
        else:
            if start_value.value < end_value.value:

                step_value = num.Number(1)
            else:
                step_value = num.Number(-1)
        i = start_value.value
        if step_value.value >= 0:
            condition = lambda: i < end_value.value
        else:
            condition = lambda: i > end_value.value
        while condition():
            context.symbol_table.set(node.var_name_tok.value, num.Number(i))
            i += step_value.value

            value = res.register(self.visit(node.body_node, context))
            if res.should_return() and res.loop_should_continue is False and res.loop_should_break is False:
                return res

            if res.loop_should_continue:
                continue

            if res.loop_should_break:
                break

            elements.append(value)

        return res.success(
            list.List(elements).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_BooleanNode(self, node, context):
        return rtr.RunTimeResult().success(
            boolean.Boolean(node.tok.value).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_VarAccessNode(self, node, context):
        res = rtr.RunTimeResult()
        var_name = node.var_name_tok.value
        value = context.symbol_table.get(var_name)

        if not value:
            return res.failure(errors.RunTimeError(
                node.pos_start, node.pos_end,
                f"'{var_name}' is not defined",
                context
            ))

        value = value.copy().set_pos(node.pos_start, node.pos_end).set_context(context)
        return res.success(value)

    def visit_DataAccessNode(self, node, context):
        res = rtr.RunTimeResult()
        var_name = node.var_name_tok.value
        value = context.symbol_table.get(var_name)

        if not value:
            return res.failure(errors.RunTimeError(
                node.pos_start, node.pos_end,
                f"'{var_name}' is not defined",
                context
            ))

        if isinstance(value, list.List) or isinstance(value,string.String) or isinstance(value,dict.Dictionary):
            index = res.register(self.visit(node.index_tok, context))
            if res.should_return():
                return res

            result, error = value.division(index)

            if error:
                return res.failure(error)
            else:
                return res.success(result)

        return res.failure(errors.RunTimeError(
            node.pos_start, node.pos_end,
            "Dictionary, list and string should be present"
        ))

    def visit_VarAssignNode(self, node, context):
        res = rtr.RunTimeResult()
        var_name = node.var_name_tok.value
        value = res.register(self.visit(node.value_node, context))
        if res.should_return():
            return res

        context.symbol_table.set(var_name, value)
        return res.success(value)

    def visit_BinOpNode(self, node, context):
        res = rtr.RunTimeResult()
        left = res.register(self.visit(node.left_node, context))
        if res.should_return():
            return res
        right = res.register(self.visit(node.right_node, context))
        if res.should_return():
            return res

        if node.op_tok.type == token.T_PLUS:
            result, error = left.addition(right)
        elif node.op_tok.type == token.T_MINUS:
            result, error = left.subtraction(right)
        elif node.op_tok.type == token.T_MUL:
            result, error = left.multiplication(right)
        elif node.op_tok.type == token.T_DIV:
            result, error = left.division(right)
        elif node.op_tok.type == token.T_MOD:
            result, error = left.modulus(right)
        elif node.op_tok.type == token.T_POW:
            result, error = left.exponential(right)
        elif node.op_tok.type == token.T_ISEQ:
            result, error = left.get_comparison_eq(right)
        elif node.op_tok.type == token.T_ISNEQ:
            result, error = left.get_comparison_ne(right)
        elif node.op_tok.type == token.T_ISL:
            result, error = left.get_comparison_lt(right)
        elif node.op_tok.type == token.T_ISG:
            result, error = left.get_comparison_gt(right)
        elif node.op_tok.type == token.T_BIT_AND:
            result, error = left.get_comparison_bitand(right)
        elif node.op_tok.type == token.T_BIT_OR:
            result, error = left.get_comparison_bitor(right)
        elif node.op_tok.type == token.T_ISLEQ:
            result, error = left.get_comparison_lte(right)
        elif node.op_tok.type == token.T_ISGEQ:
            result, error = left.get_comparison_gte(right)
        elif node.op_tok.type == token.T_RSHIFT:
            result, error = left.get_shift_right(right)
        elif node.op_tok.type == token.T_LSHIFT:
            result, error = left.get_shift_left(right)
        elif node.op_tok.type == token.T_XOR:
            result, error = left.get_xor(right)
        elif node.op_tok.matches(token.T_KEYWORD, 'च'):
            result, error = left.anded_by(right)
        elif node.op_tok.matches(token.T_KEYWORD, 'वा'):
            result, error = left.ored_by(right)

        if error:
            return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_start, node.pos_end))

    def visit_UnaryOpNode(self, Node, context):

        res = rtr.RunTimeResult()
        number = res.register(self.visit(Node.node, context))
        if res.should_return():
            return res

        error = None

        if Node.op_tok.type == token.T_MINUS:
            number, error = num.Number(0).subtraction(number)
        elif Node.op_tok.matches(token.T_KEYWORD, 'न') or Node.op_tok.type == token.T_NOT:
            number, error = number.notted()

        elif Node.op_tok.type == token.T_BIT_NOT:

            number, error = number.bitnotted()
        if error:
            return res.failure(error)
        else:
            return res.success(number.set_pos(Node.pos_start, Node.pos_end))

    def visit_FactorialNode(self, Node, context):
        res = rtr.RunTimeResult()
        factorial = res.register(self.visit(Node.node, context))
        if res.should_return():
            return res

        error = None

        if Node.op_tok.type == token.T_FACT:
            factorial, error = factorial.factorial()
        if error:
            return res.failure(error)
        else:
            return res.success(factorial.set_pos(Node.pos_start, Node.pos_end))

    def visit_WhileNode(self, node, context):
        res = rtr.RunTimeResult()
        elements = []

        while True:
            condition = res.register(self.visit(node.condition_node, context))
            if res.should_return():
                return res

            if not condition.is_true(): break

            value = res.register(self.visit(node.body_node, context))
            if res.should_return() and res.loop_should_break is False and res.loop_should_continue is False:
                return res

            if res.loop_should_continue:
                continue


            if res.loop_should_break:
                break

            elements.append(value)

        return res.success(
            list.List(elements).set_context(context).set_pos(node.pos_start, node.pos_end)
        )


    def visit_FuncDefNode(self, node, context):
        res = rtr.RunTimeResult()

        func_name = node.var_name_tok.value if node.var_name_tok else None
        body_node = node.body_node
        arg_names = [arg_name.value for arg_name in node.arg_name_tokens]

        func_value = func.Function(func_name, body_node, arg_names, node.should_auto_return).set_context(
            context).set_pos(
            node.pos_start, node.pos_end)

        if node.var_name_tok:
            context.symbol_table.set(func_name, func_value)

        return res.success(func_value)

    def visit_CallNode(self, node, context):
        res = rtr.RunTimeResult()
        args = []

        value_to_call = res.register(self.visit(node.node_to_call, context))
        if res.should_return():
            return res

        value_to_call = value_to_call.copy().set_pos(node.pos_start, node.pos_end)

        for arg_node in node.arg_nodes:
            args.append(res.register(self.visit(arg_node, context)))

            if res.should_return():
                return res

        return_value = res.register(value_to_call.execute(args))
        if res.should_return():
            return res

        return_value = return_value.copy().set_pos(node.pos_start, node.pos_end).set_context(context)
        return res.success(return_value)

    def visit_IfNode(self, node, context):
        res = rtr.RunTimeResult()

        for condition, expr in node.cases:
            condition_value = res.register(self.visit(condition, context))
            if res.should_return(): return res

            if condition_value.is_true():
                expr_value = res.register(self.visit(expr, context))
                if res.should_return(): return res
                return res.success(expr_value)

        if node.else_case:
            else_value = res.register(self.visit(node.else_case, context))
            if res.should_return(): return res
            return res.success(else_value)

        return res.success(None)

    def visit_ReturnNode(self, node, context):
        res = rtr.RunTimeResult()

        if node.node_to_return:
            value = res.register(self.visit(node.node_to_return, context))
            if res.should_return(): return res
        else:
            value = num.null

        return res.success_return(value)

    def visit_ContinueNode(self, node, context):
        return rtr.RunTimeResult().success_continue()

    def visit_BreakNode(self, node, context):
        return rtr.RunTimeResult().success_break()
