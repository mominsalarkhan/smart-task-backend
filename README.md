# smart-task-scheduler/README.md

# 🧠 Smart Task Scheduler (AI-Enhanced To-Do App)

A full-stack to-do app that uses a simple machine learning model to automatically prioritize your tasks based on urgency. Built with Python, Flask, and vanilla JS.

---

## 🚀 Features
- Add tasks with natural language descriptions (e.g. "Submit report tomorrow")
- AI-based priority prediction (Low / Medium / High)
- View tasks sorted by predicted priority
- Lightweight, responsive UI (HTML + CSS + JS)

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **ML:** Scikit-learn
- **Frontend:** HTML, CSS, JavaScript
- **Data:** CSV-based sample task set (can be expanded to SQLite/Postgres)

---

## 📁 Folder Structure
```
smart-task-scheduler/
├── backend/
│   ├── app.py
│   ├── model.py
│   ├── scheduler.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── styles.css
├── data/
│   └── sample_tasks.csv
├── README.md
└── .gitignore
```

---

## 📦 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/smart-task-scheduler
cd smart-task-scheduler
```

### 2. Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### 3. Frontend
Simply open `frontend/index.html` in your browser (or run with Live Server extension).

---

## 📊 Sample Input
```
Task: Finish project report by tonight
Predicted Priority: High
```

---

## 📌 Future Ideas
- Login/authentication system
- Persistent task storage (SQLite/PostgreSQL)
- Deadline reminders
- React frontend version

---

## 📄 License
MIT
