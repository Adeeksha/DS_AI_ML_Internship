def calc_rectangle(length,width):
   area=length*width
   perimeter=2*(length+width)
   return area,perimeter
result=calc_rectangle(5,3)
area,perimeter=result
print(f"Area: {area}, Perimeter: {perimeter}")
