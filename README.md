# ToDo Manager

A modern and responsive ToDo Manager web application built using **FastAPI**, **MySQL**, **HTML**, **CSS**, and **JavaScript**. The application allows users to efficiently manage daily tasks through a simple and user-friendly interface.

---

## Features

- Create new tasks
- View all tasks
- Update existing tasks
- Delete individual tasks
- Delete all tasks
- Mark all tasks as completed
- Separate Pending and Completed task sections
- Reminder date and time support
- Responsive and modern user interface
- Interactive API documentation using Swagger UI

---

## Tech Stack

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

## Project Structure

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

## Installation

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

## Application URLs with Screenshots

**Frontend**

```
http://127.0.0.1:8000/frontend

<img width="1867" height="871" alt="image" src="https://github.com/user-attachments/assets/20fe9b1e-15b6-4860-a148-5691003ec770" />
<img width="1899" height="851" alt="image" src="https://github.com/user-attachments/assets/fb935f4e-bf77-442a-b1b4-2cb74c733077" />



```

**Swagger API Documentation**

```
http://127.0.0.1:8000/docs

<img width="1884" height="759" alt="image" src="https://github.com/user-attachments/assets/262e5523-5a59-4ca2-b7fb-2b6329b47d61" />
<img width="1873" height="423" alt="image" src="https://github.com/user-attachments/assets/22dfecb0-bc72-4bd2-bd9c-6a9ec2b1da4b" />


```

**Health Check**

```
http://127.0.0.1:8000/health

<img width="1791" height="424" alt="image" src="https://github.com/user-attachments/assets/bd2aaf3b-2382-4484-be22-e487e45bd9bd" />

```

---

## Author

**Udhayaprabha S**

---

## License

This project is created for learning and educational purposes.
