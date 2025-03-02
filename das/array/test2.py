#sort and reverse the array
def sort_array(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
    

def reverse_array(arr):
    temp=0
    for i in range(len(arr)//2):
        temp=arr[i]
        arr[i]=arr[len(arr)-1-i]
        arr[len(arr)-1-i]=temp
    return arr


arr=[5,10,15,20,-100]
# print(reverse_array(arr))
print(sort_array(arr))
# linkdlist


s= "hello world how are you"
st=s.split()