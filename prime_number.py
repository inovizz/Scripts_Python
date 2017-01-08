my_list = []
for num in range(1,101):
    for i in range(2,num):
        if (num%i==0):
            break
	else:
             my_list.append(num)
print my_list
