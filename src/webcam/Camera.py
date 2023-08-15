import cv2
import time

class Camera:
    def __init__(self):
        self.name = ''
        self.id = 0

    def capture_frame(self, capture):
        # Read a frame from the capture device
        ret, frame = capture.read()

        if not ret:
            print("Failed to capture frame")
            frame = None

        return frame

    def capture_video(self, duration, output_file = 'output'):
        # TODO: Fetch webcam id dinamically
        print("Depending on the hardware you are running, the webcam ID might change.\nOpen 'Camera.py' file and navigate to capture_video to modify the default id.")
        webcam = int(2)

        # Open the first webcam device
        capture = cv2.VideoCapture(webcam)

        if not capture.isOpened():
            print('Could not open camera device')
            exit()

        # Get the width, height, and frames per second of the video
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = capture.get(cv2.CAP_PROP_FPS)

        writer = cv2.VideoWriter(f'{output_file}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        start_time = time.time()
        
        while True:
            frame = self.capture_frame(capture)

            if frame is not None:
                writer.write(frame)

            # Break loop if the specified duration has passed
            if time.time() - start_time > duration:
                break

            # Break loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        capture.release()
        writer.release()
        cv2.destroyAllWindows()