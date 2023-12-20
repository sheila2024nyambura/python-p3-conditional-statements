#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == "admin" or username == "ADMIN") and password == "12345":
        login = "Access granted"
    else :
        login = "Access denied"
    return login
print(admin_login("admin", "1254345"))


def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        response = "brisk"
    elif temperature >= 40 and temperature < 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
    return(f"It's {response} out there!")
print(hows_the_weather(55))


def fizzbuzz(num):
    # your code here
    if (num%3 == 0 and num%5 == 0):
       return "FizzBuzz"
    elif (num %3 == 0):
       return "Fizz"
    elif (num %5 == 0):
       return "Buzz"
    else:
       return num

def calculator(operation, num1, num2):
    # your code here
    if (operation == "+"):
       return num1 + num2
    elif (operation == "-"):
       return num1 - num2
    elif (operation == "*"):
       return num1 * num2
    elif (operation == "/"):
       return num1 / num2
    else:
       print("Invalid operation!")
       return None