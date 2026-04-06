def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name} ")
    print("Welcome aboard")
# #So this function is now useful. We can call it using different arguments.
greet("Davy", "Codes")

def greeting(name):
    print(f"Hi {name}")
    return "'''"

print(greeting("Davy"))

def increment(number, by=1,):
    return number + by

print(increment(2, 5))

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

result = multiply(2,3,4,5)
print(result)

def save_user(**user):
    print(user["id"])

save_user(id = 1, name = "Davy", age = "21")

# scope = the region of the code where a variable is defined

message = "a"
def greet(name):
    message = "b" #The scope of this message variable is the greet function. It only exists inside this function

print(greet("Davy"))
print(message)

















