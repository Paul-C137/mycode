#!/usr/bin/env python3
from subprocess import call
call(["ip", "link", "show"])
print("This program will check your interfaces.")
interface = input("Enter an interface, like, en0: ")
call(["ip", "addr", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])