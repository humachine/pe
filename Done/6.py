N=101
s=0
for i in range(1,N):
	for j in range(i, N):
		if i!=j:
			s+=i*j
print s
