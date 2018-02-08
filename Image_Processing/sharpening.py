from PIL import Image

for d in range(0,1):
    img = Image.open('images/jay.jpg')
    img = img.convert('L') # convert to grayscale
    # img.save("images/einstein_gray.jpg")
    # img.show()
    pixdata = img.load()


    fl = [0,-1,0,-1,4,-1,0,-1,0]
    s = 0
    for i in range(len(fl)):
        s = s + fl[i]

    f = [1 for i in range(9)]
    k = 0
    for i in range(img.size[1] - 2):
        for j in range(img.size[0] - 2):
            sum1 = 0
            for m in range(j,j+3):
                for n in range(i,i + 3):
                    sum1 = sum1 + pixdata[m,n]*fl[k]
                    k = k + 1
            k = 0
            pixdata[j+1,i+1] = pixdata[j+1,i+1] + sum1



    final = []
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            # print pixdata[x,y]
            final.append(pixdata[x,y])
    img.putdata(final)
img.save("images/final_sharp.jpg")
img.show()      