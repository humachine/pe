def pathlen(x,a):
	if a[x]!=-1:
		return a[x]
	if x==1:
		return 1
	if x%2 ==0:
		a[x]=pathlen(x/2,a) + 1
		return a[x]
	else:
		a[x]=pathlen(3*x+1, a)+1
		return a[x]


a=[-1]*1000000000
a[1]=1
for i in range(35):
	if 2**i>1000000000:
		break
	else:
		a[2**i]=i+1


for i in range(1,10):
	pathlen(i,a)

print a[:10]
print max(a), a[4],a[8],a[5]
