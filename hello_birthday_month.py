from datetime import datetime
import sys

def main():
	name, month, current_month = get_info()
	display_name_length(name)
	display_birthday_message(month, current_month)


def get_info():
	name = input('What is your name? ').title()
	month = input('What month were you born in? ').title()
	current_month = datetime.now().strftime('%B')
	return name, month, current_month


def display_name_length(name):
	print('\nHello, {0}. Your name is {1} characters long.'.format(name, len(name)))


def display_birthday_message(month, current_month):
	if month == current_month:
		print('Happy birthday!')


main()
