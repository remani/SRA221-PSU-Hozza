# Simple Hash Cracker

Written by Brant Goings - SRA 221 Spring 2020

#### dictionary.txt
```
password
password1
12345
you'llneverguessme
```

#### hashes.txt
```
5f4dcc3b5aa765d61d8327deb882cf99
5952c9e4cbfffb0d3415310acd703ae6
827ccb0eea8a706c4c34a16891f84e7b
```

#### SimpleCracker.py
Takes the above input and uses a nested for loop to hash the dictionary.txt lines then compare to the hashes.txt lines. If any of them match, it prints to terminal the matching pair(s). The above lines return this output:

```
MD5 hash cracked -- 5f4dcc3b5aa765d61d8327deb882cf99 : password
MD5 hash cracked -- 827ccb0eea8a706c4c34a16891f84e7b : 12345
MD5 hash cracked -- 5952c9e4cbfffb0d3415310acd703ae6 : you'llneverguessme
```

Note: See https://github.com/bgoings1/PassCrack for a more comprehensive version of this.
