## 🔔 Reminder App

This is a simple desktop reminder application built using Python's **`tkinter`** for the GUI and the **`plyer`** library for native system notifications.

### ✨ Features

* **GUI Interface:** Easy-to-use graphical interface for setting reminders.
* **Time-Based Reminders:** Set reminders for a specific time of the day (in HH:MM format).
* **System Notifications:** Uses native desktop notifications via the `plyer` library to alert the user.
* **Non-Blocking:** Reminder checking runs in a separate thread (`threading`) so the main application GUI remains responsive.
* **Simple Setup:** Minimal dependencies and straightforward code structure.

### ⚙️ Requirements

To run this application, you need to have Python installed, along with the `tkinter` (usually bundled with Python) and the `plyer` library.

1.  **Python:** (3.x recommended)
2.  **Required Libraries:**
    * `plyer`
    * `tkinter` (standard library)

### 💻 Installation and Setup

Follow these steps to set up and run the application:

#### 1. Install Dependencies

You only need to install the `plyer` library using `pip`:

📝 Usage
Start the App: Run the Python script. A simple window will appear.

Enter Time: In the "Time (HH:MM):" field, enter the time you want the reminder to trigger, using a 24-hour format (e.g., 14:30 for 2:30 PM).

Enter Reminder Text: In the "Reminder Text:" field, enter the message you want to see (e.g., Take a break or Meeting with team).

Add Reminder: Click the "افزودن یادآوری" (Add Reminder) button. A success message will confirm the reminder has been saved.

Notification: At the specified time, a desktop notification will pop up with your reminder text. The application checks for new reminders every 30 seconds.

🔍 Code Breakdown
The core functionality is handled by three main components:

🛑 Important Notes
Time Format: The time must be entered in the HH:MM 24-hour format.

Persistence: The reminders are not saved to a file (like a database or JSON). They only exist for the duration of the application session. Once you close the app, all current reminders will be lost.

Threading: The check_reminders function is run as a daemon thread, meaning the thread will automatically terminate when the main application window is closed.

🚀 Future Enhancements
Add functionality to display and delete existing reminders.

Implement data persistence (e.g., using a JSON file or SQLite) to save reminders across sessions.

Allow reminders to be set for a specific date, not just a time.

Improve time format validation and error handling.

Add a feature to set repeating or recurring reminders.

🤝 Contributing
Feel free to fork this repository and submit pull requests with any improvements or new features!

📄 License
This project is open-source.

```bash
pip install plyer
