# 🕵️‍♂️ Real-Time Human & Object Detection with OpenCV & MediaPipe

This project focuses on detecting human body poses, sending alerts on detection, and recognizing specific objects (like red-colored objects) in real-time using OpenCV and MediaPipe.

---

## 📌 Features

- Real-time full-body **pose estimation** using webcam  
- Automated **email alert with screenshot** when a human is detected  
- Simple **red object detection** using HSV color masking  
- Real-time visual feedback with OpenCV windows  
- Alert sound notification on human detection  

---

## 🛠️ Installation

Install the required packages using pip:

```bash
pip install opencv-python mediapipe playsound
```
(Optional for email functionality):
```bash
pip install secure-smtplib
```
---

## 🚀 Getting Started

Follow these steps to run each feature:

1. **Clone the repository** or download the ZIP and extract it.
2. **Open a terminal** in the project folder.
3. **Run any of the scripts as needed:**

---

### 🧍 Pose Estimation

```bash
python pose_estimation.py
```

•	Detects human pose landmarks in real-time using your webcam via MediaPipe.

•	Visualizes pose connections on screen.

•	Press Q to quit the video stream.

### 📧 Human Detection with Email Alert

```bash
python human_detection_email.py
```
•	Detects a human using pose landmarks.

•	Plays an alert sound and captures a screenshot.

•	Sends an email alert with the screenshot as an attachment.

•	Note: Update the following in the script:

  1.	Sender_email and Receiver_email
  
  2.	Your Gmail App Password
  
  3.	Ensure alert.wav file is present in the same folder.

### 🎯 Red Object Detection

```bash
python object_detection.py
```
•	Detects red-colored objects using HSV color space.

•	Displays both original and masked output in separate OpenCV windows.

•	Press Q to stop the detection.

---

## 📂 Project Structure

```

day03-detection/
├── pose_estimation.py          # Full-body pose detection using MediaPipe
├── human_detection_email.py    # Pose detection with sound + email alert
├── object_detection.py         # HSV-based red object detection
├── alert.wav                   # Alert sound file (required)
└── README.md                   # Project documentation

```
---

## 🌱 Future Improvements

•	Add object detection using YOLO or SSD for general objects

•	Use face detection along with pose for accuracy

•	Log detections with timestamps

•	Convert to a Flask or Gradio web app

---

## 🧾 Requirements Summary

•	Python 3.7+

•	OpenCV

•	MediaPipe

•	Playsound

•	smtplib (for email alerts)

---

## 🙌 Credits

This project uses:

•	MediaPipe
 
•	OpenCV
 
•	Playsound

---

## 📄 License

This project is licensed under the MIT License.

---

Made with ❤️ using Python, MediaPipe, and OpenCV.


