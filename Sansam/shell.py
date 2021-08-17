<<<<<<< HEAD
'''import Sans

while True:
    text = input('Sans> ')
    result, error = Sans.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)

# committed'''
#Ookokoko
import Run
import codecs

with codecs.open("D:\\pro.txt", encoding='utf-8') as p:
    inp = p.read()
    print(inp)
    result, error = Run.run('program.txt', inp)
=======
import Run
import codecs

with codecs.open("trail.txt", encoding='utf-8') as p:

    inp = p.read()
    result, error = Run.run('firstprogram.txt', inp)
>>>>>>> d7df03c53a59ab101a6e8bf77896e2363289c804

    if error:
        print(error.as_string())
    else:
        print(result)

