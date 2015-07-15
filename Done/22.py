import sys
f=open("names.txt", 'r')
a=f.read()
a=a.split(',')
a=[i[1:-1] for i in a]
b=sorted(a)
c=[]
for ind,i in enumerate(b):
	d=[ord(j)-64 for j in i]
	c.append(sum(d)*(ind+1))

	if i=="COLIN":

print sum(c)
