import glob
import random
from shutil import copyfile

images = glob.glob("images/*.png")

train_img_dir = "train/"
test_img_dir = "test/"


for img in images:
    label = "labels/" + img[7:] + ".txt"
    if random.random() < 0.8:
        copyfile(img,train_img_dir+ img)
        copyfile(label,train_img_dir+label)
    else:
        copyfile(img, test_img_dir + img)
        copyfile(label,test_img_dir+label)



