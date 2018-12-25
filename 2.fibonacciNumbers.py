one = 1
two = 1
mysum = 0
while two < 4000000:
	new = one + two
	one = two
	two = new
	if two % 2 == 0:
		mysum += two
print (mysum)