# Via https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#

# Fonts via https://github.com/python-pillow/Pillow/tree/master/Tests/fonts

import os
import sys

from PIL import Image, ImageDraw, ImageFont

# create an image
def create_image(filename):
    """
    Create image
    """

    out = Image.new("RGB", (480, 480), (0, 0, 0))
    # get a font
    fnt = ImageFont.truetype(filename, 300)
    print(filename)
    # get a drawing context
    d = ImageDraw.Draw(out)

    # draw multiline text
    d.multiline_text((60, 0), "Hs", font=fnt, fill=(255, 255, 255))

    fontname = filename.split(".")[0]  # Remove file extension
    out.save("logo_%s.png" % fontname, "PNG")


if __name__ == "__main__":

    # files = [f for f in os.listdir(".") if f.endswith("ttf")]
    # for filename in files:

    create_image("NotoSans-Regular.ttf")
