list =[]
size = int(input("enter number of elements u want to enter:"))
for i in range(size):
    list.append(int(input()))
le =len(list)
total =0
for k in list:
    total +=k
avg =total/le

print("Avg",avg)