import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
string_word = ''
print("Welcome to the PyPassword Generator!")
ask_letters = int(input("How many letters would you like in your password?\n")) 
ask_symbols = int(input("How many symbols would you like?\n"))
ask_numbers = int(input("How many numbers would you like?\n"))
password_list = []
for i in range(ask_symbols):
    password_list.append(random.choice(symbols))
for i in range(ask_letters):
    password_list.append(random.choice(letters))
for i in range(ask_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
for word in password_list:
    string_word = word + string_word
print(string_word)
