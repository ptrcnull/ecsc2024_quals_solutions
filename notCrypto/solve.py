from pwn import *

# s = remote('notcrypto.ecsc24.hack.cert.pl', 5103)
s = process(['java', 'ecsc24.Main'])
s.sendline('ąąąąąąąąąąąą')
secret = s.recvline().decode().strip()
print(secret)
