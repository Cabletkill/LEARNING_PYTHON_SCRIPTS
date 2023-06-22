''''
Why do we use exception handlers?
Catch errors within a program

What is the purpose of a try…except statement?
Catch and handle exceptions when an error occurs

'''
a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")