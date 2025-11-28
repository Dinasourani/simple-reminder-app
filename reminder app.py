import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from plyer import notification
import threading
import time


# تابعی برای بررسی زمان و نمایش یادآوری
def check_reminders():
    while True:
        now = datetime.now().strftime("%H:%M")
        for reminder_time, reminder_text in reminders.items():
            if now == reminder_time:
                notification.notify(
                    title="یادآوری!",
                    message=reminder_text,
                    timeout=10
                )
        time.sleep(30)  # هر 30 ثانیه چک می‌کنه


# تابع افزودن یادآوری جدید
def add_reminder():
    time_input = time_entry.get()
    text_input = text_entry.get()

    if time_input and text_input:
        reminders[time_input] = text_input
        messagebox.showinfo("موفقیت", f"یادآوری اضافه شد: {time_input} - {text_input}")
        time_entry.delete(0, tk.END)
        text_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("خطا", "لطفاً زمان و متن یادآوری را وارد کنید!")


# ساخت رابط کاربری
root = tk.Tk()
root.title("برنامه یادآور ساده")
root.geometry("400x200")

reminders = {}

tk.Label(root, text="زمان (HH:MM):").pack(pady=5)
time_entry = tk.Entry(root)
time_entry.pack(pady=5)

tk.Label(root, text="متن یادآوری:").pack(pady=5)
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=5)

tk.Button(root, text="افزودن یادآوری", command=add_reminder).pack(pady=20)

# اجرای بررسی یادآوری در یک Thread جداگانه
threading.Thread(target=check_reminders, daemon=True).start()

root.mainloop()