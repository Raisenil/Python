message = "a"  # its a global variable


def greet(name):
    global message  # to use this message we can use this code
    message = "b"  # this is a local variable


greet("Raise nil")
print(message)
