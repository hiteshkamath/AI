import cv2
from deepface import DeepFace
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

# Load Video from Webcam
cap = cv2.VideoCapture(0)
last_emotion = ""  # To avoid repeating the same emotion

while True:
    key, img = cap.read()
    if not key:
        break

    # Analyze the frame
    results = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
    emotion = results[0]['dominant_emotion']

    # Display emotion on frame
    cv2.putText(img, f'Emotion: {emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Emotion Recognition", img)

    # Speak emotion only when it changes
    if emotion != last_emotion:
        engine.say(f"You look {emotion}")
        engine.runAndWait()
        last_emotion = emotion

    # Exit loop on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
engine.stop()