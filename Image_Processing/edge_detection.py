import os,sys,Image
def mask(pixs,i,j) :
  x,y=0,0
  #x=(-1)*(pixs[i-1,j-1] + pixs[i-1,j+1])+(-2)*pixs[i-1,j] + (pixs[i+1,j-1] + pixs[i+1,j+1])+(2)*pixs[i+1,j]
  #y=(-1)*(pixs[i-1,j-1] + pixs[i+1,j-1])+(-2)*pixs[i,j-1] + (pixs[i-1,j+1] + pixs[i+1,j+1])+(2)*pixs[i,j+1]
  x=(-1 * pixs[i,j]) + pixs[i+1,j+1]
  y=(-1 * pixs[i,j+1]) + pixs[i+1,j]
  return (int)(abs(x) + abs(y))

def main() :

  img=Image.open("../images/jay.jpg").convert('L')
  # pixels=list(img.getdata())
  newimg=Image.new('L',img.size)
  # newimg.paste(img,(0,0))
  pixs=img.load()
  pixels = newimg.load()
  for i in range(1,newimg.size[0]-1) :
    for j in range(1,newimg.size[1]-1) :
      pixels[i,j]=mask(pixs,i,j)
  newimg.show()
  newimg.save("edge_jay.jpg")

if __name__=='__main__' :
  main()