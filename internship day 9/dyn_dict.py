mydict = {}
count = int(input("Total records: "))
for i in range(0, count):
    mykey= input("Enter the key: ")
    mydict[mykey] = input("Enter record value: ")
    
print(f"Values are {mydict}")