"""Write script to enter 5 string in a list and check and print string whose length has even number of char
Date:24th March-2021"""
def creatlist():
    l=[]
    for i in range (5):
        s=input("Enter string:")
        l.append(s)
    return(l)
a=creatlist()
print(a)
