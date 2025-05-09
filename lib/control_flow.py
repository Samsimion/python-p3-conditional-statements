#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == "admin" or username == "ADMIN") and password =="12345":
         return "Access granted"
    else:
        return "Access denied"
    



def hows_the_weather(temperature):
    if temperature<40 :
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature >85 :
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    


    

def fizzbuzz(num):
    if num %3==0 and num % 5 ==0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    
    else :
        return num

    
   

def calculator(operation, num1, num2):
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                return "Cannot divide by zero!"
            result = num1 / num2
        else:
            print("Invalid operation!")
            return None
        print("Isn't this calculator fun?")
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: input must be of type int or float"
    except ValueError as e:
        return str(e)



