N=1001
s=0
curr=1
for i in range(3,N+1,2):
	for j in range(4):
		curr+=i-1
		s+=curr

print s+1

