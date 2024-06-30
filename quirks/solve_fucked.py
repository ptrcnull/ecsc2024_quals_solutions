from PIL import Image
from pyzbar import pyzbar

img = Image.open('quirks.png')
padding = 40
img = img.crop((padding, padding, img.size[0] - padding, img.size[1] - padding))
qr = []
for x in range(0, img.size[0], 10):
    x += 5
    line = []
    for y in range(0, img.size[1], 10):
        y += 5
        pixel = img.getpixel((y, x))
        pixel = {0: '█', 255: ' '}[pixel]
        line.append(pixel)
    qr.append(line)

def print_qr(qr):
    print('\n'.join(map(lambda row: ''.join(row), qr)))

print_qr(qr)

# output = pyzbar.decode(img)
# print(output)
