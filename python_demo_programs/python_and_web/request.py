from io import BytesIO
import requests
from PIL import Image, ImageFilter

response = requests.get('https://dog.ceo/api/breeds/image/random')

json_data = response.json()
print(json_data)

response = requests.get(json_data['message'])
# print(response.content)
f = BytesIO(response.content)
im = Image.open(f)
im.show()

# save the image as out_file
im.save('out.jpg')
print(im.format)
print(im.size)

# crop the image with range
# box = (100, 100, 200, 200)
# region = im.crop(box)
# region.show()

# im = im.rotate(90)
# im.show()
# im = im.filter(ImageFilter.BLUR)
# im.show()

'''
modify the image
an image is made of pixels, a pixel is a tuple of numbers in range(256)
(0, 176, 80)
red = 0
green = 176
blue = 80

for each value, [0, 255]

if we want to process the image, we can convert the image to 3d array of number
why 3d
width, height, pixel(rgb channels)
'''
import numpy as np


im_3d = np.asarray(im)
print(im_3d.shape)  # (width, height, number_channels)