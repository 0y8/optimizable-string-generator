import random
import secrets
import string

amount = input('How many strings: ')
length = input('String length: ')

amount = int(amount)
length = int(length)

for line in range(amount):
    r_string = ''.join(secrets.choice(string.ascii_lowercase + string.ascii_lowercase)
                       for i in range(length))
    print(r_string)