N=1000000
s=0
for i in range(1,N+1):
	if str(i)==str(i)[::-1]:
		x=bin(i)
		if str(x)[2:] == str(x)[2:][::-1]:
			s+=i
print s
