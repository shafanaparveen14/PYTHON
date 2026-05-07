#Step 1st: Create and open file
#Creating a file and writing initial student data

'''file=open("students_details.txt","w")

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
file=open("students_details.txt",w)
for line in lines:
    data=line.strip().split(",")
    if data(0)!=delete_id:
        file.write(line)
file.close()'''

'''#Step 4: update Students

uodate_id="103"
new_data="103,Pawan.98\n"

file=open("students_details.txt","r")
lines=file.readlines()
file.close()
file=open("students_details.txt","w")
for line in lines:
    data=line.strip().split(",")
    if data[0]==update_id:
        file.write(new_data)
    else:
        file.write(line)
file.close()
print("Students details updated successfully")
'''

#Read file line  by line:

file=open("students_details.txt","r")
print("\n Reading file line by line")
for line in file:
    print(line.strip())
file.close()

#Remove lines containing
input_file=open("students_details.txt","r")
output_file=open("filtered.txt","w")
for line in input_file:
    if 'n' not in line:
        output_file.write(line)
input_file.close()
output_file.close()
print("\nFilterd File created(no 'n' lines")
print("---------------------------------")
file=open("filtered.txt","r")
print("\n Reading file line by line")
for line in file:
    print(line.strip())
file.close()
































