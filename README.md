# 🔒 Secure Biometric Age Verification System

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Machine_Learning-FF6F00)

## 📌 Project Overview
This project is an offline-first, biometric access control portal powered by a Convolutional Neural Network (CNN). It acts as a security gateway, utilizing Deep Learning and Facial Recognition principles to predict a user's age demographic (Child, Teenager, or Adult) from a 2D facial photograph and grant or deny access accordingly.

This system was specifically architected to run completely locally for academic defense presentations, ensuring zero reliance on active internet connections during demonstrations.

## 🚀 Key Features
* **Secure Authentication Gateway:** A hardcoded, offline login barrier protecting the biometric scanner.
* **Biometric Preprocessing:** Automated image resizing (224x224) and mathematical array normalization.
* **Deep Learning Engine:** Utilizes Transfer Learning via the `MobileNetV2` architecture to extract facial features and classify demographics.
* **Real-Time UI:** A minimalist, highly responsive front-end dashboard built with Streamlit.

## 🛠️ Technology Stack
* **Front-End / UI:** Streamlit
* **AI / Machine Learning:** TensorFlow, Keras
* **Image Processing:** Pillow (PIL), NumPy

## 📂 Project Structure
```text
Age_Classification_Project/
│
├── app.py                 # The Streamlit front-end and access gateway
├── train.py               # The script used to train the CNN in Google Colab
├── model.h5               # The pre-trained AI brain (Weights & Biases)
├── requirements.txt       # Dependencies for cloud deployment
└── Dataset/               # The raw training data (Adult, Child, Teenager)


💻 How to Run Locally
1. Clone the repository

Bash
git clone [https://github.com/biggmanuel/AGE-GROUP-CLASSIFICATION-FROM-FACIAL-IMAGES.git](github.com/biggmanuel/AGE-GROUP-CLASSIFICATION-FROM-FACIAL-IMAGES.git)
cd AGE-GROUP-CLASSIFICATION-FROM-FACIAL-IMAGES
2. Install Dependencies
Ensure you have Python installed, then run:

Bash
pip install -r requirements.txt
3. Launch the Application

Bash
python -m streamlit run app.py
(The system will open automatically in your default web browser at http://localhost:8501)

🔑 Demo Credentials
To bypass the initial security gateway during testing, use the following local credentials:

Username: admin

Password: unical2026

🧠 Model Training details
The AI model (model.h5) was trained using a custom dataset of faces categorized into three distinct folders. Due to local hardware constraints, the model was trained using Google Colab's cloud infrastructure, achieving high validation accuracy over 10 epochs before being exported for offline local deployment.
