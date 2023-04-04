# from email_validator import validate_email, EmailNotValidError

# def check_email(em):
#     try:
        
#         if validate_email(em):
#             return True
#     except:
#         return False

# print(check_email("ola@hotmail.com"))
# print(check_email("ola@hotmailcom"))



# quest = ['What is TransportYoiu ?', 'What are my preferences ?', 'Options available:']
# matching = [ for i in range(0,len(quest)) if "available" in quest[i]]
# print(matching)





############################## make imge round  #################################3

import numpy as np
from PIL import Image, ImageDraw

# Open the input image as numpy array, convert to RGB
img=Image.open("assets/imgs/unknown.jpg").convert("RGB")
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

# Save with alpha
Image.fromarray(npImage).save('assets/imgs/unknown_pic.png')