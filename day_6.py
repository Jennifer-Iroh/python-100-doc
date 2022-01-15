# PYTHON FUNCTIONS OR NOT? LOL

#simple program to mask a person's password

username = input('Enter a username: ')
password = input('Enter your password: ')

password_length = len(password)
#mask password
secret = '*' * password_length

print(f' {username} Your password {secret} is {password_length} letters long ')

