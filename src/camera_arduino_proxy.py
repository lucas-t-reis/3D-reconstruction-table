import serial
from time import sleep

# TODO Use ls -l /dev/ttyACM* + grep to fetch port name
# TODO trycatch to handle resource busy
# TODO Controlling rotation based on steps

# Open a serial connection to Arduino UNO
connection = serial.Serial('/dev/ttyACM0', 9600)
# Wait for Arduino to reboot before issuing the first command
sleep(2)
data = input('c - Clockwise | C - Counter clockwise: ').encode('utf-8')
connection.write(data)
response = connection.readline()
print(response)
