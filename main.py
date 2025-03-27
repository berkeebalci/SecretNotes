import tkinter as tk
from PIL import Image, ImageTk

#window
window = tk.Tk()
window.title("Secret Notes")
window.geometry("400x550")

#image
image = Image.open("topsecret.png")
image = image.resize((100, 100), Image.Resampling.LANCZOS)

tk_image = ImageTk.PhotoImage(image)   # from pillow to tkinter

image_label = tk.Label(window, image=tk_image)
image_label.pack()

window.tk_image = tk_image

enter_your_title = tk.Label(text="Enter your title")
enter_your_title.pack()

entry_title = tk.Entry(bg="white",width=15)
entry_title.pack()

secret = tk.Label(text="Enter your secret")
secret.pack()

entry_secret = tk.Entry(width=20,bg="white")
entry_secret.pack(pady=10,ipady=70)

master_key = tk.Label(text="Enter master key")
master_key.pack()

entry_master_key = tk.Entry(bg="white")
entry_master_key.pack()

encrypt_button = tk.Button(text="Save & Encrypt" ,font="Arial")
encrypt_button.pack()

decrypt_button = tk.Button(text="Decrypt")
decrypt_button.pack()





window.mainloop()

