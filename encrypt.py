



# Encrypt function that takes in plain text phrase and a numeric shift

def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext


# Reverse the encrypt by taking the cipher text and using the opposite shift
def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)



# Crack the cipher by checking all shifts and using my decrypt
def crack(ciphertext):
    for shift in range(26):
        decrypt_text = decrypt(ciphertext, shift)
        print(f'Shift: {shift}, Decrypted text: {decrypt_text}')