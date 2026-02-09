filename=input("Enter the file name to open:")
try:
    with open(filename,"r") as file:
        print("\n--- File Content ---")
        print(file.read())

except FileNotFoundError:
    print("Oops! That file doesn't exist yet")