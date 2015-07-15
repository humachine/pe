#Sieve of Eratosthenes
def primes_upto(limit):
	is_prime = [False] * 2 + [True] * (limit - 1) 
	for n in range(int(limit**0.5 + 1.5)): 
		if is_prime[n]:
			for i in range(n*n, limit+1, n):
				is_prime[i]=False
	return [i for i, prime in enumerate(is_prime) if prime]
N=1000000
#Checks for Prime number circularity
def circular(x,a):
	for i in range(1, len(str(x))+1):
		if int(str(x)[i:]+str(x)[:i]) in a:
			continue
		else:
			return -1
	return 0
#Discards any primes which have an even digit in them
def valid(x):
	if '2' in str(x) or '4' in str(x) or '6' in str(x) or '8' in str(x) or '0' in str(x):
		return -1
	return 0

a=primes_upto(N)[4:]	#Get all Primes using sieve
a=[i for i in a if valid(i)==0]		#get only valid primes (i.e primes without even digits)
b=[i for i in a if circular(i,a)==0]
print len(b)+4
