import tkinter as tk
from PIL import Image, ImageTk
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

#window
window = tk.Tk()
window.title("Secret Notes")
window.geometry("400x550")



def encrypt_text():
    secret_text = entry_secret.get()
    crypto_master_key = entry_master_key.get()
    header_text = entry_title.get()
    encrypted_text = cipher_suite.encrypt(secret_text.encode())
    encrypted_text = encrypted_text.decode()

    with open("TopSecret.txt" , "w") as file:
        file.write(header_text + "\n\n")
        file.write("Encrypted Text:\n")
        file.write(encrypted_text)

    result_label.config(text="The encrypted text is saved to file.")




#image
image = Image.open("topsecret.png")
image = image.resize((100, 100), Image.Resampling.LANCZOS)

tk_image = ImageTk.PhotoImage(image)   # from pillow to tkinter

image_label = tk.Label(window, image=tk_image)
image_label.pack()

window.tk_image = tk_image

enter_your_title = tk.Label(text="Enter your title")
enter_your_title.pack()

entry_title = tk.Entry(bg="white",width=15,fg="black")
entry_title.pack()

secret = tk.Label(text="Enter your secret")
secret.pack()

entry_secret = tk.Entry(width=20,bg="white",fg="black")
entry_secret.pack(pady=10,ipady=70)

mk_label = tk.Label(text="Enter master key")
mk_label.pack()

entry_master_key = tk.Entry(bg="white",fg="black")
entry_master_key.pack()

encrypt_button = tk.Button(text="Save & Encrypt" ,font="Arial",command=encrypt_text)
encrypt_button.pack()

decrypt_button = tk.Button(text="Decrypt")
decrypt_button.pack()

result_label = tk.Label(text="")
result_label.pack()





window.mainloop()

