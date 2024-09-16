# Site Scavenger
> After making a website on my favourite stuffed toy, the Blahaj, I made a flag and hid it somewhere on the website. But now I cannot find it! Please help me get my flag again 😢

## Solution
This flag is split into 3 parts.
1. about.html
For about.html, inspect element and scroll all the way to the bottom. The following comment will appear.

```html
<!-- Oops, this is where I left the first part of the flag. -->
<!-- blahaj{i_l0v3_b14 -->
<!-- If only I knew where to find the other parts of the flag... -->
```

2. robots.txt
The next logical site to check is this. And we get the second part of the flag

```txt
Oops, this is where I left the second part of the flag.
haj_and_y0u_shou
If only I knew where to find the other parts of the flag...
```

3. sitemap.xml

Lastly, we check the final commonly hidden website files, sitemap.xml <br>
This shows us there is a super secret route `/sup3r-s3cr3t` 🤔🤔 <br>
Going there we see that `GET` functionality does not work, and on inspect element, tells to go to `POST`. <br>
We then answer the question `What is your fav_plush?`, which we reply by adding a form element `fav_plush=Blahaj` (read the question for why this is correct). <br>
Finally, we get the last part of the flag.

```
Welcome back, here is the 3rd part of the flag.
1d_70o_^_^}
Did you remember to collect the other 2 on the way?
```

And piecing them together
Flag: `blahaj{i_l0v3_b14haj_and_y0u_shou1d_70o_^_^}`