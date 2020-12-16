def selection(arr,n):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min]):
                min=j

        arr[i],arr[min]=arr[min],arr[i]

    return arr


arr=[5,6,8,9,4]

print(selection(arr,len(arr)))

