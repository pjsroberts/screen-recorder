# importing the required packages
import pyautogui
import cv2
import numpy as np
import os

resolution = (1920, 1080)

codec = cv2.VideoWriter_fourcc(*"XVID")

output_dir = "output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

filename = os.path.join(output_dir, "My Recording.avi")

fps = 60.0

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Parker's Screen Recorder", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Parker's Screen Recorder", 480, 270)

while True:
	img = pyautogui.screenshot()

	frame = np.array(img)

	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	out.write(frame)
	
	cv2.imshow('Live', frame)
	
	if cv2.waitKey(1) == ord('q'):
		break

out.release()

cv2.destroyAllWindows()
