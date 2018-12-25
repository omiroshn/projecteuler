mysum = 0;
number = 0;
while number < 1000:
	if number % 3 == 0 or number % 5 == 0:
		mysum += number
	number += 1
print(mysum)