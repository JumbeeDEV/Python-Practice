import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for char in range(0, nr_letters + 1):
    random_char = random.choice(alphabet)
    password = password + random_char

for number in range (0, nr_numbers + 1):
    random_number = random.choice(numbers)
    password = password + random_number

for symbol in range(0, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password = password + random_symbol

print(password)

password_list = list(password)
random.shuffle(password_list)
shuffled_password = "".join(password_list)
print(shuffled_password)