#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.lower() == 'admin' and password == "12345":
        return "Access granted"
    else:
       return "Access denied"
    

def hows_the_weather(temperature):
   dict_map = {
       temperature < 40 : "brisk",
       temperature >= 40 and temperature <65 : "a little chilly",
       temperature >= 85 : "too dang hot",
   }
   response = dict_map.get(True, "perfect")
   return (f"It's {response} out there!")


def fizzbuzz(num):
   if num % 5 == 0 and num % 3 == 0:
    return "FizzBuzz"
   elif num %  5 == 0:
    return "Buzz"
   elif num % 3 == 0:
    return "Fizz"
   else:
      return num

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None

