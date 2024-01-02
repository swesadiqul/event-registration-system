# Event Registration System using Django

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

A simple event registration system built with Django, allowing users to create events, register for events, and manage their registrations. The system also includes a user dashboard, admin panel, and API endpoints for listing events, viewing event details, user registration for an event, and retrieving a user's registered events.

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [User Authentication](#user-authentication)
- [Admin Panel](#admin-panel)
- [Search Functionality](#search-functionality)
- [User Dashboard](#user-dashboard)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Installation

### Prerequisites

- Python (>=3.x)
- Django (>=3.x)
- Django Rest Framework

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/event-registration-django.git
    cd event-registration-django
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Features

### 1. Create Events

- Each event has a title, description, date, time, and location name.

### 2. Event Registration

- Registered users can enroll for an event.
- Limit the number of available slots for each event.

### 3. User Registration

- User registration functionality to create accounts using Django's default User model.

### 4. User Authentication

- Only authenticated users can register for events.
- Users can unregister from events they've registered for.

### 5. Admin Panel

- Utilizes Django's admin panel for managing events and user registrations.

### 6. Search Functionality

- Implements a basic search functionality that allows users to search for events based on keywords.

### 7. User Dashboard

- Creates a user dashboard where users can see the events they've registered for and manage their registrations.

### 8. API Endpoints (Using Django Rest Framework)

- List of all events
- Details of a specific event
- User registration for an event
- User's registered events

## User Authentication

- Admin credentials can be created during the superuser creation process.

## License

This project is licensed under the [MIT License](LICENSE).
