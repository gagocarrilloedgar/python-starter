

def say_hi():
    print("hello world function")


def cube(num):
    return num*num*num


say_hi()
print(cube(3))


# Statements
is_male = False

if is_male:
    say_hi()
else:
    print("Goodbay")


# Statements
is_female = True

if is_female or is_male:
    print("Hi")
else:
    print("Goodbay")


# Dictionary
months = {
    0: "hola",
    1: "adiós"
}
