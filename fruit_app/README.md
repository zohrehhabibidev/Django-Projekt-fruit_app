# Mini Fruits API 🍎

A small Django REST-style backend project created for learning the basics of Backend development with Django.

## 📌 About the Project

This project provides a simple API that returns information about five fruits.

Each fruit contains:

- `name`
- `color`
- `weight`

The Backend is built with **Python** and **Django** and returns the fruit data as a JSON response.

## 🛠️ Technologies

- Python
- Django
- django-cors-headers
- JSON
- HTTP
- Git / GitHub

## 📂 Project Structure

Django-Projekt fruit_app/
├── core/
│ ├── settings.py
│ └── urls.py
│
├── fruit_app/
│ ├── views.py
│ └── urls.py
│
├── manage.py
└── requirements.txt

## 🚀 API Endpoint

The main endpoint is:

GET /fruits/

Example:

http://127.0.0.1:8000/fruits/

The API returns JSON in the following structure:

{
"fruits": [
{
"name": "Apple",
"color": "Red",
"weight": 150
},
{
"name": "Banana",
"color": "Yellow",
"weight": 120
}
]
}

## 🌐 Frontend

This Backend is connected to a separate Frontend project.

The Frontend uses **JavaScript `fetch()`** to request the data from the Django Backend and displays the fruits in the browser.

The Frontend code was provided by the following repository:

[BE-mini_fruits_api_frontend](https://github.com/Developer-Akademie-AA/BE-mini_fruits_api_frontend/tree/main?utm_source=chatgpt.com)

## 🔐 CORS

Because the Frontend and Backend run on different origins during development, **CORS (Cross-Origin Resource Sharing)** is configured using `django-cors-headers`.

The development Frontend origin is allowed to access the Django API.

## ▶️ How to Run

### 1. Activate the virtual environment

.venv\Scripts\activate

### 2. Install dependencies

pip install -r requirements.txt

### 3. Start the Django development server

python manage.py runserver

The Backend will be available at:

http://127.0.0.1:8000/

### 4. Test the API

Open:

http://127.0.0.1:8000/fruits/

You should receive the fruit data as JSON.

## 🎯 Learning Goals

This project was created to practice the following Backend concepts:

- Django project and app structure
- Django `views`
- URL routing with `path()`
- `include()`
- HTTP requests and responses
- JSON responses
- Django `JsonResponse`
- CORS
- Connecting a JavaScript Frontend to a Django Backend
- Using `fetch()` to communicate with an API
- Basic Git workflow

## 📚 Project Context

This project is part of my Backend development learning journey and focuses on understanding how a Backend provides data to a Frontend through an HTTP API.
