a=input()
a=a.split()
a[0]=int(a[0])
a[1]=int(a[1])
for i in range(a[0]+1,a[1]):
	for j in range(2,i):
		if(i%j==0):
			break
	else:
		if(a[1]-1!=i):
			print(i,end=' ')
		else:
			print(i)
		
