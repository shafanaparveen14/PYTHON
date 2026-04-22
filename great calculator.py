ch=int(input("Enter\n 1.for addition \n2.Subtraction\n3.Multipication\n4.Division\n"))
if(ch==1):
    num1=int(input("Enter first no. : "))
    num2=int(input("Enter second no. : "))
    sum=num1+num2
    print("Answer is ",sum)
elif(ch==2):
    num1=int(input("Enter first no. : "))
    num2=int(input("Enter second no. : "))
    sum=num1-num2
    print("Answer is ",sum)
elif(ch==3):
    num1=int(input("Enter first no. : "))
    num2=int(input("Enter second no. : "))
    sum=num1*num2
    print("Answer is ",sum)
elif(ch==4):
    num1=int(input("Enter first no. : "))
    num2=int(input("Enter second no. : "))
    sum=num1/num2
    print("Answer is ",sum)
else:
    print("you have entered wrong choice")
