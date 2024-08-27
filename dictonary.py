a={"name":"devan","age":16,"place":"india","course":"flutter"}
print(a)
print(type(a))
print(len(a))
print(a["name"])
print(a.get("name"))
print(a.keys())
print(a.values())
print(a.items())
print("name" in a)
print("name" not in a)
a["name"]="sini"
print(a)
a.update({"age":42})
print(a)
a["job"]="teacher"
print(a)
a.update({"salary":35000})
print(a)
a.pop("course")
print(a)
a.popitem()
print(a)
del a["place"]
print(a)
for i in a:
    print(i)
for i in a:
    print(a[i])
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i) 
b=a.copy()
print(b)
c=dict(a)
print(c)
a.clear()
print(a)
del a
family={"child1":{"name":"alex","age":23},"child2":{"name":"sam","age":27},"child3":{"name":"sandra","age":23}}
print(family)
print(family["child2"])
print(family["child2"]["age"])
print(family["child3"]["name"])

       

