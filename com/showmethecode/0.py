from PIL import Image, ImageFont, ImageDraw
import os

image = Image.open('0.jpg')
w, h = image.size
fontsFolder = '/Library/Fonts'
font = ImageFont.truetype(os.path.join(fontsFolder, 'Arial.ttf'), 32)
# font = ImageFont.truetype(size=50)
draw = ImageDraw.Draw(image)
draw.text((4*w/5, h/5), '5', fill=(255, 10, 10), font=font)
image.save('0.0.jpg')
