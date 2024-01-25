from PIL import ImageGrab
import numpy
import cv2
from win32api import GetSystemMetrics
import datetime

print("Hi MUHAMMAD Mohib"[::-1])
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
file_name = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))
# cam = cv2.VideoCapture(0)
start_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
while True:
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    if int(now_time) - int(start_time) >= 12:
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = numpy.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        '''_, frame = cam.read()
        fr_height, fr_width, _ = frame.shape
        img_final[0:fr_height, 0:fr_width, :] = frame[0:fr_height, 0:fr_width, :]'''
        # cv2.imshow('secret capture', img_final)

        captured_video.write(img_final)
    # cv2.imshow('cam', frame)
    if cv2.waitKey(10) == ord('q'):
        break