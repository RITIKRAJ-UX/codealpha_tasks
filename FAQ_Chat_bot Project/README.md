\# 🤖 FAQ Chatbot – Python Beginner Project



A smart \*\*FAQ Chatbot\*\* built using \*\*Python, NLP, TF-IDF, and Cosine Similarity\*\*.  

This chatbot answers questions related to \*\*Python programming (Beginner to Intermediate level)\*\* and works as:



\- 💻 Command Line Chatbot

\- 🖥️ GUI Desktop Chatbot (Tkinter)

\- 🌐 Web Chatbot (Flask)



This project is suitable for \*\*BCA Mini Project / AI / NLP Lab / Python Project\*\*.



---



\## 📌 Project Objective



The objective of this project is to design and implement an intelligent chatbot that:

\- Understands user questions in natural language

\- Matches them with the most relevant FAQ

\- Returns accurate answers related to Python programming



---



\## 🧠 Technologies Used



\- \*\*Python 3\*\*

\- \*\*Natural Language Processing (NLP)\*\*

\- \*\*TF-IDF Vectorizer\*\*

\- \*\*Cosine Similarity\*\*

\- \*\*Scikit-learn\*\*

\- \*\*Tkinter (GUI)\*\*

\- \*\*Flask (Web Application)\*\*



---



\## 📂 Project Structure



FAQ\_Chat\_bot\_Project/

│

├── faqs.txt # Python beginner FAQ knowledge base

├── faq\_chatbot.py # Command-line chatbot

├── faq\_chatbot\_gui.py # GUI chatbot (Tkinter)

├── app.py # Web chatbot (Flask)

├── README.md # Project documentation



yaml

Copy code



---



\## 📘 Dataset Description



\- \*\*faqs.txt\*\* contains Python beginner questions and answers

\- Covers:

&nbsp; - Python basics

&nbsp; - Data types

&nbsp; - Control statements

&nbsp; - Functions

&nbsp; - OOP concepts

&nbsp; - File handling

&nbsp; - Exception handling

&nbsp; - Libraries and tools



---



\## ⚙️ Installation \& Setup



\### 1️⃣ Install Python Libraries



```bash

pip install nltk scikit-learn flask

2️⃣ (Optional) Download NLTK Resources

python

Copy code

import nltk

nltk.download('stopwords')

▶️ How to Run the Project

🔹 1. Command Line Chatbot

bash

Copy code

python faq\_chatbot.py

Sample Interaction



vbnet

Copy code

You: What is Python?

Bot: Python is a beginner-friendly, high-level programming language.

🔹 2. GUI Chatbot (Tkinter)

bash

Copy code

python faq\_chatbot\_gui.py

✔ Opens a desktop chatbot window

✔ Type questions and receive answers instantly



🔹 3. Web Chatbot (Flask)

bash

Copy code

python app.py

Open browser and visit:



cpp

Copy code

http://127.0.0.1:5000

✔ Web-based chatbot interface

