import customtkinter as ctk

ctk.set_appearance_mode("System")  # "Light", "Dark", or "System"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("Volleyball Stats")
app.geometry("300x200")

def greet():
    name = entry.get()
    label.configure(text=f"Hello, {name or 'User'}")

entry = ctk.CTkEntry(app, placeholder_text="Enter your name")
entry.pack(pady=10)

button = ctk.CTkButton(app, text="Greet", command=greet)
button.pack(pady=5)

label = ctk.CTkLabel(app, text="text")
label.pack(pady=5)

app.mainloop()
