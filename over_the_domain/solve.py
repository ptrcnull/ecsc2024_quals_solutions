import base64
from scapy.all import *
import zipfile

data = ''

scapy_cap = rdpcap('over-the-domain.pcap')
for packet in scapy_cap:
    domain = str(packet[DNS]).split("'")[1]
    if domain.count('.') == 4:
        parts = domain.split('.')
        if parts[1] != 'X':
            continue
        decoded = base64.b64decode(parts[0])
        data += parts[0]

content = base64.b64decode(data.encode('utf-8'))
zip_buffer = io.BytesIO(content)

with zipfile.ZipFile(zip_buffer) as zip_file:
    with zip_file.open('flag.txt') as file:
        print(file.read().decode())

# os.unlink('file.raw')
# with open('file.raw', 'wb') as file:
#     file.write(base64.b64decode(data.encode('utf-8')))
