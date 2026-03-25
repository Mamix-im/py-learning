# Pront thr elements of the following list using th loop
# [1,4,9,16,25,36,49,64,,81,100]

num = [1,4,9,16,25,36,49,64,81,100,49]
x = 49

idx = 0
for el in num:
    if(el == x):
        print("numb found at idx", idx)
    idx += 1
