def happy_birthday(name, age):
    print(f"Happy Birthday to {name} !!!")
    print(f"You are {age} years old")
    print("Happy Birthday to you!!!")

happy_birthday("Davy", "21")
print()
happy_birthday("Bro", "25")
print()
happy_birthday("Kevin", "30")


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Davy", 42.50, "04/5/2026")

def add(x,y):
    return x + y

z = add(1, 2)
print(z)

w = add(2,3)
print(w)

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first +" "+ last

full_name = create_name("davy", "codes")
print(full_name)



def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

result = multiply(2,3,4,5)
print(result)


















