#!/usr/local/bin/python

from Crypto.Util.number import bytes_to_long, getRandomNBitInteger

FLAG = b"blahaj{Th15_1s_wHY_W3_u53_X0R}"

flag_int = bytes_to_long(FLAG)
flag_length = flag_int.bit_length()

otp = getRandomNBitInteger(flag_length)

encrypted_flag = flag_int & otp

print(f"Here's the encrypted flag: {encrypted_flag}")