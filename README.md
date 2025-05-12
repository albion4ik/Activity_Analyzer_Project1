# 🎓 AI Student Activity Analyzer

This is a full-stack AI web application developed for the **AI Final Project (Spring 2025)** at **IITU**. The system allows students to track their daily activity and receive intelligent insights based on multiple AI techniques.

---

## 📌 Project Goals

- Analyze student activity patterns.
- Predict and classify behavior using supervised AI.
- Cluster similar behavior types using unsupervised learning.
- Detect objects from user-uploaded images using computer vision.

---

## ✅ Project Features

| Task | Description |
|------|-------------|
| **Task A** | Implements 8 Supervised Learning Algorithms |
| **Task B** | Implements 3 Unsupervised Learning Algorithms |
| **Task C** | Includes a Computer Vision algorithm for image recognition |

---

## 🧠 Supervised Learning (Task A)

The following algorithms are implemented from scratch:

- Linear Regression
- Logistic Regression
- Decision Tree
- Random Forest
- Naive Bayes
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Gradient Boosting

Each algorithm makes predictions based on a training set of labeled activities and returns both a **prediction** and its **accuracy**.

---

## 🧪 Unsupervised Learning (Task B)

Implemented algorithms:

- **KMeans** — clusters student behavior patterns
- **PCA** — dimensionality reduction of activity features
- **FP-Growth** — discovers activity association rules (e.g., “Studying → Reading”)

---

## 🖼 Computer Vision (Task C)

Users can upload an image and the system uses a custom CV model (stubbed with `object_detection.py`) to detect and label the object.

---

## 🚀 How to Run the Project

1. Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/ai-student-analyzer.git
cd ai-student-analyzer
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

4. Open your browser at:
```
http://localhost:5000
```

---

## 📁 Project Structure

```
ai-student-analyzer/
│
├── ai_modules/               # All 12 AI algorithms (Task A, B, C)
├── static/
│   ├── style.css             # Lavender-pink theme
│   └── uploads/              # Uploaded images (Task C)
├── templates/
│   └── index.html            # Web interface
├── app.py                    # Flask backend logic
├── requirements.txt
└── README.md                 # This file
```

---



*(Add screenshots of your app here during testing and UI demo)*

---

## 📚 License

This project is for educational purposes as part of IITU's Spring 2025 AI course.
