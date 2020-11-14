import numpy as np
import cv2
import threading
import time
import sys

count = 0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

print('faces-in-randomness initialized')
sys.stdout.flush()

def display_time():
  global count

  while True:
    sys.stdout.write("\r")
    sys.stdout.write('Current speed: ' + str(count) + ' images/s      ')
    sys.stdout.flush()
    count = 0
    time.sleep(1)

def search_for_faces():
  global count

  while True:
    # Generate a grey scale bitmap.
    float_img = np.random.random((256,256))
    im = np.array(float_img * 255, dtype = np.uint8)

    faces = face_cascade.detectMultiScale(im, 1.1, 4)
    count += 1

    if len(faces) > 0:
      # Draw the rectangle around each face.
      for (x, y, w, h) in faces:
          cv2.rectangle(im, (x, y), (x+w, y+h), (255, 0, 0), 2)

      # Display image.
      cv2.imshow('img', im)
      cv2.waitKey(0) 
      cv2.destroyAllWindows()

threading.Thread(target=display_time).start()
threading.Thread(target=search_for_faces).start()
