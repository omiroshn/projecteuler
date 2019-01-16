def gcd(a, b):
	while a!=0:
		c = a
		a = b % a
		b = c
	return b

def lcm(a, b):
	return a * (b / gcd(a, b))

def get_lcm_for(N):
	multiple = 1
	i = 1
	while i <= N:
		multiple = lcm(multiple,i)
		i+=1
	return multiple

print(get_lcm_for(20))