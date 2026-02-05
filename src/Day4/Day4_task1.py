contacts={"Mythili":7632874577,"Chaithanya":85490243564,"Prajna":6634923405}
print(contacts)
#new contact added as Thanya
print("Added new contact Thanya")
contacts["Thanya"]=7436723450
#updated phone number of existing Contacts
print(contacts)
print("updated phone number of existing contacts")
contacts["Mythili"]=8974563227
contacts["Chaithanya"]=7832456788
contacts["Prajna"]=7645332345
print(contacts)
#checks for name exists
print(contacts.get("Mythili"))
#checks if name doesn't exists and prints message as Contact not found
print(contacts.get("Navya","Contact not found"))
for Name,Number in contacts.items():
    print(f"Contact: {Name} | Phone: {Number}")