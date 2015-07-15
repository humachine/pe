f=open('in.txt', 'r')
a=f.read()
a=a.split()
a=[i.rstrip('\n') for i in a]
b=""
for i in a:
	b+=i
N=1000
ans=1
for i in range(0,N-13):
	prod=1
	for j in range(13):
		prod*=int(b[i+j])
		if prod>ans:
			ans=prod

print ans
f.close()
