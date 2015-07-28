triangle=[n*(n+1)/2 for n in range(1, 30)]

f=open('inp.txt','r')
g=f.read()
g=g.split(',')
cnt=0
for line in g:
	x=sum([ord(i)-64 for i in line[1:-1]])
	if x in triangle:
		cnt+=1
print cnt
