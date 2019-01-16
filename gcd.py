def gcd(a,b):
	if (a>b):
		max = a
		min = b
	else:
		max = b
		min = a
	while (True):
		q = max // min
		r = max % min
		if r == 0:
			return min
		max = min
		min = r