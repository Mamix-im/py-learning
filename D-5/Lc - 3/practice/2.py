#WAP to check if a list contains a palindrome of elements. 

list1 = ["m","a","a","m"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")