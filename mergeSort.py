def MergeSort(data,start,end):
    if start < end:
        mid =(start+end)//2
        MergeSort(data,start,mid)
        MergeSort(data,mid+1,end)
        merge(data,start,mid,end)

def merge(data,start,mid,end):
    temp=[]

    i=start
    j=mid+1
    k=0


    while (i<=mid and j<=end):
        if(data[i]<=data[j]):
            temp[k]=date[i]
            k+=1
            # j+=1
            i+=1
        else:
            temp[k]=data[j]
            k+=1
            j+=1
            # i+=1
    while (i<=mid):
        temp[k]=data[i]
        k+=1
        i+=1
    while (j<=end):
        temp[k]=data[j]
        k+=1
        j+=1
    
    for i in range(start,end+1):
        data[i]=data[i-start]




a=[1,0,6,9,81,-1]
length=len(a)-1
a=MergeSort(a,0,length)
print("stop")