from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO('/home/orin/Ghaat/Code/Data/Model/9m_450.pt')

# Input and output paths
video_path = '/home/orin/Ghaat/Code/Data/Videos/VID_05.mp4'
output_path = '/home/orin/Ghaat/Code/Data/Videos/VID_05_output.mp4'

# Open video
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Create video writer with H.264 codec for .mp4
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # H.264 codec
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

frame_count = 0
print(f"Processing video: {total_frames} frames at {fps} FPS")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Run inference on frame
    results = model(frame, conf=0.25, device='0', verbose=False)
    
    # Get annotated frame
    annotated_frame = results[0].plot()
    
    # Write frame to output video
    out.write(annotated_frame)
    
    frame_count += 1
    if frame_count % 30 == 0:  # Print progress every 30 frames
        print(f"Processed {frame_count}/{total_frames} frames ({(frame_count/total_frames)*100:.1f}%)")

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"\nVideo processing complete!")
print(f"Output saved to: {output_path}")
