# try:
#     print("Trying 1 / 0")
#     total = 1 / 0
#     print("This will not show up")
# except Exception:
#     print("Exception was caught")
#     total = 0

# print(total)

num = input("What is a number? ")
try:
    num = int(num)
except Exception:
    num = "Unknown"

print(num)


            #^    ---CATCHING EXPRESSIONS-----

num = input("Enter a number: ")
num2 = input("Enter a second number: ")
try:
    num = int(num)
    num2 = int(num2)
    total = num / num2
except ValueError:
    print("Num or num2 were not valid numbers")
# except ZeroDivisionError:
#     print("Numbers could not be divided")
except Exception as e:
    print("Exception was caught")
    print(type(e))
#^ Ten divided by zero.

# Well, you can't divide anything by zero.

# We get a zero division error.

# So we said, OK, try to catch a value error if it exists.

# If it doesn't, let's try to catch the zero division error.

# We then caught that ZeroDivisionError  and printed something else out, and because this one was executed,

# the generic exception at the bottom was not executed.