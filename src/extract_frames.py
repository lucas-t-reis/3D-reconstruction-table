import os
import cv2
import argparse

# Extract frames every ith of a second
def extract_frames(video, interval, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    capture = cv2.VideoCapture(video)

    # Define the frame rate and interval
    frame_rate = capture.get(cv2.CAP_PROP_FPS)
    interval = int(frame_rate / interval)  # Get a frame every ith interval of a second

    frame_count = 0
    success = True
    while success:
        success, frame = capture.read()
        if not success:
            break

        frame_count += 1

        if frame_count % interval == 0:
            filename = f'frame_{frame_count}.jpg'
            fullpath = os.path.join(output_path, filename)
            cv2.imwrite(fullpath, frame)

    capture.release()
    cv2.destroyAllWindows()

def main():

    parser = argparse.ArgumentParser(description='Extract images, given interval of time, from a video.')
    parser.add_argument('video', help='Path to video file. Ex. ~/Downloads/video.mp4.')
    parser.add_argument('interval', type=int, help='Defines the amount of frames saved per second.')
    parser.add_argument('output_path', help='Defines the folder to dump the images to.')

    args = parser.parse_args()
    extract_frames(args.video, args.interval, args.output_path)
    
if __name__ == '__main__':
    main()