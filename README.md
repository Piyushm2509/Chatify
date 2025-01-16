# Chat Application

This is a simple chat application built using Django and Django Channels to enable real-time WebSocket communication.

## Contents

- **chat_app/**: The main application directory containing all the necessary files.
  - **chat/**: The chat application that handles messaging.
    - **consumers.py**: Contains the WebSocket consumer for handling chat messages.
    - **routing.py**: Defines the WebSocket URL routing.
    - **templates/**: Contains HTML templates for the chat interface.
    - **static/**: Contains static files like CSS.
  - **manage.py**: The command-line utility for managing the Django project.
  - **settings.py**: Configuration settings for the Django project.
  - **asgi.py**: ASGI configuration for handling WebSocket connections.

## How to Run

1. Ensure you have Python and Django installed.
2. Install the required packages:
   ```bash
   pip install django channels
   ```
3. Navigate to the project directory:
   ```bash
   cd chat_app
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```
5. Open your web browser and go to `http://127.0.0.1:8000/` to access the chat application.

## Usage

- Click on a user to start chatting.
- Type your message and hit "Send" to communicate in real-time.

## Note

Make sure to check the browser console for any WebSocket connection errors if you encounter issues.
