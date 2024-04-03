import glob
import os

labels = glob.glob("my_custom_dataset/test/labels/*.png.txt")

for lab in labels:
    base_name, extension = os.path.splitext(os.path.basename(lab))  # Get the base filename without extension
    new_name = base_name.replace('.png', '')  + extension # Remove .jpg and .png extensions
    
    new_path = os.path.join(os.path.dirname(lab),new_name)

    os.rename(lab,new_path)

    print(f'Renamed:{lab} to {new_path}')

