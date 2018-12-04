# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sum_of_numbers = 0  # initializes the sum to 0

for i in range(1000):  # runs a for loop from 0 to 1000
    if (i % 3 == 0 or i % 5 == 0):  # checks if number is multiple of 3 or 5
        sum_of_numbers += i  # if number is multiple, adds it to the sum

print(sum_of_numbers)  # prints the sum to the console