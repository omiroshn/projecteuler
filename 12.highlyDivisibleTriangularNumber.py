def factors(v):
	count = 0
	for i in range(1,v+1):
		if v % i == 0:
			count+=1
		i+=1
	return count

def triangle(n):
	sum = 0
	for i in range(1,n+1):
		sum+=i
	return sum

# print(factors(triangle(50000)))

sum = 0
for i in range(1,10000000):
	sum+=i
	if factors(sum) >= 500:
		print(sum)
		break


# i = 
# while factors(triangle(i))