from PIL import Image
import matplotlib.pyplot as plt


img = Image.open('../images/jay.jpg').convert('L')
pixdata = img.load()
for y in xrange(img.size[1]):
	for x in xrange(img.size[0]):
		pixdata[x,y] = 256 - pixdata[x,y] - 1


img.show()
# img.save("screenshots/negative.jpeg")