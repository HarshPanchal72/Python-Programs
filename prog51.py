# 4. A RAJIV hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, 
# such as the complete works of William Shakespeare. Well, suppose we replace a RAJIV with a Python function.

import random
import string

def random_string(length):
    return ''.join(random.choices(string.ascii_letters + ' ', k=length))

def generate_until_match(target):
    target_length = len(target)
    attempts = 0
    
    while True:
        random_text = random_string(target_length)
        attempts += 1
        
        if random_text == target:
            return attempts, random_text

target_text = "Hello World"
attempts, matched_text = generate_until_match(target_text)
print(f"Found the target text '{matched_text}' after {attempts} attempts.")
