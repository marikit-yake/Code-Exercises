% Completed, July 2021

# Multiples of 3 or 5 -- Project Euler, Problem 1

## Example: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

## Goal: Find the sum of all the multiples of 3 or 5 below 1000

<img src="/multiples-3s-or-5s/images/Capture.PNG" alt="Code used in this project"/>


For the solution to this problem, I used a range function to generate a range object that included integers from 1-to-1000 (since natural numbers exclude zero). To keep the solution concise, explicit, and since we aren't working with a larger set of numbers, I chose to implement a list comprehension which loops over every number in our range object, only adding one of those numbers if they meet the criteria specified in the if-statement. 


## Solution: The sum of all the multiples of 3 or 5 below 1000:  233168

<img src="/multiples-3s-or-5s/images/solution.PNG" alt="Solution to this project"/>