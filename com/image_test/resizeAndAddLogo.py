import os
from PIL import Image, ImageDraw


SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoImg = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoImg.size

os.makedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue
    img = Image.open(filename)
    width, height = img.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print('Resizing %s...' % filename)
        img = img.resize((width, height))

        print('Adding logo to %s...' % filename)
        img.paste(logoImg, (width - logoWidth, height - logoHeight), logoImg)

        img.save(os.path.join('withLogo', filename))