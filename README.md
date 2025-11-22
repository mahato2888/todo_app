Todo List Fullstack App
A simple Todo List web app built with Django (backend) and React (frontend).
Add, view, edit, and delete tasks with status and optional due date.

Features
Add tasks with status (pending/done)

Edit and delete tasks

Optional due date for each task

Attractive, responsive frontend UI

How to Run Locally
Clone this repo

text
git clone https://github.com/yourusername/todo-fullstack.git
Backend setup

text
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Frontend setup

text
cd ../frontend
npm install
npm start
Open http://localhost:3000 in your browser.

Folder Structure
text
backend/    # Django REST API
frontend/   # React UI
