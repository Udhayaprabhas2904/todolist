# 📝 ToDo Manager

A modern and responsive ToDo Manager web application built using **FastAPI**, **MySQL**, **HTML**, **CSS**, and **JavaScript**. The application allows users to efficiently manage daily tasks through a simple and user-friendly interface.

---

## 🚀 Features

- ➕ Create new tasks
- 📋 View all tasks
- ✏️ Update existing tasks
- 🗑️ Delete individual tasks
- ❌ Delete all tasks
- ✅ Mark all tasks as completed
- 📌 Separate Pending and Completed task sections
- ⏰ Reminder date and time support
- 🎨 Responsive and modern user interface
- 📖 Interactive API documentation using Swagger UI

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- SQLAlchemy

### Database
- MySQL

### Frontend
- HTML5
- CSS3
- JavaScript
- Font Awesome

### Tools
- Git
- GitHub
- VS Code

---

## 📂 Project Structure

```text
todolist/
│── static/
│   ├── style.css
│   ├── script.js
│
│── templates/
│   └── index.html
│
│── database.py
│── model.py
│── schema.py
│── main.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Udhayaprabhas2904/todolist.git
```

### Navigate to the project

```bash
cd todolist
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
uvicorn main:app --reload
```

---

## 🌐 Application URLs

**Frontend**

```
http://127.0.0.1:8000/frontend
```

**Swagger API Documentation**

```
http://127.0.0.1:8000/docs
```

**Health Check**

```
http://127.0.0.1:8000/health
```

---

## 👨‍💻 Author

**Udhayaprabha S**


---

## 📄 License

This project is created for learning and educational purposes.
