from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('/home/shivakrishnakarnati/Documents/Programming/Python_project/yolo/ultralytics/runs/detect/train11/weights/best.torchscript')

# Define path to the image file
results = model.predict('/home/shivakrishnakarnati/Documents/Programming/ML_projects/yolo/my_custom_dataset/test/images/', save=True)

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    
    
