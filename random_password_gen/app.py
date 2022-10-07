import random
import string

import pyperclip

chars = list(string.ascii_letters + string.digits + '!@#$%^&*()')


def generate_pwd(length):
    return ''.join([random.choice(chars) for i in range(length)])


def main():
    length = int(input('Enter the length of the password: '))
    gen_pwd = generate_pwd(length)
    pyperclip.copy(gen_pwd)
    print("Password copied to clipboard")
    print(f'Generated password: {gen_pwd}')


main()
