import Sans

while True:
    text = input('Sans> ')
    result, error = Sans.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)

##TARUN

##mohan
#c1
