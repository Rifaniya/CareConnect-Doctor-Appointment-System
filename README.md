CareConnect — Doctor Appointment Booking System

CareConnect is a web application developed using Django that allows users to browse doctors, filter available doctors, book appointments, and manage their bookings.

Features

- User registration, login, and logout
- Browse doctors and view their details
- Search and filter doctors by specialization
- Book appointments with doctors
- View personal appointments
- Cancel pending appointments
- Validate appointment dates and prevent duplicate active bookings
- Admin interface for managing doctors and appointments
- User-specific appointment privacy

Technologies Used

- Backend: Python, Django
- Frontend: HTML, CSS
- Database: SQLite
- Tools: Visual Studio Code, Git, GitHub

Installation and Setup

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER

Replace the placeholders with your actual repository URL and folder name.

2. Create and activate a virtual environment

On macOS or Linux:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

python3 -m pip install django

If you create a "requirements.txt" file, you can install all project dependencies with:

python3 -m pip install -r requirements.txt

4. Apply database migrations

python3 manage.py migrate

5. Create an administrator account

python3 manage.py createsuperuser

Follow the prompts to set up your administrator account.

6. Run the development server

python3 manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

Project Status

Core features and initial functional tests are complete. Further improvements may include doctor availability schedules, appointment confirmation workflows, automated tests, and deployment.

Future Improvements

- Doctor working hours and availability management
- Appointment reminders
- Improved accessibility and responsive design
- Automated unit and integration tests
- Deployment to a production hosting platform

Author

Developed as a learning project to practise Python, Django, database integration, and web development.