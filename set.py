t={"java","china","bird","mountain","pandas"}
print(t)
print(type(t))
print(len(t))
print("china" in t)
print("china" not in t)
for i in t:
    print(i)
t.add("new")
print(t)
i={"lion","old,"}
t.update(i)
print(t) 
t.remove("pandas")
print(t)
t.discard("number")
print(t) 
t.discard("bird")
print(t)
t.pop()
print(t) 
z=t.union(i)
print(z)
j={"java","python","china","hallo"}
k={"java","python","tea","india"}
l=j.intersection(k)
print(l)
m=j.difference(k)
print(m)
k.clear()
print(k)
del k




