import cv2
from deepface import DeepFace
#Load Video from Webcam
cap = cv2.VideoCapture(0)

while True:
   key,img = cap.read()
   # Convert color format
   results = DeepFace.analyze(img,actions=['emotion'],enforce_detection=False)
   #Display Emotion on frame
   emotion = results[0]['dominant_emotion']
   cv2.putText(img,f'Emotion:{emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
   cv2.imshow("Emotion Recognition",img)

   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()