from PIL import ImageColor, Image, ImageDraw, ImageFont
import os

catImg = Image.open('zophie.png')
print(type(catImg))
# print(catImg.info)
# print(catImg.size)
width, height = catImg.size
print('width:%s height:%s' % (width, height))
print('filename: %s' % catImg.filename)
print('format: %s' % catImg.format)

img = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(catImg)

# draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
# draw.rectangle((20, 30, 60, 60), fill='blue')
# draw.ellipse((120, 30, 160, 60), fill='red')
# draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
# for i in range(100, 200, 10):
#     draw.line([(i, 0), (200, i-100)], fill='green')
#
# img.save('drawing.png')

draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = '/Library/Fonts'
arialFOnt = ImageFont.truetype(os.path.join(fontsFolder, 'Arial.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFOnt)
catImg.save('text_cat.png')