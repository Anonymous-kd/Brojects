import random
import string

def password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = 8  
password = password(password_length)
print('Hi there, welcome to password generator:)')

print('yo password is', password)