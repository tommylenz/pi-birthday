import os

file = open('pi-billion.txt', 'r')
pi = file.read(100000000)
file.close()

birthday = input('Please type in your birthday.("DDMMYYYY" or "DDMMYY")')
length = len(birthday)

def birthday_pi(index_pi, index_birthday):
    if index_pi >= 100000000:
        return 1
    else:
        if birthday[index_birthday] == pi[index_pi]:
            if index_birthday >= length-1:
                return index_pi-index_birthday
            else:
                return birthday_pi(index_pi+1, index_birthday+1)
        else:
            return 0

b = 2
a = 0

while a == 0:
   a = birthday_pi(b, 0)
   b += 1

if a == 1:
    print('Your birthday is not in the first 100 Million digits of pi.')
else:
    print('Your birthday starts at digit number {} of pi.'.format(a-1))
