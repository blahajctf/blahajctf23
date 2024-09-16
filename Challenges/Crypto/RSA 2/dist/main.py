from Crypto.Util.number import bytes_to_long, getPrime

FLAG = b"blahaj{???}"

p = getPrime(256)
q = getPrime(256)
n = p * q
e = 3

flag_int = bytes_to_long(FLAG)
ciphertext = pow(flag_int, e, n)

print(f"The modulus is: {n}")
print(f"The ciphertext is: {ciphertext}")