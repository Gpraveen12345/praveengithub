n=input()
n=n.lower()
if(n=='a' or n=='e' or n=='i' or n=='o' or n=='u'):
	print ("Vowel")
elif(ord(n)>=97 and ord(n)<=123):
	print("Constent")
else:
	print("invalid")
