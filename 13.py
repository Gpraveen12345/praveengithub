a=int(input())
c=1
for i in range(2,a):
	if(a%i==0):
		print("no")
		c=0
		break
else:
	
	print("yes")
