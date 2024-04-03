from ultralytics import YOLO

#model = YOLO('yolov8n.yaml')

model = YOLO('yolov8n.pt')

results = model.train(data='my_custom_dataset.yaml', epochs=10)

model.export()
