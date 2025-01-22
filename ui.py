import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from password_checker import check_password_strength, generate_password, check_pwned_password

def check_password():
    password=entry.get()
    strength, feedback=check_password_strength(password)

    try:
        if check_pwned_password(password):
            feedback.append("This password has been compromised. Avoid using it!")
    except Exception as e:
        feedback.append("Error checking against Have I Been Pwned API.")

    result_label.config(text=f"Strength: {strength}", style="success.TLabel" if strength=="Strong" else "danger.TLabel")
    feedback_label.config(text="\n".join(feedback) if feedback else "Your password is strong!")

def generate_password_ui():
    password=generate_password(12)
    entry.delete(0, ttk.END)
    entry.insert(0, password)
    check_password()

def toggle_password_visibility():
    if show_password_var.get():
        entry.config(show="")
    else:
        entry.config(show="*")

def clear_fields():
    entry.delete(0, ttk.END)
    result_label.config(text="")
    feedback_label.config(text="")
    show_password_var.set(0)
    entry.config(show="*")

app=ttk.Window(themename="superhero")
app.title("Password Strength Checker")
app.geometry("500x400")

title_label=ttk.Label(app, text="Password Strength Checker", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

entry=ttk.Entry(app, width=30, show="*", font=("Arial", 12))
entry.pack(pady=10)

show_password_var=ttk.IntVar()
show_password_check=ttk.Checkbutton(app, text="Show Password", variable=show_password_var, command=toggle_password_visibility)
show_password_check.pack(pady=5)

button_frame=ttk.Frame(app)
button_frame.pack(pady=5)

check_button=ttk.Button(button_frame, text="Check Strength", command=check_password, bootstyle=PRIMARY)
check_button.grid(row=0, column=0, padx=5)

generate_button=ttk.Button(button_frame, text="Generate Password", command=generate_password_ui, bootstyle=INFO)
generate_button.grid(row=0, column=1, padx=5)

clear_button=ttk.Button(button_frame, text="Clear", command=clear_fields, bootstyle=SECONDARY)
clear_button.grid(row=0, column=2, padx=5)

result_label=ttk.Label(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

feedback_label=ttk.Label(app, text="", font=("Arial", 12), wraplength=450, justify="center")
feedback_label.pack(pady=10)

app.mainloop()
