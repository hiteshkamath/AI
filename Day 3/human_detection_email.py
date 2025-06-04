import cv2
import mediapipe as mp
import time
import smtplib
import ssl
from email.message import EmailMessage
from playsound import playsound

# MediaPipe Setup
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

# Email setup
sender_email = "sender@gmail.com"
app_password = "app password"
receiver_email = "receiver@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 465

# Webcam
cap = cv2.VideoCapture(0)
last_screenshot_time = 0  # Track last screenshot time

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)

    if results.pose_landmarks:
        #mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Play alert sound
        playsound("alert.wav", block=False)

        current_time = time.time()
        if current_time - last_screenshot_time >= 10:
            # Take screenshot
            filename = f"screenshot_{int(current_time)}.jpg"
            cv2.imwrite(filename, frame)
            print("[INFO] Screenshot saved:", filename)

            # Send Email with attachment
            msg = EmailMessage()
            msg['Subject'] = "Human Detected via Pose Estimation"
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg.set_content("A human has been detected. See the attached screenshot.")

            with open(filename, 'rb') as f:
                img_data = f.read()
                msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename=filename)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
                server.login(sender_email, app_password)
                server.send_message(msg)
                print(f"[INFO] Email sent to {receiver_email}")

            last_screenshot_time = current_time  # Update the last screenshot time

    cv2.imshow("Pose Estimation", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()