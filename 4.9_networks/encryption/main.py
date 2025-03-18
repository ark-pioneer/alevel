class SubCipher():
    def encrypt(self, plaintext, key):
        ciphertext = ""
        for char in plaintext:
            ciphertext += chr(ord(char) + key)
        return ciphertext
    
    def decrypt(self, ciphertext, key):
        plaintext = ""
        for char in ciphertext:
            plaintext += chr(ord(char) - key)
        return plaintext
    

cipher = SubCipher()
res = cipher.encrypt('Mr. Withers', 9)

possible_keys = range(1,11)
for guess_key in possible_keys:
    try: 
        print(guess_key, cipher.decrypt(res, guess_key))
    except Exception as error:
        print(guess_key, error)
