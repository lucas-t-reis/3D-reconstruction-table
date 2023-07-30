import pyrealsense2 as rs
import numpy as np
import cv2
import time

class IntelCamera:
    def __init__(self):
        self.pipeline = rs.pipeline()
        self.profile = rs.config()
        self.model = 'D435i'

    def config_profile(self, width: int = 640, height: int = 480, fps: int = 30):
        self.profile.enable_stream(rs.stream.depth, width, height, rs.format.z16, fps)
        self.profile.enable_stream(rs.stream.color, width, height, rs.format.rgb8, fps)

    def capture_frame(self):
        try:
            # This call waits until a new coherent set of frames is available on a device
            frames = self.pipeline.wait_for_frames()
        except RuntimeError as ignore:
            print('Failed to fetch frames')
            return None

        # Get color frame
        color = frames.get_color_frame()
        if not color:
            return None
        
        # Convert images to numpy arrays
        color_image = np.asanyarray(color.get_data())
        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        return cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)


    def capture_photos(self, num_photos=5, delay=5):
        try:
            for i in range(num_photos):
                color_image = self.capture_frame()
                if color_image is None:
                    continue

                cv2.imwrite(f'photo_{i}.png', color_image)

                time.sleep(delay)
        finally:
            self.pipeline.stop()

    def capture_video(self, duration=5, video_name = 'output', codec = 'mp4v'):
        try:
            self.pipeline.start(self.profile)
            print(f'Startig capture with {duration} s')
            # Define the codec
            fourcc = cv2.VideoWriter_fourcc(*codec)
            out = cv2.VideoWriter(f'{video_name}.mp4', fourcc, 30, (640, 480))

            start_time = time.time()
            while True:
                color_image = self.capture_frame()
                if color_image is None:
                    continue

                out.write(color_image)

                if time.time() - start_time > duration:
                    break
        finally:
            out.release()
            self.pipeline.stop()

    def stream_camera(self):
        print('Press "q" to close the stream.')
        try:
            while True:
                color_image = self.capture_frame()
                if color_image is None:
                    continue

                cv2.imshow('RGB Stream', color_image)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            cv2.destroyAllWindows()
            self.pipeline.stop()

    def stream_depth(self):
        print('Press "q" to close the stream.')
        try:
            while True:
                frames = self.pipeline.wait_for_frames()
                depth = frames.get_depth_frame()
                if not depth:
                    continue

                depth_image = np.asanyarray(depth.get_data())
                depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

                cv2.imshow('Depth Stream', depth_colormap)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            cv2.destroyAllWindows()
            self.pipeline.stop()

    # TODO: Fix resource busy when this function is called
    def record_rgbd(self, duration=5, filename='output'):
        # Start the pipeline with a configuration that enables recording
        self.profile.enable_record_to_file(f'{filename}.bag')
        self.pipeline.start(self.config)
        
        time.sleep(duration)
        
        # Stop the pipeline
        self.pipeline.stop()