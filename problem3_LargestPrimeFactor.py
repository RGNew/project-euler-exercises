# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

number_to_check = 600851475143
factorial = 2
last_fact = 1

while (number_to_check > 1):

    if (number_to_check % factorial == 0):
        last_fact = factorial
        number_to_check /= factorial

    factorial += 1

print(last_fact)