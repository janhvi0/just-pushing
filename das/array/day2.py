# #rotate an array by k times
arr=[1,2,3,4,5,6,7]
k=3
k=k%len(arr)
l,r=0,len(arr)-1
while l<r:
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1

l,r=0,k-1
while l<r:
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1

l,r=k,len(arr)-1
while l<r:
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1

print(arr)

#rotate and check if its sorted



