import numpy as np
from PIL import Image, ImageDraw
import os
def round_image(path):
    # Open the input image as numpy array, convert to RGB
    # "assets/imgs/edit_image_use.png"
    img=Image.open(path).convert("RGB")
    npImage=np.array(img)
    h,w=img.size

    # Create same size alpha layer with circle
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)

    # Convert alpha Image to numpy array
    npAlpha=np.array(alpha)

    # Add alpha layer to RGB
    npImage=np.dstack((npImage,npAlpha))
    filepath = 'assets/imgs/profile_pic_final_edit.png'
    # Save with alpha
    Image.fromarray(npImage).save(filepath)
    return filepath