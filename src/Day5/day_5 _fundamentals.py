#function
def greet():
 print("Hello,Welcome to the internship!")
greet()

print()

#arguments and return values
def add_numbers(a,b):
  return a+b
result=add_numbers(5,3)
print(result)

print()

#variable scope(local vs global)
x=10
def show_value():
 x=5
 print(x)
show_value()
print(x)

print()

Cho="Kit kat"
def eatable():
  
  print("i like ",Cho)
eatable()

print()
#importing standard modules
import math
import random
print(math.sqrt(16))
print(random.randint(1,10))


 





