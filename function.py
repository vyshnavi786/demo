def sample():
    print("python is easy")
sample()
def add():
    a=2
    b=4
    c=a+b
    print(c)
add()
def demo(x):
    print(x)
demo(x="hallo")
def addition(x,y):
    d=x+y
    print(d)
addition(5,6) 
def new(*x):
    print(x[2])
new("apple","mango","orange","grape","lichi")
def r(x,y,z):
    print(x)
r(x=34,z=5,y=7)
def e(**x):
    print(x["a"])
e(a="python",b=34,c="india")
def dea(x=5):
    print(x)
dea(10)
def fault(x=5):
    print(x)
fault()
def turn(x,y):
    return x-y
print(turn(20,10))
def t():
    pass
def l(x):
    for i in x:
        print(i)
y=["python","easy","off"]
l(y)
def s(x):
    sum=0
    for i in range (1,x+1):
        sum+=i
    print(sum)
x=int(input("enter number"))
s(x)
v=lambda x,y:x+y
print(v(3,4))
a=lambda x,y,z:x+y+z
print(a(2,5,3))
fruit=["apple","mango","orange","pineapple","kiwi"]
w=list(map(lambda q:q.upper(),fruit))    
print(w) 
num=[20,3,14,15,6,7,18]
t=list(filter(lambda u:u>10,num))
print(t)   


