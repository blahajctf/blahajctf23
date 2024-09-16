# Blåfish
> blahaj found a cipher that hasn't been broken! and it's a fish too! 

## Solution
Because every character is converted to hex, before being encoded as UTF-32, each character corresponds to 64 bits i.e. the size of each block in Blowfish. As we are using Blowfish in ECB mode, identical characters will encrypt to the same 8 byte block. Thus, by cutting the ciphertext into chunks of 8 bytes, we obtain a monoalphabetic substituition cipher (this is what `sol.py` does), which can be solved by hand or through use of a tool like quipquip.

Flag: `blahaj{blowfish_more_like_blowhai}`
