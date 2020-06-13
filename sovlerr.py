from PIL import Image
from typing import List, Tuple
import random
from struct import pack, unpack
image = Image.open("out.png")
image = image.convert("RGB")
pixels = image.load()
def getByte(locations: List[Tuple[int, int, int]]):
    ans = ""
    for location in locations:
        x, y, channel = location
        val = pixels[x, y][channel]
        val &= 0b00000001
        ans+=str(val)
    return bytes([int(ans,2)])
valid_spots = []
for channel in range(3):
    for y in range(image.height):
        for x in range(image.width):
            valid_spots.append((x, y, channel))
meta= 60
msg = b""
c=0
for i in range(meta):
    msg += getByte(valid_spots[c:c+8])
    c+=8
seed = msg[-8:-4]
size = unpack("<I", msg[-4:])[0]
random.seed(bytes(seed))
locations = random.sample(valid_spots[c:], size * 8 + 1)
c=0
flag = b""
for i in range(size):
    flag += getByte(locations[c:c + 8])
    c += 8
print(flag)

