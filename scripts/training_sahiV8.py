from sahi.utils.yolov8  import download_yolov8s_model
from sahi import AutoDetectionModel
from sahi.utils.cv import read_image
from sahi.utils.file import download_from_url
from sahi.predict import get_prediction, get_sliced_prediction, predict
from pathlib import Path
import cv2
import numpy as np
import os

input_image_path = "my_custom_dataset/val/"

# Batch prediction
results = predict(
    model_type="yolov8",
    model_path="/home/shivakrishnakarnati/Documents/Programming/Python_project/yolo/ultralytics/runs/detect/train11/weights/best.pt",
    model_device="cpu",  # or 'cuda:0'
    model_confidence_threshold=0.4,
    source=input_image_path,
    slice_height=256,
    slice_width=256,
    overlap_height_ratio=0.2,
    overlap_width_ratio=0.2,
)


#####
# To write from the video
#####

"""

frames = cv2.imread(input_image_path+'*.png')

object_prediction_list = results.object_prediction_list

boxes_list = []
clss_list = []

for ind, _ in enumerate(object_prediction_list):
            boxes = (
                object_prediction_list[ind].bbox.minx,
                object_prediction_list[ind].bbox.miny,
                object_prediction_list[ind].bbox.maxx,
                object_prediction_list[ind].bbox.maxy,
            )
            clss = object_prediction_list[ind].category.name
            boxes_list.append(boxes)
            clss_list.append(clss)
            
for box, cls in zip(boxes_list, clss_list):
            x1, y1, x2, y2 = box
            cv2.rectangle(frames, (int(x1), int(y1)), (int(x2), int(y2)), (56, 56, 255), 2)
            label = str(cls)
            t_size = cv2.getTextSize(label, 0, fontScale=0.6, thickness=1)[0]
            cv2.rectangle(
                frames, (int(x1), int(y1) - t_size[1] - 3), (int(x1) + t_size[0], int(y1) + 3), (56, 56, 255), -1
            )
            cv2.putText(
                frames, label, (int(x1), int(y1) - 2), 0, 0.6, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA
            )
            

cv2.imwrite("output.png",frames)

"""