def primeFactor(n):
	i = 2
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i;
	return n

n = 600851475143
print (primeFactor(n))