a = 1
for a in range(1,1000):
	b = 2
	for b in range(1,1000):
		c = 3
		for c in range(1,1000):
			if a*a+b*b==c*c:
				if a+b+c == 1000:
					print("prod:",a*b*c)
			c+=1
		b+=1
	a+=1