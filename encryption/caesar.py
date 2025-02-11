class SubCipher():
    def encrypt(self, plaintext, key):
        code = ord(plaintext)
        ciphertext = chr(code + 1)
        # find the ascii code for the char
        # add one to it
        # find the character for new ascii code
        return ciphertext
    



    def decrypt(self, ciphertext, key):
        return plaintext
    

cipher = SubCipher()
res = cipher.encrypt('a', 1)
original = cipher.decrypt(res, 1)

print(original == 'a')