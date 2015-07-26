year=1900
date=1

[JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER]=range(1,13)
[SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY]=range(7)

month=JANUARY
ans=0
date=1
while 1:
	if month in [JANUARY, MARCH, MAY, JULY, AUGUST, OCTOBER, DECEMBER]:
		date+=31
		month+=1
	elif month in [APRIL, JUNE, SEPTEMBER, NOVEMBER]:
		date+=30
		month+=1
	elif month==FEBRUARY:
		if year%4 ==0 and year!=1900:
			date+=29
			month+=1
		else:
			date+=28
			month+=1
	
	if date%7==0:
		ans+=1
	if month==13:
		year+=1
		month=1
	if year==2001:
		break
	date=date%7
	
print ans

