import serial
import threading
from time import sleep

from webcam import Camera 

# There is also a specific class for IntelCamera configured with some presets in intelcamera folder.
camera = Camera()

# TODO Spawn a need thread for each iteration. Currently in the second iteration the code breaks because it attempts to use the same thread as before
video_thread = threading.Thread(target = camera.capture_video, kwargs={'duration' : 30})

DEFAULT_MESSAGE = 'c - Clockwise | C - Counter clockwise: '

# TODO Use ls -l /dev/ttyACM* + grep to fetch port name
connection = serial.Serial('/dev/ttyACM0', 9600)

# Wait for Arduino to reboot before issuing the first command
sleep(2)
while(data := input(DEFAULT_MESSAGE).encode('utf-8')):
    if data == 'q'.encode('utf-8'):
        break
    video_thread.start()
    connection.write(data)
    response = connection.readline()
    print(response)

video_thread.join()
