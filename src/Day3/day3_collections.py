#List example
numbers=[10,20,30,40]
#Tuple example
coordinates=(5,10)
print(numbers)
print(coordinates)


#indexing and Slicing=start,stop,skip
a=[100,200,300,400,500]
print(a[-3:-1])
print(a[1:4:2])
print(a[1:4:1])
print(a[1:4:3])
print(a[-4:-1:2])

#append,insert,extend,sort
a=[8,7,6,9]
a.sort()
print(a)

a.reverse()#can use only rev for descending order
print(a)

a.append(10)
print(a)

a.insert(2,15)
print(a)

a.extend([20,25,30])
print(a)