# 🎭 Real-Time AI-Powered Emotion & Face Recognition Toolkit

This project brings together **computer vision** and **AI** to explore real-time face mesh detection, emotion recognition (with voice), and hand distance monitoring using your webcam. Built with Python, it combines the power of **DeepFace**, **MediaPipe**, **OpenCV**, **pyttsx3**, and **Pygame**.

---

## 📌 Features

- 🎭 Real-Time Emotion Detection using DeepFace  
- 🗣️ Voice Feedback for emotions using pyttsx3  
- ✋ Hand Distance Measurement with alert sound  
- 👁️ Face Mesh Detection using MediaPipe  
- 🖥️ Lightweight, runs locally on most machines  
- 🔌 No internet needed after installation

---

## 📂 Project Structure

```
emotion-ai-suite/
├── emotion_detection.py             # Basic emotion detection with DeepFace
├── emotion_detection_withvoice.py  # Emotion detection with voice output
├── hand_distance.py                # Hand distance detection with sound alert
├── face_detection.py               # Face mesh visualization
├── alert.wav                       # Sound used in hand_distance.py
├── README.md                       # This file
└── demo.png / demo.gif             # Optional: Visual preview

```

## 🛠️ Installation

Install the required packages:

```bash
pip install opencv-python mediapipe deepface pyttsx3 pygame

```

---

## 🚀 Getting Started

Follow these steps to run the project:

1. **Clone the repository** or download the ZIP file and extract it.
2. **Open a terminal** and navigate to the project folder.
3. **Run any of the following scripts depending on your need:**

### ▶️ Emotion Detection (Text Only)

```bash
python emotion_detection.py

```
---
## 🌱 Future Improvements

- Add emotion log history & graphs  
- Visual dashboards for each program  
- Merge all features into a single UI using Streamlit or Gradio  
- Add image/video input support

---

## 🧾 Requirements Summary

- Python 3.7+
- OpenCV (`opencv-python`)
- MediaPipe
- DeepFace
- pyttsx3 (for text-to-speech)
- pygame (for sound alerts)
- TensorFlow (optional but recommended)

---

## 🙌 Credits

This project uses:
- [DeepFace](https://github.com/serengil/deepface)
- [MediaPipe](https://google.github.io/mediapipe/)
- [OpenCV](https://opencv.org/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [pygame](https://pypi.org/project/pygame/)

---

## 📄 License

This project is licensed under the **MIT License**.

---

Made with ❤️ using Python and AI.
