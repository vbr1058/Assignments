stduent_dict={}
num= int(input("Enter the number of student: "))
for i in range(num):
	Name=input("Enter the Name: ")
	USN=input("Enter the USN: ")
	stduent_dict[USN]=Name
print(stduent_dict)