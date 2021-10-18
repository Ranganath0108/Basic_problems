def countChar(inputString):
    count=dict()
    for i in inputString:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    return count



a="Ranganathaswamy"
print(countChar(a))    