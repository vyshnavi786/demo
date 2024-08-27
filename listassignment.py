food=["biriyani","chappathi","noodles","pizza","burger","soup","chicken mandi","dragon chicken","fried rice"]
price=[120,30,200,450,350,250,500,400,300]
print(type(food))  # find type o
print(len(food)) #length of list
print("noodles" in food)
print("noodles" not in food)
food[4]="alfham"   # replace 
print(food)
food.append("shawai") # add new item
print(food)
food.insert(3,"ice cream") # add new item to a particular position
print(food)
food.extend(price) #
print(food)
food.remove("soup") # remove item
print(food)
food.pop(1)  #remove an item
print(food)
food.pop() # remove last item 
print(food)
price.sort() 
print(price)
price.sort(reverse=True)
print(price)
del food[9]
x=food.copy()
print(x)
y=list(food)
print(y)
print(food.count("dragon chicken"))
y.clear()
print(y)
del y

