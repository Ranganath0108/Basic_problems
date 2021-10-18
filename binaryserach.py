def binarysearch(a,left,right,query):
    if (left > right):
        return -1
    mid=(left+right)//2

    if(query==a[mid]):
        return mid
    if(query>a[mid]):
        return binarysearch(a,mid+1,right,query)
    return binarysearch(a,left,mid-1,query)


a=[1,2,6,7,8,89]
hi=len(a)-1
li=0
print(binarysearch(a,li,hi,1))

   
    
    
