# Largest Palindrome Product
# Project Euler

# EXAMPLE : A palindromic number reads the same both ways. 
#			The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99
# GOAL : Find the largest palindrome made from the product of two 3-digit numbers.


def main():
	# Input, n: Length of integers for multiplying	
	n = int(input("Enter preferred length of digits: "))
	largest_pal = 0
	list_of_pals = []

	# Create iterable values for multiplying and checking palindromic values
	for x in range((10**n)-1, (10**(n-1)), -1):
		for y in range((10**n)-1, (10**(n-1)), -1):
			result = x * y
			if is_pal(result) == False:
				continue
			else:
				list_of_pals.append(result)

	# Print the largest palindrome product possible using n-length digits
	print(f"\nLargest Palidromic Product, given n-length digits: {max(list_of_pals)}")


def is_pal(test):
	test = str(test)
	lst = []

	# Result must be read the same forwards and backwards
	if test == test[::-1]:
		lst.append(int(test))
		return True
	else:
		return False


main()