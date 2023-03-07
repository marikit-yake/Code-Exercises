fib_array = [1,2]

def fib(n):

	# Reject any values equal to or lower than zero
	if n <= 0:
		print("Enter a higher value than 0 next time.")

	# If the given input is smaller than the length of the list
	# Return item at position [input - 1]
	elif n <= len(fib_array):
		return fib_array[n-1]
	
	# Calculate next step in fibonacci sequence
	# Append to the fibonacci array
	else:
		temp_fib = fib(n - 1) + fib(n - 2)
		fib_array.append(temp_fib)
		return temp_fib


fib(100)


# List comprehension capturing even numbers, based on previous fib_array
even_array = [
				num 
				for num in fib_array 
				if (num % 2 == 0 and num <= 4_000_000)
]

print(even_array)
print(sum(even_array))