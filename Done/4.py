m=1
for i in range(999,100,-1):
	for j in range(999,100,-1):
		x=i*j
		if str(x) == str(x)[::-1] :
			if x>m:
				m=x
				print i,j

print m
