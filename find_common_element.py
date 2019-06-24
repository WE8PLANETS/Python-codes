def common_numb(l1,l2):
    l3=[]
    for i in l1 :
        if i in l2:
            l3.append(i)
    print(f"Common elements:{l3}")

L1=[]
L2=[]
L=[L1,L2]
numb=int(input("Enter the size of first list:"))
print("Enter the numbers in list 1:")
for i in range(numb):
    numbers=int(input())
    L1.append(numbers)

numb2=int(input("Enter the size of second list:"))
print("Enter the numbers in list 2:")
for i in range (numb2):
    numbers=int(input())
    L2.append(numbers)
print(f"LIST: {L}")

common_numb(L1,L2)
