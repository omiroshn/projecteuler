def checkPrime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

i = 2
countPrimes = 0
while countPrimes < 10001:
	if checkPrime(i) == True:
		countPrimes+=1
	i+=1
print(i-1)