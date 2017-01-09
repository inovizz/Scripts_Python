def get_prime_numbers(n):
	my_list = []
	for j in xrange(1, n+1):
		for i in xrange(2, n):
			if (n % i) ==0:
				break
			else:
				my_list.append(j)
	return list(set(my_list))


def is_belz(number):
	list_ = get_prime_numbers(number)
	print list_
	x = 0
	for i in list_:
		if (i*(i+14)) == int(number) or (i*(i-14)) == int(number):
			x = 1
			return True
		else:
			pass
	if x == 0:
		return False

print is_belz(991)

