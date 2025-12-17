from ultralytics import YOLO
import cv2
import time
import numpy as np

# Load TensorRT model
print("Loading TensorRT engine...")
model = YOLO('/home/orin/Ghaat/Code/Data/Model/9m_450.engine')
print("TensorRT engine loaded successfully!")

# GStreamer pipeline for IMX519 camera on Jetson
gst_pipeline = (
    "nvarguscamerasrc ! "
    "video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=30/1 ! "
    "nvvidconv ! "
    "video/x-raw, format=BGRx ! "
    "videoconvert ! "
    "video/x-raw, format=BGR ! "
    "appsink"
)

# Open camera with GStreamer pipeline
cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Error: Could not open IMX519 camera")
    exit()

print("Camera opened successfully!")
print("Running TensorRT inference on live feed...")
print("Press 'q' to quit, 's' to save current frame")

# Variables for FPS calculation
frame_count = 0
start_time = time.time()
fps_update_interval = 30  # Update FPS every 30 frames

# For smoothed FPS display
fps_history = []
display_fps = 0.0

while True:
    # Read frame from camera
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture frame")
        break
    
    # Run TensorRT inference
    inference_start = time.time()
    results = model(frame, conf=0.25, device='0', verbose=False)
    inference_time = (time.time() - inference_start) * 1000  # ms
    
    # Get annotated frame
    annotated_frame = results[0].plot()
    
    # Calculate FPS
    frame_count += 1
    elapsed_time = time.time() - start_time
    current_fps = frame_count / elapsed_time
    
    # Smooth FPS for display
    fps_history.append(current_fps)
    if len(fps_history) > 10:
        fps_history.pop(0)
    display_fps = np.mean(fps_history)
    
    # Add performance metrics to frame
    cv2.putText(annotated_frame, f'FPS: {display_fps:.1f}', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(annotated_frame, f'Inference: {inference_time:.1f}ms', (10, 70), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow('TensorRT YOLO Inference', annotated_frame)
    
    # Handle keyboard input
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord('s'):
        filename = f'tensorrt_capture_{frame_count}.jpg'
        cv2.imwrite(filename, annotated_frame)
        print(f"Saved: {filename}")
    
    # Print detection info periodically
    if frame_count % fps_update_interval == 0:
        boxes = results[0].boxes
        print(f"Frame {frame_count}: Detected {len(boxes)} objects | "
              f"FPS: {display_fps:.1f} | Inference: {inference_time:.1f}ms")

# Release resources
cap.release()
cv2.destroyAllWindows()

print(f"\nInference stopped")
print(f"Average FPS: {display_fps:.1f}")
print(f"Total frames processed: {frame_count}")
