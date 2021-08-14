import Sansam.Lexer.Lexer
import Sansam.Values.Number
import Sansam.Parser.Parser
import Sansam.Interpreter.Interpreter
import Sansam.Context
import Sansam.Interpreter.SymbolTable as st
import Sansam.Values.Function

global_symbol_table = st.SymbolTable()
global_symbol_table.set("लुप्तः", Sansam.Values.Number.Number.null)
global_symbol_table.set("असत्यम्", Sansam.Values.Number.Number.false)
global_symbol_table.set("सत्यम्", Sansam.Values.Number.Number.true)
global_symbol_table.set("मुद्रणः", Sansam.Values.Function.BuiltInFunction.print)
global_symbol_table.set("PRINT_RET", Sansam.Values.Function.BuiltInFunction.print_ret)
global_symbol_table.set("INPUT", Sansam.Values.Function.BuiltInFunction.print_ret)
global_symbol_table.set("INPUT_INT", Sansam.Values.Function.BuiltInFunction.input_int)
global_symbol_table.set("CLEAR", Sansam.Values.Function.BuiltInFunction.clear)
global_symbol_table.set("CLS", Sansam.Values.Function.BuiltInFunction.clear)
global_symbol_table.set("IS_LIST", Sansam.Values.Function.BuiltInFunction.is_list)
global_symbol_table.set("IS_FUN", Sansam.Values.Function.BuiltInFunction.is_function)
global_symbol_table.set("APPEND", Sansam.Values.Function.BuiltInFunction.append)
global_symbol_table.set("POP", Sansam.Values.Function.BuiltInFunction.pop)



def run(fn, text):
    # Generate tokens
    lexer = Sansam.Lexer.Lexer.Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error

    # Generate AST
    parser = Sansam.Parser.Parser.Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error

    # Run program
    interpreter = Sansam.Interpreter.Interpreter.Interpreter()
    context = Sansam.Context.Context('<program>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value, result.error