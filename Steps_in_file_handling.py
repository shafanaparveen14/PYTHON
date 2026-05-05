#Step 1st: Create and open file
#Creating a file and writing initial student data

file=open("students_details.txt","w")

file.write("101,Aman,98\n")
file.write("102,Shafana,89\n")
file.write("103,Alia,67\n")

file.close()

#Step 2: Search student
search_id="102"
found=False
file=open("students_details.txt","r")
for line in file:
    data=line.strip().split(",")
    if data[0]==search_id:
        print("student Found:",line)
        found=True
file.close()

#Step 3: Delete Operation
delete_id="103"
file=open("students_details.txt","r")
lines=file.readlines()
file.close()

file=open("students_details.txt","w")
for line in lines:
    data=line.strip().split(",")
    if data[0]!=delete_id:
        file.write(line)
file.close()
