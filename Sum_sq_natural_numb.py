"""Python Program that dispay fist N number ad corresponding square 
   also display sm of the number and square of number at the end"""
n= int(input("Enter the number Length: "))
i=1
n_square=0
s_sum=0
n_sum=0
while i<=n:
    n_square=i*i
    print(f"Square of {i} = {n_square}")
    n_sum+=i
    i+=1
    s_sum+=n_square

print(f"Sum of Number = {n_sum}\nSum of Square = {s_sum}")


