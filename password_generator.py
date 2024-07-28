import random
import string

def easy_password(len):
    words = ['a', 'b', 'c', 'd', '_', 'f', 'd', 'h', 't']
    easy_password = ''.join(random.choice(words) for _ in range (len))
    print(easy_password)

def hard_password(len):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range (len))
    print(password)

def generate_password():
    complexity = str(input('Enter your desired complexity (hard/easy): ')).strip().lower()
    lenght = int(input('Enter your desired lenght: '))

    while True:

        if complexity == 'easy':
            easy_password(lenght)
        else:
            hard_password(lenght)

        ask = str(input('Do you want another password? (yes/no): ')).strip().lower()
        if ask == 'yes':
            generate_password()
        elif ask == 'no':
            print('Goodbye')
        break
generate_password()