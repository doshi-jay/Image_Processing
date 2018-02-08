from PIL import Image
import matplotlib.pyplot as plt


img = Image.open('../images/jay.jpg').convert('L')
img.show()#save('images/gray_wallpaper.jpg')
pixdata = img.load()
histo = img.histogram()
l=[i for i in range(0,256)]

histo1 = []
histo1 = img.histogram()   


def sum_of_list(histo):
    sum1 = histo[0]
    for i in range(1,256):
        sum1 = sum1 + histo[i]
        histo[i] = histo[i] + histo[i-1]
    pdf(histo,sum1)

def pdf(histo,sum1):
    cdf = []
    for i in range(0,256):
        div = float(histo[i])/float(sum1)
        print div
        cdf.append(int(div*255))
    final = []
    for i in range(256):
        final.append(0)
   
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            pixdata[x,y] = cdf[pixdata[x,y]]

    final = []
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            final.append(pixdata[x,y])
    img.putdata(final)
    img.show()       

    plt.figure(0)
    plt.bar(range(len(histo1)),histo1, align='center')
    plt.ylabel('Pixel Frequency')
    plt.xlabel('Pixel')
    plt.figure(1)
    plt.bar(range(len(img.histogram())),img.histogram(), align='center')
    plt.ylabel('Pixel Frequency')
    plt.xlabel('Pixel')
    plt.show()
    to_save = "screenshots/histogram.jpg"
    img.save(to_save)

sum_of_list(histo)