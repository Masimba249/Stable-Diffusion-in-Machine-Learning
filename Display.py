import os
from PIL import Image
from IPython.display import display

def display_renders(folder):
    for f in sorted(os.listdir(folder)):
        if f.endswith('.png'):
            img = Image.open(os.path.join(folder, f))
            print(f)
            display(img)

display_renders('/content/drive/MyDrive/text_to_3d_project/stable-dreamfusion/trial/renders')