import cv2
import numpy as np
import time
import HandTracking as ht
import autopy   # Install using "pip install autopy"

pTime = 0
width = 640
height = 480
frameR = 100
smoothening = 8
prev_x, prev_y = 0, 0
curr_x, curr_y = 0, 0

