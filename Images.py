Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from PIL import Image


def wb_negative(name):
    im = Image.open(name)
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            bw = 255 - (r + g + b) // 3
            pixels[i, j] = bw, bw, bw
    im.save("out.png")
-------------------------------------
from PIL import Image, ImageOps


def frame(name, f):
    im = Image.open(name)
    x, y = im.size
    im2 = im.crop((x // 3, y // 3, x - x // 3, y - y // 3))
    ra, ga, ba = 0, 0, 0
    pixels = im2.load()
    x2, y2 = im2.size
    p = 0
    for i in range(x2):
        for j in range(y2):
            p += 1
            r, g, b = pixels[i, j]
            ra += r
            ga += g
            ba += b
    ra //= p
    ga //= p
    ba //= p
    im2 = ImageOps.expand(im2, border=f, fill=(ra, ga, ba))
    im2.save("done.png")
--------------------------------------
from PIL import Image


def reflect(name, n=1):
    im = Image.open(name)
    im2 = ''
    if n == 1:
        im2 = im.transpose(Image.FLIP_TOP_BOTTOM)
    elif n == 2:
        im2 = im.transpose(Image.FLIP_LEFT_RIGHT)
    elif n == 3:
        im2 = im.transpose(Image.ROTATE_180)
    im2.save("result.png")
--------------------------------------
from PIL import Image


def less_variety(name, name2):
    im = Image.open(name)
    pixels = im.load()
    x, y = im.size
    a = list()
    for i in range(x):
        a.extend([pixels[i, j] for j in range(y)])
    c = len(set(a))
    for i in range(1000):
        if c // (2 ** i) <= 256:
            c //= (2 ** i)
            break
    im2 = im.resize((x // 2, y // 2))
    im2 = im2.quantize(c)
    im2.save(name2)
----------------------------------------
from PIL import Image


def snow_forest(an, p):
    im = Image.open("forest.png")
    im2 = Image.open("snow.png").resize((100, 100))
    pixels = im.load()
    pixels2 = im2.load()
    x2, y2 = im2.size
    p, p2 = p / 100, (100 - p) / 100
    for i in range(x2):
        for j in range(y2):
            r, g, b = pixels[i + an[0], j + an[1]]
            r2, g2, b2 = pixels2[i, j]
            pixels[i + an[0], j + an[1]] = int(r * p2 + r2 * p), int(g * p2 + g2 * p), int(b * p2 + b2 * p)
    im.save("output.png")