file = open("students.txt","w")
file.write("\nDeepanki\n")
file.close()

file = open("students.txt","r")
print(file.read())
file.close()

file = open("students.txt","a")
file.write("\npython\n")
file.close()

file = open("students.txt","r")
print(file.read())
file.close()