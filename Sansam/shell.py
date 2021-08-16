import Run
import codecs

with codecs.open("D:\\program.txt", encoding='utf-8') as p:
    inp = p.read()
    result, error = Run.run('program.txt', inp)

    if error:
        print(error.as_string())
    else:
        print(repr(result))
