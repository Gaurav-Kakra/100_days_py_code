#Password Generator Project
import random
import itertools

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

letter_pass = []
symbol_pass = []
number_pass = []

for i in range(0, nr_letters):
    a = random.randint(0, len(letters) - 1)
    letter_pass.append(letters[a])

for j in range(0, nr_symbols):
    b = random.randint(0, len(symbols) - 1)
    symbol_pass.append(symbols[b])

for k in range(0, nr_numbers):
    c = random.randint(0, len(numbers) - 1)
    number_pass.append(numbers[c])

# print(letter_pass)
# print(symbol_pass)
# print(number_pass)

pass1 = list(itertools.chain(letter_pass, symbol_pass, number_pass))

pass2 = ""
for l in pass1:
    pass2 = pass2 + l


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pass3 = ''.join(random.sample(pass2, len(pass2)))
print(pass3)