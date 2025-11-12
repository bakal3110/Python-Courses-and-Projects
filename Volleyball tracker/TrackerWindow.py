import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

app = ctk.CTk()
app.geometry("600x500")
app.title("CTk example")

image = Image.open("pictures/field.jpg")  # Replace with your image path
image_ctk = ctk.CTkImage(light_image=image, dark_image=image, size=(612, 408))

# Define the function to be called on click
def on_image_click():
    messagebox.showinfo("Image Clicked", "You clicked the image!")

# Create a button with the image
image_button = ctk.CTkButton(master=app, image=image_ctk, text="", command=on_image_click)
image_button.pack(pady=20)

app.mainloop()
