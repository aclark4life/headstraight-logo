from PIL import Image, ImageDraw, ImageFont
import sys

# create an image
out = Image.new("RGB", (400, 400), (255, 255, 255))

# get a font
fnt = ImageFont.truetype("FreeMono.ttf", 320)
# get a drawing context
d = ImageDraw.Draw(out)

# draw multiline text
d.multiline_text((10,10), "HS", font=fnt, fill=(0, 0, 0))

out.save("logo.png", "PNG")
