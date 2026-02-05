Dictionaries={"name":"neha","age":30}
print(Dictionaries)

#Dictionaries
student={
    "name":"amit",
    "age":21,
    "course":"Engineering"
}
print(student["name"])
student["age"]=22
student["city"]="Delhi"
print(student)

#dictionary methods and iteration
marks={"math":80,"science":75,"english":85}
print(marks.get("math"))
print(marks.get("history",0))
for subject,score in marks.items():
    print(subject,score)
#update
marks.update({"math":90})
print("marks after updation",marks)
marks.pop("science")
print("marks after deletion",marks)
print()
#using loop
purchases={"Kavya":90,"Preethi":870,"Amal":450}
for name,amount in purchases.items():
    print(f"{name} spent ₹{amount}")

print()
#input dictionary from user
n=int(input("Enter number of customers:"))
user_purchases={}

for i in range (n):
    name=input("Enter customer name: ")
    amount=int(input("Enter purchase amount for {name}:"))
    user_purchases[name]=amount
print("Customer purchase data:",user_purchases)

#person spending more
print()
top_customer=max(purchases,key=purchases.get)
top_value=purchases[top_customer]
print("top spending customer:",top_customer,"with amount:",top_value)


bottom_customer=min(purchases,key=purchases.get)
bottom_value=purchases[bottom_customer]
print("least spending customer:",bottom_customer,"with amount:",bottom_value)



print()

#sets
print("Sets")
numbers = {1, 2, 3, 3, 4}
print(numbers)
