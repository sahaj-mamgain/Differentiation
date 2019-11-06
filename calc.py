from sympy import *
from sympy.printing.mathml import print_mathml
from string import ascii_lowercase


def process_variables(input_string):
	'''
	Recursive function to take input string and remove functional text to count actual variables
	'''
	string = ''
	processed = input_string.split('+')
	for process in processed:
		if '(' in process:
			string += process_variables(process[process.find('(') + 1: process.find(')', process.find('(') + 1)])
		else:
			string += process
	return string


def calc_diff(inp_string):
	try:
		var_string = process_variables(inp_string)

		variables = list(set([variable for variable in var_string if variable in ascii_lowercase]))
		for variable in variables:
			exec(f'{variable}=Symbol("{variable}")')

		print('Variables found: ')
		for index, variable in enumerate(variables):
			print(f'{index + 1}. {variable}')

		diff_quotient = variables[int(input('Select the variable to differentiate against: ')) - 1]

		return True, print_mathml(diff(inp_string, diff_quotient))
	except Exception as e:
		print(e)
		return False, None


if '__main__' == __name__:
	print(calc_diff(input("Enter an expression to differentiate: ")))