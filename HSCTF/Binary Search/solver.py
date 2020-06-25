from PIL import Image

i = Image.open("BinaryWordSearch.png")

# d = i.getdata()
#
# print(d[1])
#
# data = ["0" if p[0] == 255 else "1" for p in d]
#
# binary = ''.join(data)


target = ''.join(["{:08b}".format(c) for c in b"flag{"])
print(target)


targetpixel = [(255,255,255) if c == "1" else (0,0,0) for c in target]
print(targetpixel)

def searchFrom(origx,origy,dx,dy):
    x = origx
    y = origy
    for cnt, pix in enumerate(targetpixel):
        if i.getpixel((x,y)) != pix:
            print(f"Failed after {cnt} chr at {x} {y}")
            return False
        x += dx
        y += dy

    print("Found it starting at ", origx, origy, dx,dy)
    return True

def findStart():
    for x in range(i.size[0]):
        for y in range(i.size[1]):
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    try:
                        if searchFrom(x,y,dx,dy):
                            return (x,y,dx,dy)
                    except IndexError:
                        pass

x,y,dx,dy = 193, 837, 1, -1

flag = ""
b = ""
while not flag.endswith("}"):
    if i.getpixel((x,y))[0] == 0:
        b += "0"
    else:
        b += "1"
    x += dx
    y += dy

    if len(b) == 8:
        flag += chr(int(b,2))
        print("Flag", flag)
        b = ""
