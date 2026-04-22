year=int(input("Enter any year to check weather it is leap year or not\n"))
if(year%4==0 & year%400==0 |year %100==0):
    print("This  year is a leap year")
else:
    print ("not a leap year")
    
