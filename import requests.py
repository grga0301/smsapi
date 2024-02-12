import tkinter as tk
from tkinter import messagebox
import requests

def send_sms():
    phone_number = phone_entry.get()
    message = message_entry.get()

    # Postavite podatke za slanje SMS-a
    data = {
        'phone': phone_number,
        'message': message,
        'key': 'textbelt',
    }

    # Napravite HTTP POST zahtjev
    response = requests.post('https://textbelt.com/text', data=data)

    # Ispišite odgovor (JSON format)
    result_label.config(text=response.json())

# Stvori glavni prozor
root = tk.Tk()
root.title("SMS Sender")

# Postavke Grid metode za automatsko prilagođavanje elemenata
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Labela i unos za broj telefona
phone_label = tk.Label(root, text="Broj telefona:")
phone_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
phone_entry = tk.Entry(root)
phone_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Labela i unos za poruku
message_label = tk.Label(root, text="Poruka:")
message_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
message_entry = tk.Entry(root)
message_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Gumb za slanje poruke
send_button = tk.Button(root, text="Pošalji poruku", command=send_sms)
send_button.grid(row=2, columnspan=2, padx=5, pady=5, sticky="ew")

# Labela za ispis rezultata
result_label = tk.Label(root, text="", wraplength=300)
result_label.grid(row=3, columnspan=2, padx=5, pady=5, sticky="ew")

# Pokreni glavnu petlju programa
root.mainloop()
