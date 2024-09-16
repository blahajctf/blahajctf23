from pwn import *
import time
import random
start_time = int(time.time()*10)
turn = 1
r = remote('167.172.6.174', 31547)
r.recv()
r.recv()
while True:
    random.seed(start_time+turn)
    r.send(str(random.randint(1,9))+"\n")
    line = r.recv()
    if "Oops!" in line.decode():
        start_time += 1
    turn += 1
    print(line, start_time)