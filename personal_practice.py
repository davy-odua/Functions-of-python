#Functions = a function is a block of reusable code.
#Return = return statement is used to end a function and send a result back to the caller.
#Parameters = The input you define for your function.
#Arguments = When calling functions, we need to supply values to those parameters.
#            We refer to these values as parameters.
#A parameter is the input you define for your function while an argument is the actual value for a given parameter.

#TYPES OF FUNCTIONS

#1. Functions that perform a task . For example print("Welcome")
#2. Functions that calculate and return a value. For example, return x + y

#Keyword arguments.
def increment(number, by):
    return number + by

result = increment(2, by= 1)
print(result)

#Default arguments.
def increments(number, by=9):
    return number + by

result2 = increments(2)
print(result2)

#Creating a function that takes a variable number of arguments.
def multiply(*numbers):
    count = 1
    for number in numbers:
        count *= number
    return count

result3 = multiply(2,3,4,5)
print(result3)


#We have a variation of the above syntax
def save_user(**user):
    print(user["id"])

save_user(id = 1, name = "Davy")
# In between the above , we have key value pairs which are the same of that of dictionaries.
#When we use double asterisks, we can have multiple key value pairs or multiple keyword arguments to a function and python will automatically package them into a dictionary.


#SCOPE = Refers to the region of the code where a variable is defined.
#for example
def greet(name):     #This function greet is the scope of the variable message.This is because this variable message can only be accessed from the function greet(). Like it only exists inside the greet function.
    message = f"Hello {name}"
    return message

final_name = greet("Davy")
print(final_name)

#The name and message variables are local variables since they are only defined inside the greet function.











