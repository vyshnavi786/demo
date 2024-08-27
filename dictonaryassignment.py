p={"film":"stree","language":"hindi","category":"horror"}
print(p)
print(len(p))
print(type(p))
print("film" in p)
print("film" not in p)
print(p["film"])
print(p.get("film"))
print(p.keys())
print(p.values())
print(p.items())
p["film"]="darkest hour"
print(p)
p.update({"language":"english"})
print(p)
p["price"]=150
print(p)
p.update({"payment":"online"})
print(p)
p.pop("price")
print(p)
p.popitem()
print(p)
del p["category"]
print(p)
for i in p:
    print(i)
for i in p:
    print(p[i])    
for i in p.keys():
    print(i)    
for i in p.values():
    print(i)
for i in p.items():
    print(i)  
q=p.copy()
print(q)
r=dict(p)
print(r)   
p.clear()
print(p)
del p
division={"div1":{"students":"adith","rollno":1},"div2":{"students":"abinav","rollno":2},"div3":{"students":"abin","rollno":3}}
print(division)
print(division["div1"])
print(division["div2"]["students"])
print(division["div3"]["rollno"])

