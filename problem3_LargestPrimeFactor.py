# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

number_to_check = 3430
factor = 2
last_factor = 1

while (number_to_check > 1):

    if (number_to_check % factor == 0):
        last_factor = factor
        number_to_check /= factor
    else:
        factor += 1

print(last_factor)
