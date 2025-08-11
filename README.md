# Ecommerce Backend

This is the backend of an ecommerce application built with **Django**.  
It handles products, categories, user authentication, cart, and checkout features.  
The project is deployed on [PythonAnywhere](https://ecommerce112.pythonanywhere.com/).

---

## 🚀 Features
- User authentication (login, signup, logout)
- Product management
- Shopping cart
- Order checkout
- Media upload support
- Admin dashboard

---

## 🛠 Tech Stack
- **Python** 3.13
- **Django** 5.2.4
- **SQLite** (Development) / PythonAnywhere hosting
- **HTML, CSS, JavaScript** for frontend templates

---

## 📂 Project Structure
ecommerceBackend/
│
├── store/ # Main app for products, cart, orders
├── ecommerce/ # Django project settings
├── templates/ # HTML templates
├── static/ # CSS, JS, Images
├── media/ # Uploaded media files
├── venv/ # Virtual environment
└── manage.py # Django management script

yaml


---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/ecommerceBackend.git
cd ecommerceBackend
Create and activate a virtual environment


python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Install dependencies


pip install -r requirements.txt
Run migrations


python manage.py migrate
Create a superuser


python manage.py createsuperuser
Collect static files


python manage.py collectstatic
Run the development server


python manage.py runserver


Also here is the admin Logins:
Username : Owner
Password : Owner1122
