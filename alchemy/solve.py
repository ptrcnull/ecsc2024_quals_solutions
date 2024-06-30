from pwn import *
import subprocess
import hashlib
import string

s = remote('confidential.ecsc24.hack.cert.pl', 5100)
ciphertext = bytes.fromhex(s.readline().decode().strip())
# print(ciphertext)
# ciphertext = b'\xf1\x13#\xf6\x0f\x91N3\xc2\x91\xd0\xf6\xf1\xa1\x05u\x05\x11|\x03%-\x07\x00QM]\n);\x07%oeS]Me\x7f\x0eH`EU\\\x16MtY\\wu\x08Wup\x02}\x17]R\x02z~Z\x0f\x7f$\x17Atu\x03`t\x16e\x7fQRz_C{0zf\x072._WRuh{}\x03\x026WzuMr7|^2d0c46790519fc0696f3b643cf3ec90616'
# ciphertext = bytes.fromhex('92b58cbf2a991ec86c9dc6735abf7e40466b06052d471202545e0c0b0c0c4e02565f3f6f782d75547b050b57665f7a6e1b514e515b75100a032b17595f7709317105536449732d414e0727066b6365296c0b687e3172231675045733504f6c0a0707612d4d606d464136150d64353837346664356562343564363039343238363131626139343931613339633935')
known_plaintext = b'U2FsdGVkX1'
known_secret = xor(ciphertext[:len(known_plaintext)], known_plaintext)
print('known_secret', known_secret.hex())
# secret = bytes.fromhex('c787 cacc 4ede 48a3 34ac ed39 3bd0')
# print(secret)
# hashed_secret = hashlib.sha512(secret).hexdigest().encode()
# print('hashed secret', ciphertext.endswith(hashed_secret[-16:]))

possibilities = []

for i in range(4):
    chars = []
    for j in range(256):
        cipher_char = chr(ciphertext[len(known_secret)+i] ^ j)
        if cipher_char in (string.ascii_letters + string.digits + '+/='):
            # print('cipher_char', cipher_char.encode(), j.to_bytes(1))
            chars.append(j.to_bytes(1))
    possibilities.append(sorted(chars))

# print(possibilities)
# exit()
def find_secret():
    for a in possibilities[0]:
        # print('a', a)
        for b in possibilities[1]:
            for c in possibilities[2]:
                for d in possibilities[3]:
                    try_secret = known_secret + a + b + c + d
                    hashed = hashlib.sha512(try_secret).hexdigest().encode()
                    if ciphertext.endswith(hashed[-16:]):
                        return try_secret

secret = find_secret()
# secret = b'\xa4!e\x85k\xd6\x18X\x9a\xa0\xe8\x9d\x85\xf8'
print('secret', secret.hex())
hashed_secret = hashlib.sha512(secret).hexdigest().encode()
with open('secret.bin', 'wb') as file:
    file.write(secret)
plain_aes = xor(secret + hashed_secret, ciphertext).strip(b'\x00')
subprocess.run(
    ['openssl', 'enc', '-d', '-aes-256-cbc', '-pbkdf2', '-iter', '1000001', '-salt', '-a', '-A', '-kfile', './secret.bin'],
    input=plain_aes
)
