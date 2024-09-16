Server allows you to pick your own primes so it's trivial; mainly intended as a test to see if players understand RSA.

Intended solution path:
1. Choose big enough values of p and q (128 bits is fine)
2. Calculate d = pow(3, -1, (p-1)*(q-1))
3. Calculate pow(ciphertext, d, p*q) and convert to bytes for flag

Alternative solution path:
1. Input random big numbers for p and q such that m^3 < p*q
2. Calculate cube root of ciphertext returned and convert to bytes

Flag: `blahaj{wHy_N0t_trY_Crypt0.U1il.numb3r.g3tPr1m3?}`