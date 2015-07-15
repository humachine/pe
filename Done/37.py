#Sieve of Eratosthenes
def primes_upto(limit):
	is_prime = [False] * 2 + [True] * (limit - 1) 
	for n in range(int(limit**0.5 + 1.5)): 
		if is_prime[n]:
			for i in range(n*n, limit+1, n):
				is_prime[i]=False
	return [i for i, prime in enumerate(is_prime) if prime]
N=1000000
#Checks for Prime number truncatability
def truncatable(x,a):
	y=x
	while y>10:
		if y in a:
			y=int(str(y)[1:])
		else:
			return -1
	
	y=x
	while y>10:
		if y in a:
			y=int(str(y)[:-1])
		else:
			return -1
	return 0
			

#Discards any primes which have an non-prime digits in them. We can go one further and also discard any primes>100 which have a 2 in them. (WE've ignored that case here)
def valid(x):
	if int(str(x)[0]) not in [2,3,5,7]:
		return -1
	if int(str(x)[-1]) not in [2,3,5,7]:
		return -1
	return 0


a=primes_upto(N)[4:]	#Get all Primes using sieve
ss=[i for i in a if valid(i)==0]		#get only valid primes
b=[i for i in ss if truncatable(i,a)==0]
print sum(b
