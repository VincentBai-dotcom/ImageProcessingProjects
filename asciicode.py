from PIL import Image
import numpy as np


def read(path):
    try:
        image = Image.open(path)
        return image
    except Exception as e:
        print(e)


def to_binary2(arr, threshold):
    for i in range(0,len(arr)):
        if arr[i] > threshold:
            arr[i] = 200
        else:
            arr[i] = 30
    return arr

def flatten(image):
    arr = np.array(image)
    return arr.flatten()


def build(arr, d):
    arr2 = []
    i = 0;
    while(i< len(arr)):
        arr2.append(arr[i:i+d])
        i += d
    return Image.fromarray(np.array(arr2))


def to_binary(image, threshold):
    image = image.convert("L")
    array = np.array(image)
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if array[i][j] > threshold:
                array[i][j] = 200
            else:
                array[i][j] = 30
    return Image.fromarray(array)


image = read("../convert_to_ascii/3.jpg")
#here it can be any image.
to_binary(image,150).show()

