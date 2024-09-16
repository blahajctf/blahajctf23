# Looking for Blahaj
> I am playing hide and seek with my Blahaj. I was told it was hiding somewhere in this image, but where?

## Solution
When you get an image, it is always good to throw it into [aperisolve](https://www.aperisolve.com/). <br>
On there, we see some sus stuff under binwalk, showing there is more to this file. <br>
Extracting, we get a zip file containing `message.txt` and `Totally_not_here.jpg`. <br>
Translating `message.txt` from Swedish to English, we see the password is `blahajery`, and that password is used to store something in Totally_not_here.jpg. <br>
Using steghide, we can extract out a `blahaj.txt` file with that password and boom, the flag.

Flag: `blahaj{n0_M0r3_h1d1n6_F0r_bl4h4j}`