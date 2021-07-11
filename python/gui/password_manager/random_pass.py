# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# for char in range(nr_letters):
#     password_list.append(random.choice(letters))
#
# for char in range(nr_symbols):
#     password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#     password_list += random.choice(numbers)
# The above one also works but we can reduce the code by using list comprehensions,exclusively in Python.

# nr_letters = random.randint(8, 10)
# nr_symbols = random.randint(2, 4)
# nr_numbers = random.randint(2, 4)
letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
symbols_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
numbers_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

password_list = letters_list + symbols_list + numbers_list
random.shuffle(password_list)

password = "".join(password_list)
pass_entry.insert(0, password)