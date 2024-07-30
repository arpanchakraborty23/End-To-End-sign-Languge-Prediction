import os,sys
import cv2
import time
import uuid

from signLanguage.logger.logger import logging
from signLanguage.exception.exception import CustomException

IMAGE_PATH = "customdata"

labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']

number_of_images = 5
try:
    for label in labels:
        img_path = os.path.join(IMAGE_PATH, label)
        os.makedirs(img_path, exist_ok=True)  # ensure the directory is created if it doesn't exist

        # Open camera
        cap = cv2.VideoCapture(0)  # changed to 0, commonly used for default camera
        if not cap.isOpened():
            raise CustomException(f"Unable to open camera")

        print(f"Collecting images for {label}")
        time.sleep(3)
       

        for imgnum in range(number_of_images):
            ret, frame = cap.read()
            if not ret:
                raise CustomException("Failed to capture image")

            imagename = os.path.join(img_path, f"{label}.{uuid.uuid1()}.jpg")
            cv2.imwrite(imagename, frame)
            cv2.imshow('frame', frame)
            time.sleep(2)
        
            logging.info(f' {label} data collected')

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
    cv2.destroyAllWindows()

except CustomException as ce:
    logging.error(f"CustomException occurred: {ce}")
except Exception as e:
    logging.error(f"An error occurred: {e}")
    raise CustomException(sys, e)
