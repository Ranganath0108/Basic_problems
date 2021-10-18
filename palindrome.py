
def is_palindrome(inputString):
    if(len(inputString)==0 or len(inputString)==1):
        return True
    if (inputString[0]==inputString[len(inputString)-1]):#checking whether the first and last element is same check for next first and last pair 
        return is_palindrome(inputString[1:len(inputString)-1])
    else:
        return False


a=input("Enter the text to check wheather it is palindrome o not \n")
if(is_palindrome(a) is True):
    print("It is a palindrome")
else:
    print("It is not a palindrome")