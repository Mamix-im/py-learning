nums =[1,4,9,16,25,36,49,64,81,36,100]

x = int(input("enter you numb: "))

i = 0 
while i < len(nums):
    if(nums[i] == x):
        print("found idex" , i)
        break   # brek ( end of the loop)
    else:
        print("finding")
    i += 1

