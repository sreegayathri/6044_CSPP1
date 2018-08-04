input_n = int(input())
result_a = 0
for i in range(1,input_n+1,1):
	if i*i*i == input_n:
		result_a = 1
	else:
		result_a = 0
if result_a == 1:
	print("perfect cube")
else:
	print("the number is not a perfect cube")