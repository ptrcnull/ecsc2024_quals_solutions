from Crypto.Util.number import getPrime

def siz(n):
	return len(bin(n))-2

def main():
    flag = open("flag.txt",'rb').read()
    flag_int = int.from_bytes(flag,byteorder='big')

    bits = 768
    bits_small = bits//8

    p = getPrime(bits)
    s1 = getPrime(bits_small)
    a = p//s1 
    s2 = p%s1

    q = getPrime(bits)
    s3 = getPrime(bits_small)
    b = q//s3
    s4 = q%s3

    N = p*q

    assert N == (a*s1+s2)*(b*s3+s4)
    assert ((N // a) // b) == s1*s3
    # (b * s2 * s3) + (s2 * s4) + (s1 * ((a * b * s3) + (a * s4)))

    c = getPrime(int((bits_small*1.5)))
    s24c = (s2*s4)%c

    # assert ((N - s24c) - ((a * b * s1 * s3) + (a * s1 * s4) + (b * s2 * s3))) % c == 0

    print('a', siz(a))
    print('b', siz(b))
    print('c', siz(c))
    print('s1', siz(s1))
    print('s2', siz(s2))
    print('s3', siz(s3))
    print('s4', siz(s4))
    print('s24c', siz(s24c))
    # print(s2/a)

    e = 65537
    ct = pow(flag_int,e,N)
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
    print(f"(s2*s4)%c={s24c}")
    print(f"ct={ct}")
    print(f"N={N}")
    print(f's2={s2}')
    print(f's4={s4}')
    print({'s1': s1, 's3': s3})

    i = (N - a*b*s1*s3 - s24c)
    j = (a*s1*s4 + b*s3*s2)
    dif = i - j
    print(i)
    print(j)
    print(dif)
    print(dif / c)
    # print('s2-s4', s2-s4)
    # print('s2-s4', len(bin(s2-s4))-2)

    # assert i >> 193 == j >> 193
    # diff = s2 - ((-a * s1 * (b * s3 + s4) - s24c + N) // (b * s3))
    diff = s2+s4
    print('diff', diff, len(bin(diff))-2)

    # print((a*s1*s4 + b*s3*s2))
    # print((N - a*b*s1*s3 - s24c))

    # assert (N - a*b*s1*s3 - s24c) == (a*s1*s4 + b*s3*s2) + n*c

main()
