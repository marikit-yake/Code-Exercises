num_list = range(1, 1000)
new_list = [
			num 
			for num in num_list 
			if (num % 3 == 0 or num % 5 == 0)
			]


print(f"\nList of Numbers:\n{new_list}\n")
print(f'Sum of Listed Numbers:\n{sum(new_list)}')