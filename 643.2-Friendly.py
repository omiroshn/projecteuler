import gcd

def f(n):
	count=0
	i = 1
	while i <= n:
		j = i + 1
		while j <= n:
			d = gcd.gcd(i,j)
			if d != 1 and (d & (d-1)) == 0:
				count+=1
			j+=1
		i+=1
	return(count)

print(f(10**6))