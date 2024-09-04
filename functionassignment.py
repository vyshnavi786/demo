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
#fibanocci
def sequence(n):
    return [f(i) for i in range (n)]
def f(n):
    if n<=1:
        return n
    else:
        return f(n-1)+f(n-2)
n=int(input("enter the number :"))
result=sequence(n)
print(result)
#palindrome or not
def palindrome(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]
string=input("enter string:")
if palindrome(string):
    print(f'"{string}" is palindrome')
else:
    print(f'"{string}" is not palindrome')
#factorial
def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
number=int(input("enter a number :"))
print(f"factorial of a {number} is {factorial(number)}")
#square of list
numb=[2,3,6,8]
square=list(map(lambda x:x**2,numb))
print(square)
#multiplication
num=int(input("enter number"))
for i in range(1,11):
    m=i*num
    print(f"{i}*{num}={m}")


      



