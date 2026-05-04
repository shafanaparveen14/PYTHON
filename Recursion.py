#Recursion - A function calling itself until a given condition satisfy.
#It has two cases:
#Base case-> The condition given to stop the recursive function.
#Recursive Function->it is the condition where function calling itself.

#Recursive Function
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
