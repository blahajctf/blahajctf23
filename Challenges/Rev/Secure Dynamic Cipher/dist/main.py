import random


def caesar_cipher(plaintext, shift):
    ciphertext = plaintext + '‍' + "".join(random.choices(list('abcdefghijklmnopqrstuvwxyz1234567890'), k=(128-len(plaintext)))) # haha no length based attack now!
    cipher_res = ""
    for i, c in enumerate(ciphertext):
        if c.isalpha():
            shift_val = shift + i  # cant guess the key if you change the key every time!
            if c.isupper(): cipher_res += chr((ord(c) + shift_val - 65) % 26 + 65)
            else: cipher_res += chr((ord(c) + shift_val - 97) % 26 + 97)
        else: cipher_res += c
    ciphertext = list(cipher_res)
    for i in range(len(ciphertext)):
        j = (i*i + shift) % len(ciphertext)
        ciphertext[i], ciphertext[j] = ciphertext[j], ciphertext[i]
    ciphertext = "".join(ciphertext)

    return ciphertext


plaintext = "blahaj{???}"
print(caesar_cipher(plaintext, random.randint(1, 26)))
# prints m_3irb5714335hot_muqlp17oc6l360y63zz81rwe0no_5t_m8‍ejm5wgm44}gzxyv26k17364q26vczy17t7p{5dj7918372_1v0ng0146lezqnfvg1libnnula_glhq
