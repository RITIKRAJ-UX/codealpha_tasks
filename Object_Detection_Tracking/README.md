Object Detection and Tracking using YOLO \& OpenCV

📌 Project Overview



This project demonstrates real-time object detection and tracking using a pre-trained YOLO (You Only Look Once) model along with OpenCV for video processing. Each detected object is assigned a unique tracking ID using a tracking algorithm (SORT).



This project is suitable for Computer Science students and fulfills the requirements of Object Detection and Tracking tasks.



🧠 Objectives



Capture real-time video using a webcam or video file



Detect objects using a pre-trained YOLO model



Track detected objects across frames



Display bounding boxes with tracking IDs



Show real-time output on screen



🛠️ Technologies Used



Python 3



OpenCV



YOLO (Ultralytics)



NumPy



SORT (Simple Online Realtime Tracking)



📁 Project Structure

Object\_Detection\_Tracking/

│

├── object\_tracking.py     # Main execution file

├── sort.py                # Tracking algorithm

├── README.md              # Project documentation

└── requirements.txt       # Required libraries (optional)



⚙️ Installation \& Setup

1️⃣ Install Python



Make sure Python 3.8 or above is installed.



python --version



2️⃣ Install Required Libraries



Run the following commands in Command Prompt / Terminal:



pip install opencv-python

pip install numpy

pip install ultralytics

pip install filterpy

pip install scipy



▶️ How to Run the Project

Step 1: Open Project Folder

cd Object\_Detection\_Tracking



Step 2: Run the Program

python object\_tracking.py



Step 3: Output



Webcam will start automatically



Objects will be detected and tracked



Each object will have a unique ID



Press Q to stop execution..







Apply YOLO object detection



Extract bounding boxes



Assign tracking IDs using SORT



Display results in real time



🧪 Sample Output



Green bounding boxes around objects



Unique tracking ID displayed on each object



Smooth real-time tracking



🎓 Academic Relevance



Subject: Artificial Intelligence / Computer Vision



Suitable for: BCA, BSc CS, MCA



Concepts covered:



Object Detection



Computer Vision



Machine Learning Models



Real-time Tracking



🚀 Future Enhancements



Implement Deep SORT for better tracking



Save output video to file



Add object count statistics



Deploy as a web application



👨‍💻 Author



Ritik Singh

Object Detection \& Tracking Project



📜 License



This project is for educational purposes only.

