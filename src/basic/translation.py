def translation(phrase):
    res = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            res = res + "f"
        else:
            res = res + letter
    return res


print(translation(input("Enter a phrase")))


# Try / except

try:
    number = int(input("Enter a number \n"))
    print(number)
except ValueError as err:
    print("Invalid input:", err)
