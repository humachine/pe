def pathlen(x,a):
	if x>=1000000:
		if x%2==0:
			return pathlen(x/2,a)+1
		else:
			return pathlen(3*x+1, a)+1
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


a=[-1]*1000000
a[1]=1

print 'Starting'
maxlen=1

for i in xrange(1,1000000):
	temp=pathlen(i,a)
	if temp>maxlen:
		print i, temp
		maxlen=temp
