# -Simple-Reminder-App-Python-Tkinter-
A lightweight and user-friendly desktop reminder application built with Python. It allows users to schedule time-based reminders and receive native system notifications at the exact time they set. This project is ideal for beginners exploring GUI development, threading, and desktop notifications in Python.

🚀 Key Features

Clean and Simple GUI using Tkinter

Time-based reminders in HH:MM format

Native OS notifications powered by plyer

Background monitoring thread (non-blocking)

Instant validation and feedback using Tkinter dialogs

Lightweight, portable, and easy to run

📂 Project Structure
reminder app.py     # Main application file

📦 Requirements

Python 3.8+

Python libraries:

tkinter (pre-installed with most Python distributions)

plyer (for desktop notifications)

Install missing dependencies:

pip install plyer

🛠️ Installation & Running

Clone or download the project, then simply run:

python "reminder app.py"


The graphical interface will open automatically.

📝 How It Works

Enter a time in HH:MM format (24-hour format).

Enter the reminder message you want to receive.

Click “Add Reminder”.

A background thread continuously checks the current time.

When the system time matches a saved reminder, a desktop notification appears instantly.

📘 Example

Time:

14:30


Reminder text:

Take a short break!


When the clock hits 14:30, the system shows a native notification:

Title: Reminder!
Message: Take a short break!

🧠 Technical Highlights

Threading:
Uses a daemon thread to check reminders every 30 seconds without freezing the GUI.

Tkinter GUI:
Simple and intuitive interface with labels, input fields, and a button.

Cross-Platform Notifications:
The plyer.notification module supports Windows, macOS, and Linux.

📝 Future Improvements (Optional)

These are ideas you could add to the project later:

Save reminders in a file (JSON/SQLite)

Allow date-based reminders

Add editing/deleting reminders

Add sound alerts

Improve UI layout with custom themes

📄 License

You may use this project freely.
(Consider adding an MIT License if publishing publicly.)
