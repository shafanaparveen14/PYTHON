#Adavanced Function
'''Decorator:A function that modifies other function without changind its original code'''
#Creating Decorator function
def my_decorator(func):
    def wrapper():
        print("Enter login Details")
        func()
        print("succesfully login")
    return wrapper

#Main function with decorator
@my_decorator
def say_hello():
    print("Hello")
#Calling main function with decorator   
say_hello()    
