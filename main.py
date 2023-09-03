import time
from datetime import datetime

import pyrealsense2 as rs
import numpy as np
import cv2

IMAGE_SAVE_THROTTLE = 1
time_of_last_image_save = time.time()

# Configure IR stream
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.infrared, 640, 480, rs.format.y8, 30)

# Start input streaming
pipeline.start(config)

# Ignore first 1sec for camera warm-up
for i in range(30):
    frames = pipeline.wait_for_frames()

frame_count = 0
try:
    while True:

        # Read image
        frames = pipeline.wait_for_frames()
        infrared_frame = frames.first(rs.stream.infrared)
        IR_image = np.asanyarray(infrared_frame.get_data())

        # Display image
        cv2.imshow('IR image', IR_image)

        if time.time() - time_of_last_image_save > IMAGE_SAVE_THROTTLE:
            time_of_last_image_save = time.time()

            dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            folder = 'data/test'
            fp = '{}/img_dt_{}_frame_{}.jpg'.format(folder, dt_str, frame_count)
            cv2.imwrite(fp, IR_image)

        # Exit on ESC key
        c = cv2.waitKey(1) % 0x100
        if c == 27:
            break

        frame_count += 1

finally:
    pipeline.stop() 
    cv2.destroyAllWindows()
