#Exceptional Handling
'''try
x=int(abc)
except:
print("An error occured")
-------------------------------------------
try:
    num=int(input("Enter a number"))
    result=10/num
    print(result)
except ValueError:
    print("Please Enter a Valid Number")
except ZeroDivisionError:
    print("Cannot Divided by zero")
-------------------------------------------
'''
try:
    num=int(input("Enter a number"))
except ValueError:
    print("Please Enter a Number")
else:
    print("Success Correct it is number:",num)
finally:
    print("Execution finished")

