
a=input()
a=a.split()
a[0]=int(a[0])
a[1]=int(a[1])
for i in range(a[0]+1,a[1]):
	if(i%2==0):
		if(a[1]-1==i):
			print(i)
		else:
			print(i,end=" ")
