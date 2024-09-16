import hashlib
import random
import string

for i in range(10000):
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
    hash = hashlib.sha1(random_string.encode('utf-8')).hexdigest()
    # print the hash
    if hash.startswith('42') and hash[2] not in '0123456789':
        print(random_string)

# outputs: can use any of these for meaning of life
'''
sFfpR
REPAb
bwGE0
qzGp0
xT91y
BhTRg
pTSjA
GqmIe
72tm9
E1VGD
Odowg
U8jyj
M5ODb
Q0z3U
YbcM0
48I7K
zqOxi
mhW7H
fYHxh
'''