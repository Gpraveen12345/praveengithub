a=input()
a=a.split()
b=input()
b=b.split()
for i in range(len(a)):
	a[i]=int(a[i])
for i in range(len(b)):
	b[i]=int(b[i])
sum=0
for i in range(a[1]):
	sum=sum+b[i]
print (sum)
