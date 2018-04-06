# phi is the symbol for the golden ratio
# phi.py calculates the golden ratio for any
# number given it, and assumes you have given the
# larger number first

import math

primary_length = input("First Length: ")

def isfloat(string):
	try:
		float(string)
		return True
	except ValueError:
		print("Exiting")
		exit()

while isfloat(primary_length):
	primary_length = float(primary_length)
	answer = 0
	if primary_length > 0:
		answer = round(primary_length / 1.618, 3)
	else:
		primary_length = abs(primary_length)
		answer = round(primary_length * 1.618, 3)
	print("\t", primary_length, " / ", answer, "\n")
	primary_length = input("First Length: ")