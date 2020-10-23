from math import *
from PIL import Image
import numpy as np

def read(path):
    try:
        image = Image.open(path)
        return image
    except Exception as e:
        print(e)

def get_average_brightness(image):
    image_array = np.array(image)
    w, h = image_array.shape
    return floor(np.average(image_array.reshape(w*h)))

def start(skip, image):
    ascii_chart = '@%#*+=-:. '
    result = []
    i = 0;
    w, h = image.size
    while i < h:
        y1 = i
        y2 = i + skip*5
        if y2 > h:
            y2 = h
        j = 0
        currentstr = ""


        while j < w:
            x1 = j
            x2 = j + skip*2
            if x2 > w:
                x2 = w
            cropped_image = image.crop((x1,y1,x2,y2))
            avergae_brightness = get_average_brightness(cropped_image)
            currentstr += ascii_chart[int((avergae_brightness*9)/255)]
            j += skip*2


        result.append(currentstr)
        i += skip*5
    f = open("outFile", 'w')
    for row in result:
        f.write(row + '\n')
    f.close()


image = read("8f58e30690f7cc68e2b3731e7927e93.jpg")
image = image.convert("L")
start(3, image)



