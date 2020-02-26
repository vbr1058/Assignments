arr = list(map(int, input().split()))
final_arr=[]
for i in arr:
	if i not in final_arr:
		final_arr.append(i)
print(final_arr)