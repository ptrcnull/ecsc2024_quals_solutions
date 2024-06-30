from PIL import Image, ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True
import io
import mmap
import traceback
import re

def search(mem, needle):
    off = 0
    while True:
        off = mem.find(needle, off)
        if off == -1:
            break
        yield off
        off += 1

i = 0

# header = bytes.fromhex('ffd8ffe0')
# header = bytes.fromhex('ffd8ffe1')
# footer = bytes.fromhex('ffd9')

header = bytes.fromhex('89504e47')
footer = bytes.fromhex('49454e44ae426082')

with open('zettabyte.raw', 'rb') as f:
    mem = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    for match in re.finditer(rb'RIFF....WEBP', mem):
        start = match.start()
        file_size = int.from_bytes(mem[start+4:start+8], 'little')
        with open(f'dump4/{hex(start)}.webp', 'wb') as file:
            file.write(mem[start:start+file_size+12])

    # offset = 0
    # while True:
    #     start = mem.find(header, offset)
    #     if start == -1:
    #         break

    #     end = start
    #     for i in range(10):
    #         end = mem.find(footer, end+1)
    #         if (end - start) > 10_000_000:
    #             break
    #         if end == -1:
    #             print('huh?')
    #             exit()
    #         # try:
    #         #     image = Image.open(io.BytesIO(mem[start:end+500]))
    #         #     print(start, 'found image')
    #         #     break
    #         # except Exception as ex:
    #         #     print(start, 'failed to read:', ex)
    #             # print(traceback.format_exc())
    #         try:
    #             image = Image.open(io.BytesIO(mem[start:end+len(footer)]))
    #             if image.size[0] < 100 and image.size[1] < 100:
    #                 break
    #             image.save(f'dump3/{hex(start)}-n.png')
    #             with open(f'dump3/{hex(start)}-{i}.png', 'wb') as file:
    #                 file.write(mem[start:end+len(footer)])
    #             break
    #         except Exception as ex:
    #             print(hex(start), 'failed to open', ex, f'(try {i})')
    #             continue

    #     offset = start + 1
    # for match in search(mem, bytes.fromhex('ffd8ffe000104a4649460001')):
    #     print(match)
        # x = next(search(mem[match:], bytes.fromhex('ffd9')))
        # print(match, x)
        # with open('dump/' + str(i) + '.jpg', 'wb') as file:

    # for match in search(mem, b'\x89PNG'):
    #     print(match)
