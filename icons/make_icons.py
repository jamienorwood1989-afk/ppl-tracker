from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = r'C:\Windows\Fonts\arialbd.ttf'

def make_icon(size, path):
    s = size / 512
    img = Image.new('RGB', (size, size), (11, 15, 20))  # app --bg #0b0f14
    d = ImageDraw.Draw(img)
    green = (52, 211, 153)   # app --good #34d399
    white = (230, 237, 243)  # app --tx #e6edf3

    # Barbell: bar + plates, centred at (256, 185) in 512-space
    cy = 185 * s
    # bar
    d.rectangle([100*s, cy-9*s, 412*s, cy+9*s], fill=green)
    # collars (small, where plates meet the bar)
    for cx in (156*s, 356*s):
        d.rectangle([cx-8*s, cy-20*s, cx+8*s, cy+20*s], fill=white)
    # plates: outer bigger, inner smaller, each side
    for (cx, hw, hh) in [(80*s, 26*s, 60*s), (122*s, 22*s, 46*s),
                         (432*s, 26*s, 60*s), (390*s, 22*s, 46*s)]:
        d.rounded_rectangle([cx-hw, cy-hh, cx+hw, cy+hh], radius=hw*0.6, fill=green)

    # PPL wordmark
    try:
        f = ImageFont.truetype(FONT, int(120*s))
    except OSError:
        f = ImageFont.load_default()
    txt = 'PPL'
    bbox = d.textbbox((0, 0), txt, font=f)
    w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
    d.text(((size-w)/2 - bbox[0], 330*s - bbox[1]), txt, font=f, fill=white)

    img.save(path, 'PNG')
    print('wrote', path, size)

make_icon(512, os.path.join(HERE, 'icon-512.png'))
make_icon(192, os.path.join(HERE, 'icon-192.png'))
make_icon(180, os.path.join(HERE, 'apple-touch-icon.png'))
