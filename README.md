# 📊 OBE Achieve - A CO-PO-PSO Calculation App

A full-stack web application designed to automate the calculation, mapping, and tracking of Course Outcomes (CO), Program Outcomes (PO), and Program Specific Outcomes (PSO). Built with Django, this tool streamlines the Outcome-Based Education (OBE) workflow, making it easier for faculty and academic departments to evaluate curriculum attainment.

## ✨ Features
* **Automated Mapping:** Easily map Course Outcomes to Program Outcomes and PSOs.
* **Attainment Calculation:** Replaces manual spreadsheet work with automated, accurate OBE metric calculations.
* **Admin Dashboard:** A secure Django administration panel for managing courses, academic batches, and mapping logic.
* **Responsive Frontend:** Clean and interactive user interface built with HTML, CSS, and JavaScript.

## 🛠️ Tech Stack
* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, JavaScript
* **Database:** SQLite (default) / MySQL 

## 🚀 Installation and Setup

Follow these steps to run the project locally on your machine.

**1. Clone the repository**
```bash
git clone [https://github.com/Chayapathi077/co-po-pso-calculation.git](https://github.com/Chayapathi077/co-po-pso-calculation.git)
cd co-po-pso-calculation
```

**2. Create a virtual environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install dependencies**
*(If you have a requirements.txt file, run this. Otherwise, just install Django)*
```bash
pip install -r requirements.txt
# or
pip install django
```

**4. Apply database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Start the development server**
```bash
python manage.py runserver
```

## 💻 Usage

* **Main App:** Access the web application at [http://localhost:8000/](http://localhost:8000/) after starting the server.
* **Admin Panel:** Use the admin panel for advanced management. First, create a superuser account:
```bash
  python manage.py createsuperuser
  ```
  Then log in at [http://localhost:8000/admin/](http://localhost:8000/admin/).

## 📸 Screenshots

<img width="3194" height="1753" alt="Screenshot 2025-07-17 202520" src="https://github.com/user-attachments/assets/ff1bbbea-61d2-42e8-aaf0-b598527c0e44" />
<img width="3188" height="1745" alt="Screenshot 2025-07-17 202500" src="https://github.com/user-attachments/assets/c1b24f0b-ec09-439b-a0d3-1a751cb71893" />

## 🤝 Contributing
Contributions are always welcome!
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## 📄 License
© 2026 OBE. All rights reserved.
