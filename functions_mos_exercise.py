# THE FIZZ BUZZ ALGORITHM

#If the input is divisible by 3, it returns the string fizz
#If the input is divisible by 5, it returns the string buzz
#If the input is divisible by both 3 and 5, it returns the string fizz buzz
#If the input is not divisible by either 3 or 5, it returns the input


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "Fizz Buzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(10))




