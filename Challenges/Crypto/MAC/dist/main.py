import random
from Crypto.Util.number import bytes_to_long as b2l

FLAG = "blahaj{???}"

def MAC(message, key):
    key += 1<<32
    assert key.bit_length() == 33, key

    m = b2l(message.encode())
    l = m.bit_length()
    m <<= 32

    for i in range(l-1, -1, -1):
        if (m >> (i+32)) & 1:
            m ^= key << i
    
    return hex(m)[2:]

while True:
    print("Options:")
    print("[1] Test MAC")
    print("[2] Verify MAC")
    print("[3] Get flag")
    i = int(input(">> "))
    if i == 1:
        message = input("Message: ")
        key = random.getrandbits(32)
        print(f"Your MAC is {MAC(message, key)} with key {hex(key)[2:]}")
    elif i == 2:
        message = input("Message: ")
        key = int(input("Key: "), 16)
        mac = input("MAC: ")
        print(MAC(message, key))
        if MAC(message, key) == mac:
            print("Verified!")
        else:
            print("Not verified!")
    elif i == 3:
        key = random.getrandbits(32)
        print(f"MAC of flag is {MAC(FLAG, key)}")