def get_multiplied_digits(number):
	str_number = str(number)
	first = int(str_number[0])
	r = 1
	while r == 1:
		if str_number[-1] == "0":
			str_number = str_number[:-1]
			if str_number[-1] == "0":
				r = 1
		else:
			break
	if len(str_number) == 1:
		return int(str_number)
	else:
		if int(str_number[0]) != 0:
			return first * get_multiplied_digits(int(str_number[1:]))
		else:
			return get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(int(input())))
print(get_multiplied_digits(int(input())))
print(get_multiplied_digits(int(input())))
