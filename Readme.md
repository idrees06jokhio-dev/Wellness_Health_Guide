# 🌿 Wellness Health Guide – Disease Prediction & Remedies (Flask)

## 1) Overview
**Wellness Health Guide** is a lightweight Flask web application designed to:
- **Predict probable diseases** based on four user‑entered symptoms using machine learning.
- **Suggest Ayurvedic remedies** for the predicted condition from a curated CSV dataset.
- **Provide a clean, responsive interface** built with Bootstrap and custom CSS.

---

## 2) How It Works
- On the **Symptoms** page, users enter four symptoms which are sent to the backend.
- The backend trains multiple classifiers (RandomForest, SVC, Logistic Regression) on `Training.csv`, evaluates them against `Testing.csv`, and selects the most accurate model.
- The **predicted disease** is displayed to the user and stored in a local SQLite database.
- On the **Suggester** page, remedies are retrieved from `Remedies.csv` and shown for the selected condition.

---

## 3) Running Locally
**Prerequisite:** Python 3.10 or higher recommended

### a. Create and activate a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### b. Install dependencies
```bash
pip install -r requirements.txt
```

### c. Start the app
```bash
python app.py
```

### d. Open in browser
Navigate to: `http://localhost:3000`

---

## 4) App navigation
- **Home**      → Overview and quick links
- **Symptoms**  → Enter four symptoms for ML prediction
- **Suggester** → View Ayurvedic remedies for a condition
- **About**     → Learn more about the project

---

## 👤 Author
- MUHAMMAD IDREES 2K23/TCS/34 & YUSRA ZENAB 2K23/TCS/51 
