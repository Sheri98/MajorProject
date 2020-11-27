#! /usr/bin/env python
import socket
import pyfiglet
from termcolor import colored
import subprocess
import time
import struct
import attack
import fuzzing_new
import create_pattern
import offset
import fuzzing
result = colored(pyfiglet.figlet_format("              SBM TOOL",font="slant"),color="red")
names = colored("By sheri and dippam",color="yellow")
print(result)
print(" "*45 + names)
print("Welcome to Buffer overfloww automator")
print("These are the following options availbale")
value  = int(input('''
            1. Fuzzing
            2. Create pattern
            3. replaced_fuzzing
            4. find offset
            5. exploit
            '''
        ))
if value == 1:
    print("Started Fuzzing:")
    x = fuzzing.fuzzer()
    print("Length of segmentation fault")
    print(x)
elif value == 2:
    print("Creating pattern")
    length = input("Enter length for pattern")
    x = create_pattern.pattern_create(length)
    print("Pattern:")
    print(x)
elif value == 3:
    print("new fuzzing with pattern")
    fuzzing_new.replaced_fuzzing()

elif value ==4:
    x = offset.find_offset()
    print("Offset length:")
    print(x)
elif value == 5:
    attack.exploiting()
    print("Exploiting")
    print("done")
























