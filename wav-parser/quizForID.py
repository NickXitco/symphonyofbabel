import math

from PIL import Image

TARGET_WIDTH = 598
TARGET_HEIGHT = 535

performer = "Ancànta Choir".ljust(100)
songName = "Holy Water".ljust(100)
date = 6744073709551615
trackNumber = 2534

img = Image.open("test_files/vc.jpg")
width, height = img.size

heightRatio = TARGET_HEIGHT / height
img = img.resize((math.ceil(width * heightRatio), math.ceil(height * heightRatio)))
width, height = img.size

if width < TARGET_WIDTH:
    widthRatio = TARGET_WIDTH / width
    img = img.resize((math.ceil(width * widthRatio), math.ceil(height * widthRatio)))
    width, height = img.size

widthDif = (width - TARGET_WIDTH) / 2
heightDif = (height - TARGET_HEIGHT) / 2
img = img.crop((math.floor(widthDif),
                math.floor(heightDif),
                math.ceil(width - widthDif),
                math.ceil(height - heightDif))
               )
width, height = img.size

performerBits = ''.join([format(x, "08b") for x in bytearray(performer, 'cp437')])
songNameBits = ''.join([format(x, "08b") for x in bytearray(songName, 'cp437')])
dateBits = format(date, "064b")
trackNumberBits = format(trackNumber, "016b")
pixels = list(img.getdata())
imageBits = ''.join([format(y, "08b") for x in pixels for y in x])

print(f"{len(performerBits)} bits: {performerBits}")
print(f"{len(songNameBits)} bits: {songNameBits}")
print(f"{len(dateBits)} bits: {dateBits}")
print(f"{len(trackNumberBits)} bits: {trackNumberBits}")
print(f"{len(imageBits)} bits: {imageBits}")

print(f"{len(performerBits) + len(songNameBits) + len(dateBits) + len(trackNumberBits) + len(imageBits)} total bits")



