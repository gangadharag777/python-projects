with  open("data.txt","r+") as file:
    print(file.read())
    file.write("am fine")
file.close()
    