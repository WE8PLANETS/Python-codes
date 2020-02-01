#Write a program that reads a line and prints \
""" No of Upper case letters
    No of Lower case Letters
    NO of Alphabets Letters
    No of digits"""

line=input("Enter the line :")
uc=lc=al=di=0
l=len(line)
for i in range(l):
    if(line[i].isupper()):
        uc+=1
    if(line[i].islower()):
        lc+=1
    if(line[i].isalpha()):
        al+=1
    if(line[i].isdigit()):
        di+=1
print(f" No of Upper Case= {uc} \n No of lower Case= {lc} \n No of Alphabets= {al} \n No of Digits= {di}")