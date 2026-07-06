import sys
from PIL import Image, ImageDraw

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def main():
    img_path = r'f:\YANG66-bot\src\header_.png'
    try:
        im = Image.open(img_path).convert('RGBA')
        
        # Round the corners. For a large banner, 30px is a good radius.
        w, h = im.size
        # Make the radius proportional, say 5% of height, or at least 20px
        rad = max(20, int(h * 0.05))
        rad = 30 # Let's stick to 30px
        im = add_corners(im, rad)
        
        im.save(img_path)
        print("Successfully rounded corners.")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
