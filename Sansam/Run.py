import Sansam.Lexer.Lexer
import Sansam.Values.Number
import Sansam.Parser.Parser
import Sansam.Interpreter.Interpreter
import Sansam.Context
import Sansam.Interpreter.SymbolTable as st
import Sansam.Values.Function as func

global_symbol_table = st.SymbolTable()
global_symbol_table.set("लुप्तः", Sansam.Values.Number.null)
global_symbol_table.set("असत्यम्", Sansam.Values.Number.false)
global_symbol_table.set("सत्यम्", Sansam.Values.Number.true)
global_symbol_table.set("मुद्रणः", func.print_)
global_symbol_table.set("मुद्रणः_यच्छ", func.print_ret)
global_symbol_table.set("आगम्", func.input_)
global_symbol_table.set("आगम्_पूर्णाङ्कः", func.input_int)
global_symbol_table.set("किम्_पूर्णाङ्क", func.is_number_)
global_symbol_table.set("किम्_सूत्र", func.is_string_)
global_symbol_table.set("किम्_आवलि", func.is_list_)
global_symbol_table.set("किम्_कार्य", func.is_function_)
global_symbol_table.set("संकलः", func.append_)
global_symbol_table.set("पोप", func.pop_)
global_symbol_table.set("अतिसृ", func.extend_)

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

