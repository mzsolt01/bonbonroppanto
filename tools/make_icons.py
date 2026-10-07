"""Az app ikonjainak előállítása (icon-512.png, icon-192.png, apple-touch-icon.png).

Futtatás a projekt gyökeréből: python tools/make_icons.py
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

S = 1024  # rajzolási méret; a végén kicsinyítünk, így simák lesznek az élek
ROOT = Path(__file__).resolve().parent.parent


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def background():
    img = Image.new('RGB', (S, S))
    px = img.load()
    top, mid, bottom = (122, 36, 97), (74, 20, 82), (42, 14, 58)
    for y in range(S):
        for x in range(S):
            d = math.hypot(x - S * .5, y - S * .3) / (S * .9)
            px[x, y] = lerp(top, mid, min(1, d * 1.6)) if d < .62 else lerp(mid, bottom, min(1, (d - .62) * 2.6))
    return img


def sprinkles(draw):
    cols = [(255, 163, 180), (255, 201, 143), (255, 243, 166), (168, 245, 193), (163, 212, 255), (223, 188, 255)]
    spots = [(150, 170, 20), (840, 140, 70), (120, 760, 120), (880, 820, 30), (250, 905, 150), (790, 330, 100),
             (215, 400, 60), (900, 560, 160), (480, 105, 10), (560, 930, 80)]
    for i, (x, y, a) in enumerate(spots):
        r = math.radians(a)
        dx, dy = math.cos(r) * 26, math.sin(r) * 26
        draw.line((x - dx, y - dy, x + dx, y + dy), fill=cols[i % 6], width=16)


def candy(img):
    cx, cy, r = S * .5, S * .52, S * .27
    layer = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # csavart csomagolópapír két oldalt
    for side in (-1, 1):
        x0 = cx + side * r * .82
        x1 = cx + side * r * 1.75
        d.polygon([(x0, cy), (x1, cy - r * .62), (x1 - side * r * .18, cy), (x1, cy + r * .62)], fill=(255, 92, 143))
        d.polygon([(x0, cy), (x1 - side * r * .18, cy - r * .3), (x1 - side * r * .18, cy + r * .3)], fill=(255, 143, 194))
    # árnyék
    shadow = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).ellipse((cx - r, cy - r + 40, cx + r, cy + r + 40), fill=(20, 0, 30, 140))
    shadow = shadow.filter(ImageFilter.GaussianBlur(28))
    img.alpha_composite(shadow)
    img.alpha_composite(layer)
    # a bonbon teste: fényes piros gömb
    ball = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    bp = ball.load()
    light, base, dark = (255, 163, 180), (255, 59, 92), (168, 15, 46)
    for y in range(int(cy - r), int(cy + r) + 1):
        for x in range(int(cx - r), int(cx + r) + 1):
            dd = math.hypot(x - cx, y - cy)
            if dd <= r:
                t = math.hypot(x - (cx - r * .35), y - (cy - r * .42)) / (r * 1.5)
                col = lerp(light, base, min(1, t * 1.8)) if t < .55 else lerp(base, dark, min(1, (t - .55) * 2.2))
                a = 255 if dd < r - 1 else int(255 * (r - dd + 1))
                bp[x, y] = (*col, max(0, min(255, a)))
    # fehér spirálcsíkok
    sw = ImageDraw.Draw(ball)
    pts = []
    for i in range(0, 1400):
        a = i / 1400 * math.pi * 5
        rad = r * .92 * i / 1400
        pts.append((cx + math.cos(a) * rad, cy + math.sin(a) * rad))
    sw.line(pts, fill=(255, 240, 245, 210), width=34, joint='curve')
    mask = Image.new('L', (S, S), 0)
    ImageDraw.Draw(mask).ellipse((cx - r, cy - r, cx + r, cy + r), fill=255)
    ball.putalpha(Image.composite(ball.getchannel('A'), Image.new('L', (S, S), 0), mask))
    img.alpha_composite(ball)
    # csillanás
    gl = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(gl).ellipse((cx - r * .62, cy - r * .78, cx - r * .02, cy - r * .42), fill=(255, 255, 255, 150))
    img.alpha_composite(gl.filter(ImageFilter.GaussianBlur(10)))


def main():
    img = background().convert('RGBA')
    sprinkles(ImageDraw.Draw(img))
    candy(img)
    img = img.convert('RGB')
    for name, size in (('icon-512.png', 512), ('icon-192.png', 192), ('apple-touch-icon.png', 180)):
        img.resize((size, size), Image.LANCZOS).save(ROOT / name, optimize=True)
    print('ikonok kész')


if __name__ == '__main__':
    main()
