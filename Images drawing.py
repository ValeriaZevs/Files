Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from PIL import Image, ImageDraw


def stripes(n, w, direction="v"):
    im = Image.new("RGB", w)
    im2 = ImageDraw.Draw(im)
    if direction == "v":
        wid = w[0] // n
        x, y, x2, y2 = 0, 0, wid, w[1]
        for i in range(0, n):
            im2.rectangle((x, y, x2, y2), fill=(0, 0, 0), width=wid)
            x += wid
            x2 += wid
            im2.rectangle((x, y, x2, y2), fill=(255, 255, 255), width=wid)
            x += wid
            x2 += wid
    else:
        wid = w[1] // n
        x, y, x2, y2 = 0, 0, w[0], wid
        for i in range(0, n):
            im2.rectangle((x, y, x2, y2), fill=(0, 0, 0), width=wid)
            y += wid
            y2 += wid
            im2.rectangle((x, y, x2, y2), fill=(255, 255, 255), width=wid)
            y += wid
            y2 += wid
    im.save("zebra.png")
---------------------------------------
from PIL import Image, ImageDraw


def train(name):
    im = Image.new("RGB", (280, 200), '#CCECFF')
    drawer = ImageDraw.Draw(im)
    drawer.rectangle(((40, 110), (80, 150)), '#C55A11')
    drawer.rectangle(((80, 90), (160, 150)), '#0070C0')
    drawer.rectangle(((160, 50), (240, 150)), '#548235')
    drawer.rectangle(((185, 60), (215, 100)), '#FFFFFF')
    drawer.rectangle(((150, 40), (250, 50)), '#C55A11')
    drawer.rectangle(((80, 60), (110, 90)), '#FF0000')
    drawer.polygon(((40, 110), (60, 75), (80, 110)), '#FFC000')
    drawer.polygon(((80, 60), (95, 34), (110, 60)), '#FFC000')
    drawer.ellipse(((80, 140), (110, 170)), '#000000')
    drawer.ellipse(((120, 130), (160, 170)), '#000000')
    drawer.ellipse(((180, 130), (220, 170)), '#000000')
    im.save(name)
----------------------------------------
from PIL import Image, ImageDraw


def human(wc, lc, m, lw):
    im = Image.new("RGB", (16 * m, 21 * m), wc)
    drawer = ImageDraw.Draw(im)
    drawer.line((8 * m, 5 * m, 8 * m, 11 * m), fill=lc, width=lw)
    drawer.line((7 * m, 6 * m, 9 * m, 6 * m), fill=lc, width=lw)
    drawer.line((7 * m, 6 * m, 4 * m, 10 * m), fill=lc, width=lw)
    drawer.line((9 * m, 6 * m, 12 * m, 10 * m), fill=lc, width=lw)
    drawer.line((4 * m, 10 * m, 6 * m, 13 * m), fill=lc, width=lw)
    drawer.line((12 * m, 10 * m, 15 * m, 7 * m), fill=lc, width=lw)
    drawer.line((8 * m, 11 * m, 6 * m, 15 * m), fill=lc, width=lw)
    drawer.line((8 * m, 11 * m, 11 * m, 10 * m), fill=lc, width=lw)
    drawer.line((6 * m, 15 * m, 5 * m, 20 * m), fill=lc, width=lw)
    drawer.line((11 * m, 10 * m, 13 * m, 15 * m), fill=lc, width=lw)
    drawer.line((5 * m, 20 * m, 7 * m, 20 * m), fill=lc, width=lw)
    drawer.line((13 * m, 15 * m, 15 * m, 14 * m), fill=lc, width=lw)
    drawer.ellipse((6 * m, 1 * m, 10 * m, 5 * m), width=lw, outline=lc)
    drawer.ellipse((7 * m - m // 5, 3 * m - m // 5, 7 * m + m // 5, 3 * m + m // 5), fill=lc, width=lw, outline=lc)
    drawer.ellipse((9 * m - m // 5, 3 * m - m // 5, 9 * m + m // 5, 3 * m + m // 5), fill=lc, width=lw, outline=lc)
    drawer.arc((6 * m, 1 * m - m // 2, 10 * m, 5 * m - m // 2), 45, 45 + 90, width=lw, fill=lc)
    drawer.ellipse((7 * m - m // 5, 6 * m - m // 5, 7 * m + m // 5, 6 * m + m // 5), width=lw, outline=lc)
    drawer.ellipse((9 * m - m // 5, 6 * m - m // 5, 9 * m + m // 5, 6 * m + m // 5), width=lw, outline=lc)
    drawer.ellipse((8 * m - m // 5, 11 * m - m // 5, 8 * m + m // 5, 11 * m + m // 5), width=lw, outline=lc)
    drawer.ellipse((4 * m - m // 5, 10 * m - m // 5, 4 * m + m // 5, 10 * m + m // 5), width=lw, outline=lc)
    drawer.ellipse((12 * m - m // 5, 10 * m - m // 5, 12 * m + m // 5, 10 * m + m // 5), width=lw, outline=lc)
    drawer.ellipse((6 * m - m // 5, 15 * m - m // 5, 6 * m + m // 5, 15 * m + m // 5), width=lw, outline=lc)
    drawer.ellipse((5 * m - m // 5, 20 * m - m // 5, 5 * m + m // 5, 20 * m + m // 5), width=lw, outline=lc)
    drawer.ellipse((11 * m - m // 5, 10 * m - m // 5, 11 * m + m // 5, 10 * m + m // 5), width=lw, outline=lc)
    drawer.ellipse((13 * m - m // 5, 15 * m - m // 5, 13 * m + m // 5, 15 * m + m // 5), width=lw, outline=lc)
    im.save("human.png")
---------------------------------------
from PIL import Image, ImageDraw


def weather_vane_orientation(size, c, *args):
    args = list(args)
    im = Image.new("RGB", size, c)
    drawer = ImageDraw.Draw(im)
    for i in args:
        a, b, f = i
        s = int(str(f)[-1]) * 4
        x, y = a - s // 2, b - s // 2
        x2, y2 = a + s // 2, b + s // 2
        drawer.rectangle(((x, y), (x2, y2)), (f, f, f))
    return im