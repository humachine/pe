a=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
b=['twenty', 'thirty','forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
for i in b:
	a.append(i)
	for j in range(1,10):
		a.append(i+a[j])
for i in range(1,10):
	a.append(a[i]+'hundred')
	for j in range(1,100):
		a.append(a[i]+'hundredand'+a[j])
a.append('onethousand')
x=[len(i) for i in a]
print sum(x[1])
