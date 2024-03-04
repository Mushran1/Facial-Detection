# Face Detection in Python using OpenCV
This repository contains Python scripts for detecting faces in images, videos, and live webcam streams using OpenCV with the haarcascade_frontalface_default.xml classifier.

Features

Image Face Detection: Detect faces in static images.
Video Face Detection: Detect faces in video files.
Live Webcam Face Detection: Detect faces in real-time using your computer's webcam.
Multiple Face Detection: Capable of detecting multiple faces simultaneously.
Easy-to-Use: Simple scripts with clear comments for easy understanding and modification.
Prerequisites

Python 3.x
OpenCV library (pip install opencv-python)

Usage
1. Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/Mushran1/face-detection.git
2. Download the haarcascade_frontalface_default.xml file from the OpenCV GitHub repository or use the one provided in this repository.
3. Move the haarcascade_frontalface_default.xml file to the project directory.
4. Run the desired Python script according to your requirement:
For image face detection:
bash
Copy code
python image_face_detection.py --image path/to/image.jpg
For video face detection:
bash
Copy code
python video_face_detection.py --video path/to/video.mp4
For live webcam face detection:
bash
Copy code
python live_webcam_face_detection.py

Acknowledgements

This project is inspired by the OpenCV library and various tutorials available online.

License

This project is licensed under the MIT License.
