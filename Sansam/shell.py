import Run

while True:
    text = input('Sans> ')
    result, error = Run.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
