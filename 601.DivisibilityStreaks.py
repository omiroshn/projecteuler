# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    601.DivisibilityStreaks.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omiroshn <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/26 17:48:19 by omiroshn          #+#    #+#              #
#    Updated: 2018/12/26 17:48:20 by omiroshn         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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

def P(s, N):
	lcm = get_lcm_for(s)
	lcm2 = get_lcm_for(s + 1)
	return ((N-2)//lcm-(N-2)//lcm2)

mysum = 0
for i in range(1,32):
	mysum += P(i,pow(4,i))
	print ("sum of i: {0} {1}".format(mysum, i))
print(mysum)