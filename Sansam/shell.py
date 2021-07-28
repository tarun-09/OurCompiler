import Run

# while True:
#     text = input('Sans> ')
#     result, error = Run.run('<stdin>', text)
#
#     if error:
#         print(error.as_string())
#     else:
#         print(result)

import codecs

with codecs.open("D:\\program.txt", encoding='utf-8') as p:
    inp = p.read()
    print(inp)
    result, error = Run.run('program.txt', inp)

    if error:
        print(error.as_string())
    else:
        print(result)
