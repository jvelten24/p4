#!/usr/bin/env python3

import sys

#put bin/sh into the buffer then overwrite the return address to the start of ur ropgadget chain
#The ropgadget chains should be a series of gadgets that pop into registers and return
#And call syscall and return


bin_sh = b'/bin/sh\x00'



payload = bin_sh + b'A'*(120 - len(bin_sh))



#set rax to 0x69
#set rdi to 0
#then syscall

#eventually we set rdi to address of /bin/sh (where does that come from?)
#then we set rsi to 0
#then we set rdx to 0
#then syscall? How do we do syscall