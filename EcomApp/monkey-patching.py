import builtins

def my_print(message):
    with open('log.txt', 'a') as f:
        f.write(message + '\n')
    #builtins.print(message)

# Monkey patch the print function
builtins.print = my_print

# Now, every print statement will also log to a file
print("Hello, world!")
