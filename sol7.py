#!/usr/bin/env python3

import sys


#rop chain = pop_rax + setuid syscall number + syscall + pop_rax + execve syscall number + pop_rdi + bin_sh + pop_rsi_r15 + dump + syscall