total_bill=float(input("Enter the total bill amount:"))
people=int(input("Enter the number of people sharing the bill:"))
share_per_person=total_bill/people
print(f"Total bill:{total_bill}.Each person pays:{share_per_person}")
print(type(total_bill))
print(type(people))
print(type(share_per_person))