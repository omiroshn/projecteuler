def isPrime(n):
	for i in range(2,n//2):
		if n%i==0:
			return False
	return True

sum = 0
for i in range(2,2000001):
	if i > 10000 and not i % 2 == 0:
		if isPrime(i):
			sum+=i
print(sum)
