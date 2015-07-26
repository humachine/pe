import itertools
N=['0','1','3','4','6']
a=list(itertools.permutations(N))

total=0
for i in a:
	j=''.join(i)
	if j[0]=='0':
		continue
	if int(j[3]) % 2 !=0:
		continue
	if int(j[2:5]) % 3 !=0:
		continue
	if int(j[-1]+'57') % 3 !=0:
		continue
	print j


