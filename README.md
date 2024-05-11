
# Multi-face Recognition using OpenCV (CV2) and Face_Recognition Library in Python.

Detect and Recognize Multiple Faces in a Real Time Video Feed.


## Problem Definition

The problem addressed in this code is to develop a real-time face recognition system using OpenCV and the Face Recognition library. The goal is to be able to identify and recognize specific individuals (Srijan and his friends) from a live video stream.


## Methodology

<img width="1104" alt="Untitled" src="https://github.com/siripiripiri/cv2-multi-face-recognition/assets/68395391/3b253721-2855-41b8-b063-63952540b8ac">

- Input Video: The code starts by capturing a live video feed from the default camera using cv2.VideoCapture(0).
- Face Detection: The face_recognition.face_locations() function is used to detect the locations of faces in each frame of the video. Dlib's pre-trained facial landmark detector, a deep learning-based algorithm, is used for this purpose.
- Face Encoding: The face_recognition.face_encodings() function is used to generate a 128-dimensional encoding for each detected face. This encoding represents the unique facial features of an individual. FaceNet, a pre-trained deep learning model for extracting facial feature vectors is used.
<img width="611" alt="Screenshot 2024-05-09 at 11 43 41 AM" src="https://github.com/siripiripiri/cv2-multi-face-recognition/assets/68395391/149c1bfe-d95a-4712-b46f-134582eeaad5">

- Face Comparison: The code compares the face encoding of each detected face with the known face encodings stored in the known_face_encodings list. The face_recognition.compare_faces() function is used for this comparison. Distance-based algorithms, such as Euclidean distance or cosine similarity, to measure the similarity between face encodings are used.
- Face Label: If a match is found between the detected face and a known face, the corresponding name from the known_face_names list is displayed on the video frame. If no match is found, the name is displayed as "unknown".
- Output Video: The processed video frame with the face labels is displayed in a window using cv2.imshow().

## Installation
### Requirements
Python 3.3+ or Python 2.7 <br>
macOS or Linux (Windows not officially supported, but might work) <br>
<br>
Installation Options: <br>
Installing on Mac or Linux <br>

## Dependencies

- cv2 (OpenCV)
- Numpy
- face_recognition

### Face-Recognition Library's Installation can be found here <br>
[face_recognition](https://github.com/ageitgey/face_recognition) by ageitgey.

-------------------------------------
## Run the File

Clone the Repository <br>
`git clone https://github.com/siripiripiri/cv2-multi-face-recognition.git`

Go to the cloned directory <br>
`cd cv2-multi-face-recognition`

Install dependencies <br>
`pip install numpy` <br>
`pip install opencv-python` <br>
`pip install face_recognition`  <br>

### To compile and Run the python file, run: <br>

`python face.py` OR <br>
`python3 face.py`


## Results Analysis

- The face recognition system implemented in this code is able to accurately identify and label the known individuals in real-time. The use of the Face Recognition library provides a robust and efficient face recognition algorithm, which can handle variations in lighting, angle, and occlusion to a certain extent.
- The accuracy of the system depends on the quality and diversity of the training data (the images of Srijan and his friends) as well as the performance of the underlying face detection and recognition algorithms.


## Use Cases
- Security and Surveillance: The system can be used to identify and track individuals in security camera footage, improving the effectiveness of surveillance systems.
- Human-Computer Interaction: The system can be used to identify users and personalize their experiences in applications like smart home systems, personal assistants, or gaming platforms.
- Attendance Tracking: The system can be used to automate attendance tracking in educational institutions or workplaces, replacing traditional manual sign-in/sign-out processes.
- Customer Engagement: The system can be used in retail or hospitality settings to recognize and greet regular customers, improving the overall customer experience.



## Conclusions
- The code demonstrates the use of OpenCV and the Face Recognition library to develop a real-time face recognition system.
- The system is able to accurately identify known individuals in a live video feed.
- The use of face detection, face encoding, and face comparison algorithms provides a robust and efficient face recognition solution.
- The system has various potential use cases, including security, human-computer interaction, attendance tracking, and customer engagement.
- The accuracy and performance of the system can be further improved by expanding the training dataset, fine-tuning the algorithms, and optimizing the code for better computational efficiency.


