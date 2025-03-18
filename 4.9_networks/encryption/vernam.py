import random
from itertools import product

class VCipher():
    def generate_keyset(self, length):
        return [random.randint(0, 1) for _i in range(length)]

    def encrypt(self, plaintext, keyset):
        if len(plaintext) != len(keyset):
            return "incorrect keyset length"
        else:
            i = 0
            ciphertext = ""
            while i < len(plaintext):
                char = plaintext[i]
                key = keyset[i]
                ciphertext += chr(ord(char) + key)
                i += 1
            return ciphertext

    def decrypt(self, ciphertext, keyset):
        if len(ciphertext) != len(keyset):
            return "incorrect keyset length"
        else:
            plaintext = ""
            i = 0
            while i < len(ciphertext):
                char = ciphertext[i]
                key = keyset[i]
                plaintext += chr(ord(char) - key)
                i += 1
            return plaintext

# vc = VCipher()
# a = vc.encrypt("Mr. Withers")
# print(a)
# b = vc.decrypt(a)
# print(b)

cipher = VCipher()
keyset = cipher.generate_keyset(11)
print(keyset)
enc = cipher.encrypt('Mr. Withers', keyset)

f = open("output.txt", "a")
perms = product([0,1], repeat=11)
for guess_keyset in list(perms):
    f.write(cipher.decrypt(enc, guess_keyset) +"\n")

f.close()


