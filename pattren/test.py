




from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# 1. RSA Key Pair (Public এবং Private key) জেনারেট করা
key = RSA.generate(2048)  # 2048-bit RSA key pair
private_key = key.export_key()  # Private key
public_key = key.publickey().export_key()  # Public key

# Public এবং Private Key প্রিন্ট করা
print(f"Public Key:\n{public_key.decode('utf-8')}")
print(f"\nPrivate Key:\n{private_key.decode('utf-8')}")

# 2. মেসেজ এনক্রিপ্ট করা হচ্ছে Public Key দিয়ে
message = b'
public_rsa_key = RSA.import_key(public_key)  # Public key ইম্পোর্ট করা হচ্ছে
cipher_rsa = PKCS1_OAEP.new(public_rsa_key)  # RSA cipher তৈরি করা
ciphertext = cipher_rsa.encrypt(message)  # এনক্রিপ্ট করা হচ্ছে

print(f"\nEncrypted Message (Ciphertext):\n{ciphertext}")

# 3. মেসেজ ডিক্রিপ্ট করা হচ্ছে Private Key দিয়ে
private_rsa_key = RSA.import_key(private_key)  # Private key ইম্পোর্ট করা হচ্ছে
cipher_rsa = PKCS1_OAEP.new(private_rsa_key)  # ডিক্রিপ্টর তৈরি করা
decrypted_message = cipher_rsa.decrypt(ciphertext)  # ডিক্রিপ্ট করা হচ্ছে

print(f"\nDecrypted Message:\n{decrypted_message.decode('utf-8')}")
