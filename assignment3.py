print("Enter the number in the list: ")
list1=list(map(int, input().split()))
list2=list1[:]
list2.sort()
list3=[]
for i in range(0,len(list1)):
	if(list2[i]==list2[i+1]):
		key=list2[i]#founding the multiple element in the list 
		break;
for j in range(0,len(list1)):
	if(list1[j]==key):
		list3.append(j)
print(list3)