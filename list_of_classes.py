def main():
	classes = get_classes()
	display_classes(classes)


def get_classes():
	print()
	classes = []
	counter = 1
	while True:
		ordinal_indicator = get_ordinal_indicator(counter)
		classes.append(input('What\'s the name of your {0}{1} class? '.format(counter,ordinal_indicator)))
		counter = counter + 1
		if get_valid_response():
			break
	
	return classes


def display_classes(classes):
	print('\nYour classes:')
	for c in classes:
		print(c)
	print()


def get_ordinal_indicator(counter):
	second_last_digit, last_digit = get_last_digit(counter)

	if second_last_digit == 1:
		return 'th'
	elif last_digit == 1:
		return 'st'
	elif last_digit == 2:
		return 'nd'
	elif last_digit == 3:
		return 'rd'
	else:
		return 'th'


def get_last_digit(counter):
	string_count = str(counter)		# converting to string for manipulation
	last_digit = int(string_count[len(string_count)-1:]) # getting last character in string and converting back to int
	try:
		second_last_digit = int(string_count[len(string_count)-2:len(string_count)-1]) # getting last character in string and converting back to int
	except ValueError:
		second_last_digit = 0

	return second_last_digit, last_digit


def get_valid_response():
	response = input('Do you have another class? (Y/n) ').lower()
	while(response != 'y' and response != 'n'):
		print('Invalid response. Please enter \'y\' or \'n\':')
		response = input('Do you have another class? ').lower()
	return convert_response(response)


def convert_response(response):
	if response == 'y':
		return False
	elif response == 'n':
		return True


main()