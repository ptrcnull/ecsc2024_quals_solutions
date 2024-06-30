import string
import binascii

printable = string.digits + string.ascii_letters + string.punctuation + ' '

def dump(mem, offset, r=0x30):
    offset = (offset // 16) * 16
    start = offset - r
    end = offset + r
    section = mem[start:end]
    for x in range(len(section) // 48):
        off = x * 48
        line_bytes = section[off:off+48]
        line = ''
        line += hex(start + off)[2:].zfill(8)
        line += ': '
        line += binascii.hexlify(line_bytes, ' ', 2).decode()
        line += '  '
        line += ''.join([ chr(c) if chr(c) in printable else '.' for c in line_bytes ])
        print(line)
