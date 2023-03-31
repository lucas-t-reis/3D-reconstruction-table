import cv2

# Open the video file
cap = cv2.VideoCapture('video.mp4')

# Define the frame rate and interval
frame_rate = cap.get(cv2.CAP_PROP_FPS)
interval = int(frame_rate / 5)  # Get a frame every 5th of a second

# Initialize variables
frame_count = 0
success = True

# Loop through the video frames
while success:
    success, frame = cap.read()
    if not success:
        break

    frame_count += 1

    if frame_count % interval == 0:
        filename = f'frame_{frame_count}.jpg'
        cv2.imwrite(filename, frame)


cap.release()
cv2.destroyAllWindows()
