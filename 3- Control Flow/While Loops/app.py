#number = 100
# while number > 0:
#    print(number)
#    number //= 2

command = ""
#while command != "quit" and command !="QUIT":     this is not profesonal
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
