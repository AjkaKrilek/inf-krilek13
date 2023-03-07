from PIL import Image
pic = Image.new('RGB',(250,250),'white')
pixels = pic.load()

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
d = int(input('d='))

e = c-a
f = d-b
k = f/e
q = b-k*a

if e>f:
    y = int(k*e+q)
    x = e
    pixels[x,y]=(0,0,0)
if e<f:
    y = f
    x = int((f - q) / k)
    pixels[x,y]=(0,0,0)
if e==f:
    x = a
    y = c
    pixels[x,y]=(0,0,0)
pic.show()