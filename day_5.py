import random

print("Welcome to the PyPassword Generator!")
num_let = int(input("How many letters would you like in your password?\n"))
num_sym = int(input("How many symbols would you like?\n"))
num_num = int(input("How many numbers would you like?\n"))

num_all = num_let + num_num + num_sym

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
possible = [letters, numbers, symbols]

password = ""

for i in range(0, num_let):
    password += letters[random.randint(0, len(letters) - 1)]
    print(password[i])
for i in range(0, num_sym):
    password += random.choice(symbols)
for i in range(0, num_num):
    password += random.choice(numbers)

as_list = list(password)
random.shuffle(as_list)
final_password = ''.join(as_list)
print(final_password)
