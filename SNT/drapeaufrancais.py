from PIL import Image

image = Image.new("RGB", (300,300))

for x in range(0,100):
  for y in range(0,300):
    image.putpixel((x,y), (0,0,255))

for x in range(100,200):
  for y in range(0,300):
    image.putpixel((x,y), (255,255,255))

for x in range(200,300):
  for y in range(0,300):
    image.putpixel((x,y), (255,0,0))

image.save("drapeaufrancais.png")
