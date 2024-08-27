# tuple
a=("edit","select","go","run")
b=("italy","korea","river","malayalam","kerala")
print(a)
print(type(a))
print(len(a))
print("kerala" in a)
print("kerala" not in a)
for i in a:
    print(i)
print(a[3])
print(a[0:2])
print(a[1:])
print(a[:2])
print(b[-2:-1])
print(a[-2:])
print(b[:-2])    
c=list(a)
c.append("type")
print(c)
c.insert(2,"index")
print(c)
c[1]="time"
print(c)
c.remove("go")
print(c)
a=tuple(c)
print(a)
d=a+b
print(d)
e=a*2
print(e)
print(a.count("run"))

# set
r={"football","cricket","candy","food","sweet","angry","good"}
print(r)
print(type(r))
print(len(r))
for i in r:
    print(i)
print("candy"  in r) 
print("candy" not in r)
r.add("note")
print(r)
t={"bottle","dance",}
p={"cricket","new","football","good"}
r.update(t)
print(r) 
r.remove("angry")
print(r)
r.discard("food")
print(r)
r.pop()
print(r)
y=r.union(p)
print(y)
u=r.intersection(p)
print(u)
i=r.difference(p)
print(i)
t.clear()
print(t)
del t