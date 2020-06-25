Task---PIXELS----
from PIL import Image

img = Image.new( 'RGB', (200,200), "black")
pixels = img.load()  
mon_fichier = open("pixel.enc","r").read(40000)
key=0
for i in range(200):   
    for j in range(200):
        p = ord(mon_fichier[key])
        p = float(p)/1.158371
        if (p < 100):
                pixels[i,j] = (0,0,0)
        else:
                pixels[i,j] = (255,255,255)     
        key+= 1

img=img.save("QR.png")



