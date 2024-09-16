[Håstad's broadcast attack](https://en.wikipedia.org/wiki/Coppersmith%27s_attack#H%C3%A5stad's_broadcast_attack): multiple (ciphertext, modulus) pairs can be obtained by connecting to server multiple times, and CRT can be used to retrieve flag^3, which then can be cubed rooted.

Intended solution path:
1. Connect to server multiple times, getting many pairs of ciphertext and modulus (4 is enough)
2. Use CRT to find value of real value of flag^3 (check Wikipedia page for more details)
3. Take cube root and convert to bytes for flag

Flag: `blahaj{tH3_f1r5t_A_1n_h4st4d_15_th3_s4m3_4s_th3_f1r5t_A_1n_bl4h4j}`