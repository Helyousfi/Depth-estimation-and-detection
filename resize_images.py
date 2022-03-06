#!/usr/bin/python
from PIL import Image
import os, sys

path = "C:/Users/hamza/Desktop/depth dataset/images/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        #print("hello")
        #if os.path.isfile(path+item):
        print("hello")
        im = Image.open(path+item)
        f, e = os.path.splitext(path+item)
        imResize = im.resize((448,448), Image.ANTIALIAS)
        imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()