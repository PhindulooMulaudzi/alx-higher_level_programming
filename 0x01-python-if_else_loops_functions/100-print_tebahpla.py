#!/usr/bin/python3
# Author - Phindulo Mulaudzi

offset = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - offset)), end="")
    offset = 32 if offset == 0 else 0
