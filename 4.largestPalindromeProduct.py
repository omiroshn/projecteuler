def checkOnPalindrom(n):
	m = n
	new = 0
	while m != 0:
		z = m % 10
		new = new * 10 + z
		m //= 10
	if new == n:
		return True
	return False

def product():
	last = 0
	ii = 0
	jj = 0
	i = 999
	while i >= 100:
		j = 999
		while j >= 100:
			if checkOnPalindrom(i*j) == True:
				if (i * j > last):
					last = i * j
					ii = i
					jj = j
			j-=1
		i-=1
	print (ii," ",jj)
	return last

print (product())