num=int(input("Enter a number:"))
def reverse(n):
    if n<10:
        return n
    else:
        return int(str(n%10)+str(reverse(n//10)))
def isPalindrome(n):
    if n==reverse(n):
        return 1
    else:
        return 0
if isPalindrome(num)==1:
    print("Palindrome")
else:
    print("Not a Palindrome")
        
