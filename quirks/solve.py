with open("debug.txt") as file:
    lines = file.readlines()

bits = '0'

for i in range(len(lines)):
    if 'charcount = 0' in lines[i]:
        mode = lines[i-1].strip().split(' ')[3]
        bit = {'2': '0', '4': '1'}[mode]
        bits += bit
    
converted = bytes(int(bits[i : i + 8], 2) for i in range(0, len(bits), 8))
print(converted)
