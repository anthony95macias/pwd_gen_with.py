import random
import string

def generate_password(min_length=True, max_length=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    print(letters, digits, special)
    
generate_password(10)
    