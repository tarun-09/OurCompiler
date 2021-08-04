import Run
import codecs

with codecs.open("C:\\Users\\vaibhav goel\\Desktop\\firstprogram.txt", encoding='utf-8') as p:
    inp = p.read()
    print(inp)
    result, error = Run.run('firstprogram.txt', inp)

    if error:
        print(error.as_string())
    else:
        print(result)
