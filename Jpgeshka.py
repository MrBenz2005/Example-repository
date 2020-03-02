from PIL import Image
from PIL import ImageDraw
import sys
import numpy
import math
import numpy as np
im = Image.open('C:\\Users\Kostya\Pictures\kot.jpg')
tver = im.copy()
kote = im.crop((335, 345, 825, 660))
kote = kote.copy()
draw = ImageDraw.Draw(im)
width = im.size[0]
height = im.size[1]
pix = im.load()
for x in range(width):
   for y in range(height):
      r = pix[x, y][0]
      g = pix[x, y][1]
      b = pix[x, y][2]
      sr = (r + g + b) // 3
      draw.point((x, y), (255 - r, 255 - g, 255 - b))

kotek = im.crop((335, 345, 825, 660))
kotekcat = kotek.copy()
kotekcat1 = kotekcat.rotate(270)
kotekcat = kotekcat.rotate(90)

tver.paste(kotek,(0,0))
tver.paste(kotek,(460,0))
tver.paste(kotek,(920,0))
tver.paste(kotek,(1380,0))
tver.paste(kotek,(0,980))
tver.paste(kotek,(460,980))
tver.paste(kotek,(920,980))
tver.paste(kotek,(1380,980))
tver.paste(kotekcat, (0,315))
tver.paste(kotekcat, (0,630))
tver.paste(kotekcat1, (1425,315))
tver.paste(kotekcat1, (1425,630))
tver.save("resulting.png")
