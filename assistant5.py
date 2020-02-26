arr = list(map(str, input().split()))
arr=[ele for ele in reversed(arr)] 
for i in range(len(arr)):
	print(arr[i],end=" ")