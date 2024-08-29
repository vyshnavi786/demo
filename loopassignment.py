#sum of first ten natural numbers
num=1
sum=0
for i  in range(1,11):
    sum+=i
print(sum)
#factorial of a number
n=5
r=1
for i in range(1,n+1):
    r*=i
print(r) 
#sum of even number    
even=0
for i in range(1,21):
    if i %2==0:
        even+=i
print(even)
#sum of square of first ten numbers 
square=0
for i in range(1,11):
    square+=i**2
print(square)  
#fabinocci series 
number=10
a,b=0,1
count=0
print(a,end='')
for i in range (1,number):
    print(b,end='')
    c=a+b
    a=b
    b=c
#average of three numbers    
a=int(input("enter the first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
sum=0
sum=a+b+c
avg=sum/3
print(avg)
#number is prime or not  

x = int(input("Enter a number: "))

if x == 1:
    print("The number is not a prime number")
elif x > 1:
    for i in range(2, x):
        if x % i == 0:
            print("The number is not a prime number")
            break
    else:
        print("The number is prime")



