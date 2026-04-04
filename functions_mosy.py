def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name} ")
    print("Welcome aboard")
#So this function is now useful. We can call it using different arguments.
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













def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first +" "+ last

full_name = create_name("davy", "codes")
print(full_name)




















