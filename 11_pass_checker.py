import tkinter as tk
from tkinter import messagebox
import re

def check_strength(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([bool(length), bool(upper), bool(lower), bool(digit), bool(special)])

    if score <= 2:
        return "❌ Weak", "red"
    elif score == 3 or score == 4:
        return "⚠️ Moderate", "orange"
    else:
        return "✅ Strong", "green"
def analyze():
    pwd = password_entry.get()
    if not pwd:
        messagebox.showwarning("Empty Field", "Please enter a password.")
        return

    result, color = check_strength(pwd)
    result_label.config(text=f"Password Strength: {result}", fg=color)

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
password_entry.pack()

tk.Button(root, text="Check Strength", command=analyze, font=("Arial", 12), bg="#3498db", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
