import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFont, ImageDraw

# read image and convert to RGB
image=Image.open("msi_recruitment.gif")
image=image.convert('RGB')

# use the given font
font = ImageFont.truetype("calibri.ttf", 36)
draw = ImageDraw.Draw(image)
draw.text((0, 410), "channel intensity", fill=(255,255,255,0), font=font)

# build a list of 9 images which have different brightnesses
enhancer=ImageEnhance.Brightness(image)

# create a contact sheet from different brightnesses
contact_sheet=PIL.Image.new(image.mode, (image.width*3, image.height*3))
x=0
y=0

# 填充
for m in range(image.width):
    for n in range(image.height):
        draw.point((m, n+410), fill=(0,0,0))

for img in range(9):
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(image, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+image.width == contact_sheet.width:
        x=0
        y=y+image.height
    else:
        x=x+image.width
        
# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)