
# # Q1
# i = 100 
# while i >= 1 : # Stopping cond
#     print(i)
#     i-=1


# # Q2
# i = 1 
# while i <= 100 : # Stopping cond
#     print(i)
#     i+=1

# # Q3

# n = int(input("enter numb: "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i +=1

# # q4

# nums =[1,4,9,16,25,36,49,64,81,100]

# idx = 0 
# while idx < len(nums):
#     print(nums[idx]) # nums[0] , 
#     idx += 1

# # q5

# heroes = ["ironman","spider-man","thor","hulk"]

# idex = 0
# while idex <len(heroes):
#     print(heroes[idex])
#     idex += 1


# Q6

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
