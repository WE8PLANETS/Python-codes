""" Write a program that takes string as a input it then returns the strings with every alternate letter capitalize 
    For EX: Lucknow  
            LuCkNoW
"""
takei=input("Enter the string: ")
l=len(takei)
for i in range(l):
    if(i%2==0):
        print(takei[i].upper(), end="")
    if(i%2!=0):
        print(takei[i].lower(), end="")
