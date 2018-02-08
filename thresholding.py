from PIL import Image


for i in range(2,11):
    to_open = "images/jay.jpg"
    img = Image.open(to_open)
    img = img.convert("RGBA")
   
    pixdata = img.load()

    print "Image Size: " + str(img.size)
    print "Image Size 1: " + str(img.size[1])
    print "Image Size 0: " + str(img.size[0])

    # print "Pix Data: " + str(pixdata[220,70])

    for y in xrange(img.size[1]):
     for x in xrange(img.size[0]):
         if pixdata[x, y][0] < 136:
             pixdata[x, y] = (0, 0, 0, 255)
   
    for y in xrange(img.size[1]):
     for x in xrange(img.size[0]):
         if pixdata[x, y][1] < 90:
             pixdata[x, y] = (0, 0, 0, 255)

    for y in xrange(img.size[1]):
     for x in xrange(img.size[0]):
         if pixdata[x, y][2] < 85:
             pixdata[x, y] = (0, 0, 0, 255)
   
    for y in xrange(img.size[1]):
     for x in xrange(img.size[0]):
         if pixdata[x, y][2] > 1:
             pixdata[x, y] = (255, 255, 255, 255)
   
    to_save = "screenshots/thresholding.jpeg"
    img.save(to_save)