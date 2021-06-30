import Sans

while True:
    text = input('Sans> ')
    result, error = Sans.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)


# TARUN
# Abhishek Pandey
# mohan
# Gaurang
# push and pull working
#mohan branch
