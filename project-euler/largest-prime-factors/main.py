# Prime Number Factorization -- Sieve of Eratosthenes
# Project Euler
# EXAMPLE : The prime factors of 13195 are [5, 7, 13, 29]
# GOAL : Find the largest prime factor of the number 600851475143


def prime_factor(n):
	divisor = 2
	prime_factors = []


	# Prime numbers are larger than 1
	# Divisible by exclusively themselves and 1
	# if n <= 2:
	# 	return []

	# While n is larger than the divisor (result of division is greater than 1)
	while divisor <= n:
		if n % divisor == 0:
			prime_factors.append(divisor)
			n = n / divisor
		else:
			divisor += 1

	print(prime_factors)
	return prime_factors


prime_factor(100)
prime_factor(13195)
# print(max(prime_factor(600_851_475_143)))