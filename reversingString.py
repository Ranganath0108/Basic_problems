def reverseString(inputString):
    if inputString == " ":
        return " "
    if len(inputString)== 0 or len(inputString)==1:
        return inputString
    result=inputString[len(inputString)-1]+reverseString(inputString[0:len(inputString)-1])
    return result
    

a=input("Enter the text:\t")
print(f"{a} text is reversed as {reverseString(a)}")
   
