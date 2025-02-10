def find_max_element(arr):
    max_num= arr[0]
    for i in arr:
        if i>max_num:
            max_num=i
    return max_num
    
def find_second_max_element(arr,max_num):
    second_max = arr[0]
    for i in arr:
        if i>second_max and i<max_num:
            second_max=i
        return second_max


def check_if_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

def main():
    arr=[5,10,15,20,-100]
    print("The second largest number is:", find_second_max_element(arr, max_num=20))
    print("The largest number is:", find_max_element(arr))
    print(check_if_sorted(arr))

if __name__ == "__main__":
    main()
