x=[2,3,4,5,6,7,8,9]
a=list(filter(lambda e:e%2!=0,x))
print(a)
y=[2,3,4,5,6,7,8,9]
b=list(filter(lambda r:r %2==0,y))
print(b)
u=[2,3,4]
c=list(map(lambda o:o**2,u))
print(c)
def prime(n):
    if n<=1:
        print(f"{n} is not prime number.")
        return
    for i in range(2,n):
        if n % i==0:
            print(f"{n} is not prime number.")
            return
        print(f"{n} is prime number.")  
prime(4)

num=int(input("enter number"))
for i in range(1,11):
    m=i*num
    print(f"{i}*{num}={m}")


      



