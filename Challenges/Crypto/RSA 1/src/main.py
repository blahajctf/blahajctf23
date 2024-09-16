#!/usr/local/bin/python

FLAG = b"blahaj{wHy_N0t_trY_Crypt0.U1il.numb3r.g3tPr1m3?}"

# c = m^e mod n, whatever that means

# Apparently this is a commonly used value for e...
e = 65537

# But I don't know what values of p and q to use!
p = int(input("Can you give me a value for p?\n"))
q = int(input("q too, please\n"))

# ChatGPT is so helpful
from Crypto.Util.number import bytes_to_long

n = p * q
flag_int = bytes_to_long(FLAG)
ciphertext = pow(flag_int, e, n)

print(f"The modulus is: {n}")
print(f"The ciphertext is: {ciphertext}")
print("Thanks for your help!")