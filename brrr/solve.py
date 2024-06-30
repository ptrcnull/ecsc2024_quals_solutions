import functools
from math import sqrt, ceil
from sympy import isprime
 
flag_enc = b"nhx\x08\xb0wE\x00o\x89\x8b\x04\xbc\xe8\xc2\x99;\xdc\x0bCO!rV\xc8\xdd\xe3\xe8F\xed\x94\xd7o\x05\x01\xf4\xbf"

trifact_numbers = [1, 1, 1]

# @functools.cache
def tri_fact_linear(n):
    start = min(n, len(trifact_numbers) - 1)
    while True:
        if start == n:
            return trifact_numbers[n]
        else:
            next_trif = trifact_numbers[-3] + trifact_numbers[-2] + trifact_numbers[-1]
            next_trif &= 0xffffffffffffffff
            trifact_numbers.append(next_trif)
            start += 1

@functools.cache
def tri_fact(n):
    if n > 2:
        return tri_fact(n - 3) + tri_fact(n - 2) + tri_fact(n - 1)
    return 1

found_trifactorials = {0: 0}

@functools.cache
def get_tri_fact_prime(n):
    if n < list(found_trifactorials.keys())[-1]:
        return list(found_trifactorials.values())[-1]

    i = n
    while True:
        fact = tri_fact_linear(i) & 0xffffffffffffffff
        if isprime(fact) != 0:
            break
        i += 1
    found_trifactorials[i] = fact
    # print('found for n =',i)
    return fact

@functools.cache
def shifty_with_discard(num):
    # print('shifty for', num)
    lfsr_bit = (num ^ (num >> 2) ^ (num >> 3) ^ (num >> 4)) & 1
    return ((num >> 1) | (lfsr_bit << 7)) & 0xff

@functools.cache
def shfity_12(num):
    for x in range(12):
        num = shifty_with_discard(num)
    return num

def get_key_byte(n):
    # print('n', n)
    trif = get_tri_fact_prime(n)
    # print('trif', trif)
    var_1a = (trif & 0xffff) ^ 0xffff
    var_1a >>= 8

    # print('var1a befor shifty 0', bin(var_1a).zfill(10))

    result = 0
    for i in range(8):
        # for j in range(0xba04014 // 12):
        #     var_1a = shfity_12nd(var_1a)
        # for j in range(0xba04015):
        var_1a = shifty_with_discard(var_1a)
        # print('var1a after shifty', i, bin(var_1a).zfill(10))
        result = (result << 1) + (var_1a >> 7)
        # print(bin(result))
    return result

flag = b''

for i in range(37):
    key_byte = get_key_byte(i * i * i)
    flag += chr(flag_enc[i] ^ (key_byte & 0xff)).encode()

print(flag.decode())
