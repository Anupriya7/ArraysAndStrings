def insertion(arr,n):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1

        arr[j+1]=key

    return arr


arr=[5,2,4,5,6,4]

print(insertion(arr,len(arr)))
