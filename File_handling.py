'''#Create a file and write data into it
file=open("student.txt","w")#Write mode(create file)
file.write("Name:Shafana\n")
file.write("Course:B.tech\n")
file.write("Deptartment:CST\n")
file.close()
print("File Created and data written successfully")

#read data from it
file=open("student.txt","r") #Read mode (read content inside file)
data=file.read()
print(data)
file.close()
#Append Data (Add new data without deleting old data)
file=open("student.txt","a")
file.write("City:Indore\n")
file.close()
#Read whole content of file also append data
file=open("student.txt","r")
for line in file:
    print(line.strip())#remove extra newline
file.close()'''

#Update Specific Content
file=open("student.txt","r")
data=file.read()
file.close()

data=data.replace("Shafana","Khushboo")
file=open("student.txt","w")
file.write(data)
file.close()
print("File updated successfully")

file=open("student.txt","r")
updated_data=file.read()
print(updated_data)
file.close()

#Delete Content inside file
with open("student.txt","w") as file:
    file.write("")
print("File cleared Successfully")

file=open("student.txt","r")
data=file.read()
print(data)
file.close()
      
