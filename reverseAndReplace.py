def strRevRep(inpStr):
    checklist = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 1
    string = ""
    if len(inpStr) < 50:
        for i in range(0, len(inpStr)):
            if inpStr[i] in checklist:
                string = string+str(count)
                count += 1
            else:
                string = string+inpStr[i]
    string = string[::-1]
    return string


a = input("Enter the string:\n")
print(f"{a} is changed to {strRevRep(a)}")
