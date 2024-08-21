x=[3,"apple","flower","python","java","graph"]
print(x)
print(type(x))
print(len(x))
print("apple" in x)
print("plain" in x)
print("apple" not in x)
print("plain" not in x)
for i in x:
    print(i)
print(x[1])    
print(x[0:3])
print(x[2:])
print(x[:4])
print(x[-1])
print(x[-4:-1])
print(x[-2:])
print(x[:-3])
x[1]="mango"
print(x)
x.append("bird")
print(x)
x.insert(3,"edit")
print(x)
y=[5,"file","sea","sky"]
print(y)
x.extend(y)
print(x)
x.remove("flower")
print(x)
x.pop(3)
print(x)
x.pop()
print(x)
del x[0]
print(x)
z=["orange","mango","graph","apple"]
print(z)
z.sort()
print(z)
z.sort(reverse=True)
print(z)
a=x.copy()
print(a)
b=list(x)
print(b)
c=x+y
print(c)
print(x.count("java"))
z.clear()
print(z)
del z


