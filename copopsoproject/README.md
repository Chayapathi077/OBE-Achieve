# CopOpsO Project

A Django-based web application deployed on Vercel.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- MySQL 5.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd copopsoproject
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory and add:
```
DJANGO_SECRET_KEY=your_secret_key_here
DJANGO_DEBUG=True
DB_NAME=s3p
DB_USER=root
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=3306
```

5. Database setup:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

Visit http://localhost:8000 to see the application.

## 🏗️ Project Structure

```
copopsoproject/
├── copopsoproject/      # Main project directory
│   ├── settings.py      # Project settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py         # WSGI configuration
├── website/             # Main application
├── static/             # Static files (CSS, JS, images)
├── media/              # User-uploaded files
├── templates/          # HTML templates
├── manage.py           # Django management script
├── requirements.txt    # Project dependencies
└── vercel.json        # Vercel deployment configuration
```

## 🚀 Deployment

This project is configured for deployment on Vercel:

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Deploy to Vercel:
```bash
vercel
```

3. Configure environment variables in Vercel dashboard:
   - DJANGO_SECRET_KEY
   - DJANGO_DEBUG
   - Database credentials

## 🛠️ Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [MySQL](https://www.mysql.com/) - Database
- [Vercel](https://vercel.com/) - Deployment platform

## 📝 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| DJANGO_SECRET_KEY | Django secret key | Generated secure key |
| DJANGO_DEBUG | Debug mode | False in production |
| DB_NAME | Database name | s3p |
| DB_USER | Database user | root |
| DB_PASSWORD | Database password | - |
| DB_HOST | Database host | localhost |
| DB_PORT | Database port | 3306 |

## 🔒 Security Notes

1. Never commit `.env` files or sensitive credentials
2. Keep `DEBUG=False` in production
3. Regularly update dependencies
4. Use strong, unique passwords
5. Configure proper CORS settings if needed

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request 