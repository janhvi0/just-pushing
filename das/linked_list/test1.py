# palindrome without using slicing
def is_palindrome(str1):
    s, e = 0, len(str1) - 1
    
    while start < end:
        if str1[start] != str1[end]:
            return False
        start += 1
        end -= 1
    
    return True

str1 = "121"
print(is_palindrome(str1))  
str2 = "124"
print(is_palindrome(str2))  


def palindrome(num):
    rem=0
    while num!=0:
        rem=rem*10+num%10
        num=num//10





