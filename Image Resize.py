from PIL import Image

import cv2
import os
width = 480
height = 360
files = glob("/home/..../*.png")
#print files
i= len(files)
print i

for x in range(0, 3):
    fn = files[x]
    img=cv2.imread(fn)
    #fd_img = open(fn, 'r')
    a = os.path.basename(fn)
    print a
    image = cv2.resize(image, (height, width), fx=0, fy=0, interpolation=cv2.INTER_NEAREST)

k.
    image.save('/home/...../'+a)
