# Via https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#

import os
import sys

from PIL import Image, ImageDraw, ImageFont

# create an image
def create_image(filename):
    """
    Create image
    """

    out = Image.new("RGB", (400, 400), (255, 255, 255))
    # get a font
    fnt = ImageFont.truetype(filename, 300)
    print(filename)
    # get a drawing context
    d = ImageDraw.Draw(out)

    # draw multiline text
    d.multiline_text((30, 40), "Hs", font=fnt, fill=(0, 0, 0))

    fontname = filename.split(".")[0]  # Remove file extension
    out.save("logo_%s.png" % fontname, "PNG")


if __name__ == "__main__":

    # files = [f for f in os.listdir(".") if f.endswith("ttf")]
    # for filename in files:

    create_image("NotoSans-Regular.ttf")
