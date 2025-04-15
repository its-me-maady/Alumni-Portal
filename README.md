# Alumni Portal

A web application for managing alumni connections and events, built with Flask.

## Features

-   Dual login system for administrators and alumni
-   Alumni profile management
-   Event creation and management
-   Alumni search with multiple filters
-   Bulk user management
-   Real-time event registration tracking
-   Responsive design for all devices

## Tech Stack

-   Backend: Flask with SQLAlchemy
-   Frontend: HTML, CSS, JavaScript
-   Database: PostgreSQL/SQLite
-   Authentication: Flask-Login
-   Forms: Flask-WTF
-   Password Hashing: Flask-Bcrypt

## Project Structure

```
Alumni-portal-scratch/
├── app/
│   ├── Blueprints/
│   │   ├── admin/
│   │   └── user/
│   ├── models.py
│   ├── forms.py
│   ├── utils.py
│   ├── static/
│   └── __init__.py
├── config.py
├── run.py
├── requirements.txt
└── .env
```

## Setup Instructions

1. Clone the repository:

```bash
git clone <repository-url>
cd Alumni-portal-scratch
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables in `.env`:

```
DATABASEURI="sqlite:///current.db"
SECRET_KEY="your-secret-key"
```

5. Initialize the database:

```bash
flask db init
flask db migrate
flask db upgrade
```

6. Run the application:

```bash
flask run
```

## Usage

### Admin Features

-   Create/manage events
-   Approve/reject alumni registrations
-   Search and filter alumni
-   Bulk user management
-   View event participation statistics

### Alumni Features

-   Register and create profile
-   Update personal information
-   View and register for events
-   Track event participation

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

-   Flask documentation and community
-   Bootstrap for responsive design
-   Font Awesome for icons
