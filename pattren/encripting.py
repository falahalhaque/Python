"""import random
import string

# বিভিন্ন অক্ষরের তালিকা তৈরি করা
chars = string.punctuation + string.ascii_letters + string.digits  # punctuation, letters, এবং digits যুক্ত করা
chars = list(chars)

# একটি শাফল করা কীবোর্ড তৈরি করা
key = chars.copy()
random.shuffle(key)

print(f"Original chars: {chars}")
print(f"Shuffled key: {key}")

# এনক্রিপশনের জন্য ব্যবহারকারী থেকে ইনপুট নেওয়া
plain_text = input("Enter the text to encrypt: ")
cipher_text = ""

# প্রতিটি অক্ষরকে এনক্রিপ্ট করা
for letter in plain_text:
    if letter in chars:
        index = chars.index(letter)
        cipher_text += key[index]  # শাফল করা কী ব্যবহার করে এনক্রিপ্ট করা
    else:
        cipher_text += letter  # যদি অক্ষর তালিকায় না থাকে, মূল অক্ষর সংরক্ষণ করা

print(f"Cipher Text: {cipher_text}")
"""
import random
import string

# অক্ষরের তালিকা তৈরি করা
char = " " + string.punctuation + string.ascii_letters + string.digits  # সঠিকভাবে যুক্ত করা
char = list(char)

# শাফল করা কীবোর্ড তৈরি করা
key = char.copy()
random.shuffle(key)

print(f"Original chars: {char}")
print(f"Shuffled key: {key}")

# ইনপুট নেওয়া
plaine_text = input("Enter a message to encrypt: ")
cipher_text = ""

# প্রতিটি অক্ষর এনক্রিপ্ট করা
for letter in plaine_text:
    if letter in char:  # চেক করা যাতে অক্ষরটি তালিকায় আছে কিনা
        index = char.index(letter)
        cipher_text += key[index]  # সঠিকভাবে key[index] ব্যবহার করা
    else:
        cipher_text += letter  # যদি অক্ষর তালিকায় না থাকে, মূল অক্ষর সংরক্ষণ করা

print(f"Original message: {plaine_text}")
print(f"Encrypted message: {cipher_text}")

