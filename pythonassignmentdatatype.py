a=7
b=5.345
c=6+3j
print(type(a))
print(type(b))
print(type(c))
x=float(a)
print(x)
print(type(x))
y=complex(a)
print(y)
print(type(y))
i=int(b)
print(i)
print(type(i))
j=complex(b)
print(j)
print(type(j))

#string assignment
d="python programme is versatile"
e="data science is growing field "
g="python, is,p easy to use"
print(len(d)) # print length of string
print("is" in d)   # membership function
print("is" not in d)
for i in e:   # loop
    print(i)
print(d[5])  # array to find position
print(e[3:8])# slicing
print(e[4:])
print(e[:9])
print(d[-2:-8]) # inverse indexing
print(d[-4:])
print(d[:-9])
print(d.upper()) # convert string to upper case
print(d.lower()) # convert string to lower case
print(e.strip()) # strip operation to remove white space
print(d.replace("python","java")) 
print(g.split(","))
print(d+e) #  merging to strings 
f=7
print(f"i am {f} year old") # use formmated string
print(e.count(i)) # count how many times a character appear in a string


