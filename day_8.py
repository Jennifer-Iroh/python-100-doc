# FUNCTION WITH INPUTS!!!!
# 1. Prime number Checker

# n = int(input("Enter number to check if it is a prime number: "))

# def prime_num_checker(num):
#     for i in range(2, num):
#         if (num % i == 0):
#             print("Not a prime number")
#             exit()
#     print("A prime number")

# prime_num_checker(n)

# 2. Ceaser Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar_cipher(input_text, shift_no, shift_direction):
    message = ""
    for char in input_text:
        if char in alphabet:
            old_value = alphabet.index(char)
            if shift_direction == "encode":
                message += alphabet[old_value + shift_no]
            elif shift_direction == "decode":
                message += alphabet[old_value - shift_no]
    if shift_direction == "encode":
        print(f"Your encrypted text is {message}")
    else:
        print(f"Your decrypted text is {message}")


caesar_cipher(text, shift, direction)
