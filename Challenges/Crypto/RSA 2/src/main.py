#!/usr/local/bin/python

from Crypto.Util.number import bytes_to_long, getPrime

FLAG = b"blahaj{tH3_f1r5t_A_1n_h4st4d_15_th3_s4m3_4s_th3_f1r5t_A_1n_bl4h4j}"

p = getPrime(256)
q = getPrime(256)
n = p * q
e = 3

flag_int = bytes_to_long(FLAG)
ciphertext = pow(flag_int, e, n)

print(f"The modulus is: {n}")
print(f"The ciphertext is: {ciphertext}")