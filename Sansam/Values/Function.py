import numbers
import os
import math

import Sansam.Values.Value as val
import Sansam.Interpreter.RunTimeResult as rtr
import Sansam.Interpreter.Interpreter as it
import Sansam.Context as ct
import Sansam.Interpreter.SymbolTable as st
import Sansam.Error.Errors as error


class BaseFunction(val.Value):
    def __init__(self, name):
        super().__init__()
        self.name = name or "<Anonymous>"

    def generate_new_context(self):
        new_context = ct.Context(self.name, self.context, self.pos_start)
        new_context.symbol_table = st.SymbolTable(new_context.parent.symbol_table)
        return new_context

    def check_args(self, arg_names, args):
        res = rtr.RunTimeResult()
        if len(args) > len(arg_names):
            return res.failure(error.RuntimeError(
                self.pos_start, self.pos_end,
                f"{len(args) - len(arg_names)} too many arguments passed into '{self}'",
                self.context
            ))

        if len(args) < len(self.arg_names):
            return res.failure(error.RuntimeError(
                self.pos_start, self.pos_end,
                f"{len(args) - len(arg_names)} too many arguments passed into '{self}'",
                self.context
            ))

        return res.success(None)

    def populate_args(self, arg_names, args, exec_ctx):
        for i in range(len(args)):
            arg_name = self.arg_names[i]
            arg_value = args[i]
            arg_value.set_context(exec_ctx)
            exec_ctx.symbol_table.set(arg_name, arg_value)

    def check_and_populate_args(self, arg_names, args, exec_ctx):
        res = rtr.RunTimeResult()
        res.register(sef.check_args(arg_names, args))
        if res.error: return res
        self.populate_args(arg_names, args, exec_ctx)
        return res.success(None)


class Function(BaseFunction):
    def __init__(self, name, body_node, arg_names):
        super().__init__(name)
        self.body_node = body_node
        self.arg_names = arg_names

    def execute(self, args):
        res = rtr.RunTimeResult()
        interpreter = it.Interpreter()
        exec_ctx = self.generate_new_context()

        res.register(self.check_and_populate_args(self.arg_names, args, new_context))
        if res.error: return res

        value = res.register(interpreter.visit(self.body_node,new_context))
        if res.error:
            return res

        return res.success(value)

    def copy(self):
        copy = Function(self.name, self.body_node, self.arg_names)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        return f"<function {self.name}>"

class BuiltInFunction(BaseFunction):
    def __init__(self, name):
        super().__init__(name)

    class BuiltInFunction(BaseFunction):
        def __init__(self, name):
            super().__init__(name)

        def execute(self, args):
            res = rtr.RunTimeResult()
            exec_ctx = self.generate_new_context()

            method_name = f'execute_{self.name}'
            method = getattr(self, method_name, self.no_visit_method)

            res.register(self.check_and_populate_args(method.arg_names, args, exec_ctx))
            if res.error: return res

            return_value = res.register(method(exec_ctx))
            if res.error: return res
            return res.success(return_value)

    def no_visit_method(self, node, context):
        raise Exception(f'No execute_{self.name} method defined')


    def copy(self):
        copy = BuiltInFunction(self.name)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<built-in function {self.name}>"

    ##################################################

    def execute_print_ret(self, exec_ctx):
        return rtr.RunTimeResult().success(str(exec_ctx.symbol_table.get('value')))
    execute_print_ret.arg_names = ['value']

    def execute_print(self, exec_ctx):
        print(exec_ctx.symbol_table.get('value'))
        return rtr.RunTimeResult().success(Number.null)

    execute_print_ret.arg_names = ['value']

    def execute_input(self, exec_ctx):
        text = input()
        return rtr.RunTimeResult().success(String(text))
    execute_input.arg_names = []

    def execute_input_int(self, exec_ctx):
        while True:
            text = input()
            try:
                number = int(text)
                break
            except ValueError:
                print(f"'{text}' must be an integer. Try again!")
        return rtr.RunTimeResult().success(String(text))
    execute_input_int.arg_names = []

    def execute_clear(self, exec_ctx):
        os.system('cls' if os.name == 'nt' else 'clear')
        return rtr.RunTimeResult().success(Number.null)
    execute_clear.arg_names = []

    def execute_is_number(self, exec_ctx):
        is_number = isinstance(exec_ctx.symbol_table.get('value'), Number)
        return rtr.RunTimeResult().success(Number.true if is_number else Number.false)
    execute_is_number.arg_names = ['value']

    def execute_is_String(self, exec_ctx):
        is_number = isinstance(exec_ctx.symbol_table.get('value'), String)
        return rtr.RunTimeResult().success(Number.true if is_number else Number.false)

    execute_is_String.arg_names = ['value']

    def execute_is_list(self, exec_ctx):
        is_number = isinstance(exec_ctx.symbol_table.get('value'), List)
        return rtr.RunTimeResult().success(Number.true if is_number else Number.false)
    execute_is_list.arg_names = ['value']

    def execute_is_function(self, exec_ctx):
        is_number = isinstance(exec_ctx.symbol_table.get('value'), BaseFunction)
        return rtr.RunTimeResult().success(Number.true if is_number else Number.false)
    execute_is_function.arg_names = ['value']

    def execute_append(self, exec_ctx):
        list = exec_ctx.symbol_table.get("list")
        value = exec_ctx.symbol_table.get("value")

        if not isinstance(list_, List):
            return rtr.RunTimeResult().failure(error.RunTimeError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                exec_ctx
            ))

        list_.elements.append(value)
        return rtr.RunTimeResult().success(Number.null)
    execute_append.arg_names = ['list', 'value']

    def execute_pop(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        index = exec_ctx.symbol_table.get("index")

        if not isinstance(list_, List):
            return rtr.RunTimeResult().failure(error.RunTimeError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                exec_ctx
            ))

        if not isinstance(index, Number):
                return rtr.RunTimeResult().failure(error.RunTimeError(
                    self.pos_start, self.pos_end,
                    "Second argument must be list",
                    exec_ctx
                ))

        try:
            element = list_.elements.pop(index.value)
        except:
            return rtr.RunTimeResult().failure(error.RunTimeError(
                self.pos_start, self.pos_end,
                'Elements at this index could not be removed from list because index is out of range',
                exec_ctx
            ))
        return rtr.RunTimeResult().success(element)
    execute_pop.arg_names = ['list', 'index']

    def execute_extend(self, exec_ctx):
        listA = exec_ctx.symbol_table.get("listA")
        listB = exec_ctx.symbol_table.get("listB")

        if not isinstance(listA, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                exec_ctx
            ))

        if not isinstance(listB, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Second argument must be list",
                exec_ctx
            ))

        listA.elements.extend(listB.elements)
        return RTResult().success(Number.null)

    execute_extend.arg_names = ["listA", "listB"]


BuiltInFunction.print                 = BuiltInFunction("print")
BuiltInFunction.print_ret             = BuiltInFunction("print_ret")
BuiltInFunction.input                 = BuiltInFunction("input")
BuiltInFunction.input_int             = BuiltInFunction("input_int")
BuiltInFunction.clear                 = BuiltInFunction("clear")
BuiltInFunction.is__number            = BuiltInFunction("is_number")
BuiltInFunction.is_string             = BuiltInFunction("is_string")
BuiltInFunction.is_list               = BuiltInFunction("is_list")
BuiltInFunction.is_function           = BuiltInFunction("is_function")
BuiltInFunction.append                = BuiltInFunction("append")
BuiltInFunction.pop                   = BuiltInFunction("pop")
BuiltInFunction.extend                = BuiltInFunction("extend")


