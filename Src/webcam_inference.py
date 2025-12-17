from ultralytics import YOLO
import cv2
import time

# Load your trained model
model = YOLO('/home/orin/Ghaat/Code/Data/Model/9m_450.pt')

# Open webcam using V4L2 backend (works on Jetson)
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# Set camera resolution (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Webcam opened successfully!")
print("Press 'q' to quit, 's' to save current frame")

frame_count = 0
start_time = time.time()

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture frame")
        break
    
    # Run inference
    results = model(frame, conf=0.25, device='0', verbose=False)
    
    # Get annotated frame
    annotated_frame = results[0].plot()
    
    # Calculate and display FPS
    frame_count += 1
    elapsed_time = time.time() - start_time
    fps = frame_count / elapsed_time
    
    # Add FPS text to frame
    cv2.putText(annotated_frame, f'FPS: {fps:.1f}', (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow('YOLO Webcam Inference', annotated_frame)
    
    # Handle keyboard input
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        # Quit
        break
    elif key == ord('s'):
        # Save current frame
        filename = f'webcam_capture_{frame_count}.jpg'
        cv2.imwrite(filename, annotated_frame)
        print(f"Saved: {filename}")
    
    # Print detection info every 30 frames
    if frame_count % 30 == 0:
        boxes = results[0].boxes
        print(f"Frame {frame_count}: Detected {len(boxes)} objects | FPS: {fps:.1f}")

# Release resources
cap.release()
cv2.destroyAllWindows()

print(f"\nWebcam inference stopped")
print(f"Average FPS: {fps:.1f}")
