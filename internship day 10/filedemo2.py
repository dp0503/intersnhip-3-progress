with open("myfile.txt", "a") as myfile:
    myfile.write("This is a new line.\n")
with open("myfile.txt", "r") as myfile2:
    content = myfile2.read()
    print(content)