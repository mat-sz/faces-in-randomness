import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
  # Generate a grey scale bitmap.
  float_img = np.random.random((256,256))
  im = np.array(float_img * 255, dtype = np.uint8)

  faces = face_cascade.detectMultiScale(im, 1.1, 4)

  if len(faces) > 0:
    # Draw the rectangle around each face.
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display image.
    cv2.imshow('img', im)
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 
  