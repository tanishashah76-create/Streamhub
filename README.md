# 🎬 StreamHub - Django Movie Streaming Web Application

A full-fledged, modern Movie & Series Streaming platform built with **Django 5** and **Bootstrap 5**, pre-configured for one-click running and debugging in **Visual Studio Code**.

---

## 🚀 Quick Start in VS Code

### Step 1: Open the Project in VS Code
1. Launch **Visual Studio Code**.
2. Go to **File > Open Folder...** (or `Ctrl+K Ctrl+O`).
3. Select this folder:
   ```text
   C:\Users\Tanisha shah\.gemini\antigravity\scratch\streamhub
   ```

### Step 2: Run with 1-Click (F5)
- Simply press **`F5`** on your keyboard, or click the **Run and Debug** icon on the left sidebar and click **"Python: Django Run Server"**.
- VS Code will start the server and open the integrated terminal.
- Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### (Alternative) Run via Terminal
Open the VS Code terminal (`Ctrl + \``) and type:
```powershell
python manage.py runserver
```

---

## 🔑 Pre-configured Accounts

The database is already initialized and seeded with sample movies, series, and ready-to-use accounts:

| Role | Username | Password | Notes |
| :--- | :--- | :--- | :--- |
| **Superuser / Admin** | `admin` | `admin1234` | Full access to Django Admin at [`/admin/`](http://127.0.0.1:8000/admin/) |
| **Demo User** | `demo` | `demoPassword123!` | Standard streaming user with watchlist functionality |

---

## 📁 Project Structure

```text
streamhub/
│
├── .vscode/                     # VS Code Configuration
│   ├── launch.json              # F5 Debugger config for Django runserver
│   ├── settings.json            # Template associations and terminal settings
│   └── tasks.json               # Quick tasks (Make Migrations, Migrate, Seed)
│
├── streamhub/                   # Project Settings & Root Routing
│   ├── settings.py              # Configured for templates, static files, auth
│   ├── urls.py                  # Root URL dispatcher
│   ├── wsgi.py                  # WSGI entry point
│   └── asgi.py                  # ASGI entry point
│
├── movies/                      # Core Streaming Application
│   ├── models.py                # Movie and Watchlist database models
│   ├── forms.py                 # MovieForm, RegisterForm, and LoginForm
│   ├── views.py                 # Streaming views & business logic
│   ├── urls.py                  # App routes (/movies/, /series/, /form.html, etc.)
│   ├── admin.py                 # Admin dashboard configuration
│   ├── tests.py                 # Comprehensive unit test suite (8 passing tests)
│   └── management/
│       └── commands/
│           └── seed_movies.py   # Seeder command for movies & series
│
├── static/                      # Static Assets
│   ├── home_page_style.css      # Custom styling from user specification
│   ├── css/
│   │   └── home_page_style.css  # Subdirectory alias
│   └── images/
│       └── logo.svg             # StreamHub vector logo
│
├── templates/                   # HTML Templates
│   ├── base.html                # Master layout with navbar & footer
│   ├── home.html                # Landing page with user HTML & dynamic catalog
│   ├── form.html                # Add movie form (<a href="form.html">)
│   ├── login.html               # Login page (<a href="login.html">)
│   └── movies/
│       ├── home.html            # Exact user HTML integration
│       ├── form.html            # Interactive movie publishing form
│       ├── login.html           # Authentication page
│       ├── register.html        # New user registration
│       ├── movies.html          # Movies catalog with genre & search filters
│       ├── series.html          # Series catalog with genre & search filters
│       ├── movie_detail.html    # Movie page with trailer player & watchlist button
│       └── my_list.html         # Personal user watchlist
│
├── db.sqlite3                   # Initialized and migrated SQLite database
├── manage.py                    # Django management script
└── requirements.txt             # Project dependencies
```

---

## ✨ Key Features Implemented

1. **Exact HTML Integration**:
   - Uses the requested layout with full-bleed background wallpaper, responsive navbar, `#homebtn` smooth scrolling, button transform animations, scroll navbar shadow, and page fade-in effect.
2. **Direct Link Compatibility**:
   - `form.html` in the user's snippet maps cleanly to the Add Movie view.
   - `login.html` in the user's snippet maps cleanly to Django's authentication system.
3. **Database Catalog**:
   - `Movie` model stores title, synopsis, rating, duration, release year, category (Movie/Series), poster URL, and trailer URL.
   - Seeder pre-populates titles like *Inception*, *Interstellar*, *The Dark Knight*, *Stranger Realities*, and more.
4. **Interactive Watchlist ("My List")**:
   - Authenticated users can bookmark movies and manage their watchlist with one click.
5. **Django Admin Dashboard**:
   - Visit [`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/) to manage movies, series, users, and watchlist items.
6. **Search & Filter**:
   - Filter by genre (Action, Sci-Fi, Drama, Thriller, etc.) and search by keywords.

---

## 🧪 Running Automated Tests

To run the automated test suite:
```powershell
python manage.py test
```
Result: **8/8 tests pass** verifying views, models, forms, and template routing.
