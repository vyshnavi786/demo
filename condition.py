#largest among the three numbers
d=int(input("enter first number"))
e=int(input("enter second number"))
f=int(input("enter third number"))
if d>e and d>f:
    print("d largest among")
elif e>d and e>f:
    print("e is largest")
else:
    print(" f is largest") 

#number is odd or even
t=int(input("enter the number"))
if t %2==0:
    print("number is even")
else:
    print("number is odd")  
#number is positive,negative or zero    
u=float(input("enter the num"))
if u>0:
    print("number is positive")
elif u<0:
    print("number is negative")
else:
    print("number is zero")            