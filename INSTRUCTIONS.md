
# Django + MongoDB Blog Project

This project uses **Django** with **MongoEngine** to connect to a **MongoDB** database.
It features a public blog with view counters, and a hidden secure admin dashboard.

## Prerequisites

1.  **Python 3.10+** (Tested with Python 3.12+)
2.  **MongoDB Local Server** running on `localhost:27017`.
    - If you don't have MongoDB installed, download and install valid **MongoDB Community Server**.
    - Ensure the service is running.

## Installation

1.  **Install Dependencies**
    ```bash
    pip install django mongoengine pillow
    ```

2.  **Configuration**
    - The project connects to `mongodb://localhost:27017/blog_db` by default.
    - To change this, edit `core_project/settings.py` (look for `mongoengine.connect`).

## Running the Project

1.  **Start the Server**
    ```bash
    python manage.py runserver
    ```

2.  **Access the Website**
    - Public Home: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Admin Access (Hidden)

1.  **Login URL**
    - [http://127.0.0.1:8000/secure-panel-9090/](http://127.0.0.1:8000/secure-panel-9090/)

2.  **Default Credentials**
    - On the first visit to the login page, a default admin account is created automatically:
    - **Username:** `admin`
    - **Password:** `admin123`

3.  **Dashboard**
    - [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/)
    - You can Add, Edit, and Delete blogs here.
    - View counts are visible in the table.

## Notes
- **Images**: Uploaded images are stored in the `media/` folder and served locally.
- **Database**: Data is stored in MongoDB database `blog_db`, collections `blog_posts` and `admin_users`.
- **SQLite**: SQLite is strictly NOT used. Sessions are file-based.
