from PIL import Image

for d in range(0,1):
    img = Image.open('../images/jay.jpg')
    img = img.convert('L') # convert to grayscale
    img.save("final_sharp.jpeg")

    pixdata = img.load()

    fl = [1,1,1,1,1,1,1,1,1]
    # fl = [-1,-1,-1,-1,8,-1,-1,-1,-1]
    s = 0
    for i in range(len(fl)):
        s = s + fl[i]

    f = [1 for i in range(9)]
    k = 0
    for i in range(img.size[1] - 2):
        for j in range(img.size[0] - 2):
            sum1 = 0
            for m in range(i,i+3):
                for n in range(j,j + 3):
                    sum1 = sum1 + pixdata[n,m]*f[k]
                    k = k + 1
            k = 0
            pixdata[j+1,i+1] = sum1 / 9
            # if s != 0:
            #     pixdata[j+1,i+1] = sum1 / s
            # else:
            #     pixdata[j+1,i+1] = sum1


    final = []
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            # print pixdata[x,y]
            final.append(pixdata[x,y])
    img.putdata(final)
img.save("screenshots/smoothing.jpeg")
img.show()        