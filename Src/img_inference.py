from ultralytics import YOLO
import cv2
from pathlib import Path

# Load your trained model
model = YOLO('/home/orin/Ghaat/Code/Data/Model/9m_450.pt')

# Single image inference
results = model('/home/orin/Ghaat/Code/Data/Images/IMG_01.jpg')

# Process results
for result in results:
    # Display image with detections
    result.show()
    
    # Save annotated image
    result.save(filename='result.jpg')
    
    # Print detection info
    boxes = result.boxes
    for box in boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        print(f"Class: {model.names[cls]}, Confidence: {conf:.2f}")

# Batch inference on multiple images
image_folder = '/home/orin/Ghaat/Code/Data/Images/'
results = model(image_folder)

# Save all results
for i, result in enumerate(results):
    result.save(filename=f'results/result_{i}.jpg')

# Inference with custom parameters
results = model(
    source='/home/orin/Ghaat/Code/Data/Images/',
    conf=0.25,        # Confidence threshold
    iou=0.45,         # NMS IOU threshold
    imgsz=640,        # Image size
    device='0',       # Use GPU 0 (or 'cpu' for CPU)
    save=True,        # Save results
    save_txt=True,    # Save labels as .txt
    save_conf=True,   # Include confidence in labels
    project='runs/detect',
    name='exp'
)

# Access detection data
for result in results:
    boxes = result.boxes.xyxy.cpu().numpy()  # Bounding boxes
    confidences = result.boxes.conf.cpu().numpy()  # Confidence scores
    classes = result.boxes.cls.cpu().numpy()  # Class IDs
    
    print(f"Found {len(boxes)} objects")
