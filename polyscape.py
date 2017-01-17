from skimage import io, transform
IMAGE = io.imread('images/mountains.jpg')
IMAGE2 = io.imread('images/forrest.jpg')
IMAGE3 = io.imread('images/sunrise.jpg')
MASK = io.imread('masks/circlesquare.png')

height = IMAGE.shape[0]
width = IMAGE.shape[1]

FLIPPED_IMAGE = transform.rotate(IMAGE,180,preserve_range=True)

for x in range  (0,height):
    for y in range (0,width):
        t = MASK[x,y]
        if t[0] == 255 and t[1] != 255:
            IMAGE[x,y] = IMAGE3[x,y]
        elif t[1] == 255 and t[0] != 255:
            IMAGE[x,y] = IMAGE2[x,y]
        elif t[2] == 255 and t[0] != 255:
            IMAGE[x,y] = FLIPPED_IMAGE[x,y]


io.imshow(IMAGE)
io.show()