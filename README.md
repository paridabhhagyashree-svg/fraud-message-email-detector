🛡️ Fraud Message / Email Detector

An AI-powered web application that detects fraudulent, spam, phishing, and scam messages using Machine Learning, Natural Language Processing (NLP), and Flask.

This project was developed as part of the IFIM School of Technology AI Club Summer Projects 2026.

---

Project Overview

Fraudulent SMS messages, phishing emails, and scam communications have become increasingly common. Many users unknowingly click malicious links or share confidential information after receiving deceptive messages.

The Fraud Message / Email Detector addresses this problem by using a trained Machine Learning model to classify text messages as Spam or Not Spam. The system provides users with an easy-to-use web interface where they can paste a message and instantly receive a prediction.

---

Objectives

- Detect spam and fraudulent messages using Artificial Intelligence.
- Classify incoming messages as Spam or Not Spam.
- Build an interactive web application using Flask.
- Demonstrate the practical application of Machine Learning and NLP.
- Improve awareness regarding phishing and online scams.

---

Features

- Spam Message Detection
- Fraud Message Classification
- Machine Learning Prediction
- Natural Language Processing
- Interactive Flask Web Application
- Responsive User Interface
- Fast Prediction
- Simple and Easy-to-use Interface
- Git Version Control
- GitHub Repository Integration

---

Technologies Used

Programming Language

- Python 3

Machine Learning

- Scikit-learn
- Multinomial Naive Bayes

Natural Language Processing

- CountVectorizer
- Text Cleaning
- Tokenization

Web Framework

- Flask

Frontend

- HTML5
- CSS3
- JavaScript

Libraries

- Pandas
- Joblib
- NumPy

Development Tools

- Visual Studio Code
- Git
- GitHub

---

Project Structure

fraud-message-email-detector/

│── data/
│     └── SMSSpamCollection

│── static/
│     ├── style.css
│     └── script.js

│── templates/
│     ├── layout.html
│     ├── index.html
│     ├── about.html
│     ├── features.html
│     └── contact.html

│── model.pkl
│── vectorizer.pkl
│── train_model.py
│── main.py
│── README.md

---

Machine Learning Workflow

1. Collect SMS Spam Dataset.
2. Clean and preprocess text.
3. Convert text into numerical features using CountVectorizer.
4. Train the Machine Learning model.
5. Save the trained model using Joblib.
6. Load the model in Flask.
7. Predict whether a message is Spam or Not Spam.
8. Display the prediction on the website.

---

Dataset

Dataset Used:

SMS Spam Collection Dataset

The dataset contains thousands of SMS messages labelled as:

- Ham (Legitimate Message)
- Spam (Fraudulent Message)

---

Installation

Clone the repository

git clone https://github.com/paridabhagyashree-svg/fraud-message-email-detector.git
Navigate into the project directory

cd fraud-message-email-detector

Install dependencies

pip install -r requirements.txt

Run the application

python main.py

Open the browser

http://127.0.0.1:5000

---

How to Use

1. Open the web application.
2. Paste an SMS or email into the text box.
3. Click the Detect Message button.
4. The model analyses the message.
5. The application displays:

- 🚨 Spam Message
- ✅ Safe Message (Not Spam)

---

Sample Messages

Spam

Congratulations! You have won ₹50,000. Click the link below to claim your reward.

Safe

Hi, are we meeting tomorrow at 10 AM for the project discussion?

---

Future Enhancements

- Deep Learning based classification
- BERT Transformer Model
- Email Attachment Analysis
- URL Detection
- Multi-language Support
- Real-time Email Scanning
- Browser Extension
- Mobile Application
- User Authentication
- Cloud Deployment

---

Learning Outcomes

Through this project, I gained practical experience in:

- Machine Learning
- Natural Language Processing
- Flask Web Development
- Python Programming
- Git & GitHub
- Model Deployment
- Web Application Development
- Project Documentation

---

Author

Bhagyashree Parida

Bachelor of Computer Applications (BCA)

IFIM School of Technology

Batch: 2024–2027

---

Acknowledgements

I sincerely thank the AI Club Faculty Advisors and IFIM School of Technology for their guidance, encouragement, and support throughout this project. I also acknowledge the open-source community and publicly available datasets that made this project possible.

---

License

This project is developed for educational and academic purposes under the IFIM School of Technology AI Club Summer Project 2026.