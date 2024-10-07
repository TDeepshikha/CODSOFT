import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    characters = ''
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
  
password_length = 16
password = generate_password(length=password_length)
print("Generated password:", password)
