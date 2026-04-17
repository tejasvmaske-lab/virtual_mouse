# 🖱️ Virtual Mouse Using Python

Control your computer cursor using **hand gestures** through your webcam using **Computer Vision**.

## 🚀 Project Overview

This project uses:

* **OpenCV** → Webcam access & image processing
* **MediaPipe** → Hand tracking & landmark detection
* **PyAutoGUI** → Mouse control

The system detects your hand in real time, tracks your **index finger**, and moves the mouse cursor based on finger position.

---

## ✨ Features

✅ Real-time webcam hand tracking
✅ Hand skeleton visualization
✅ Index finger detection
✅ Cursor movement using finger
✅ Mirror correction (natural left-right movement)
✅ Smooth cursor movement

---

## 🧠 How It Works

1. Capture webcam frames using OpenCV
2. Detect hand landmarks using MediaPipe
3. Get index finger tip coordinates
4. Map camera coordinates to screen coordinates
5. Move system cursor using PyAutoGUI
6. Apply smoothing for stable movement

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* PyAutoGUI

---

## ⚠️ Python Version / Virtual Environment

For best compatibility, use **Python 3.10.x**.

Some versions of MediaPipe may not work properly with newer Python versions.

### Create Virtual Environment

```bash id="n2r2mu"
py -3.10 -m venv venv
```

### Activate (Windows)

```bash id="8i9n5n"
venv\Scripts\activate
```

After activation, your terminal should show:

```text id="0dbu2j"
(venv)
```

---

## 📦 Installation

```bash id="4v0kij"
pip install opencv-python mediapipe pyautogui
```

---

## ▶️ Run the Project

```bash id="rj23pn"
python test.py
```

(Replace `test.py` with your actual file name)

---

## 📁 Project Structure

```text id="g7ik9v"
virtual_mouse/
│── test.py
│── .gitignore
│── README.md
│── venv/   (ignored in GitHub)
```

---

## 🔮 Future Improvements

* Click using finger pinch gesture
* Drag and drop
* Scroll using gestures
* Multi-hand controls
* Better UI / FPS counter

---

## 📸 Demo

Add screenshots or demo GIF here later.

---

## 🙌 Learning Outcomes

This project helped in understanding:

* Computer Vision basics
* Coordinate systems
* Real-time tracking
* Gesture-based interfaces
* Python project setup with virtual environments

---

## 📜 License

This project is for learning and educational purposes.
