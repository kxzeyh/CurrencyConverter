import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import os

currencies = {
    "USD": "United States",
    "EUR": "Euro",
    "GBP": "United Kingdom",
    "JPY": "Japan",
    "AUD": "Australia",
    "CAD": "Canada",
    "CHF": "Switzerland",
    "CNY": "China",
    "SEK": "Sweden",
    "NZD": "New Zealand",
    "MXN": "Mexico",
    "SGD": "Singapore",
    "HKD": "Hong Kong",
    "NOK": "Norway",
    "KRW": "South Korea",
    "TRY": "Turkey",
    "RUB": "Russia",
    "INR": "India",
    "BRL": "Brazil",
    "ZAR": "South Africa"
}
def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/3a2af7d89f02d2d2cc69c173/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        return data['conversion_rates'][target_currency]
    else:
        messagebox.showerror("Error", "Failed to retrieve exchange rates.")
        return None


def convert_currency():
    base_currency = base_currency_var.get().upper()
    target_currency = target_currency_var.get().upper()
    amount = amount_entry.get()

    if not amount:
        messagebox.showerror("Input Error", "Please enter a valid amount.")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")
        return

    api_key = '3a2af7d89f02d2d2cc69c173' 
    exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
    

    if exchange_rate:
        converted_amount = amount * exchange_rate
        result_label.config(text=f"{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        result_label.config(text="Conversion failed.")

def load_flag(currency_code):
    img_path = os.path.join("flags", f"{currency_code}.png")
    img = Image.open(img_path).resize((25, 15), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

def swap_currencies():
    base_currency = base_currency_var.get()
    target_currency = target_currency_var.get()
    base_currency_var.set(target_currency)
    target_currency_var.set(base_currency)
    update_flag(base_flag_label, base_currency_var.get())
    update_flag(target_flag_label, target_currency_var.get())

def update_flag(label, currency_code):
    flag_image = load_flag(currency_code)
    label.config(image=flag_image)
    label.image = flag_image

root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.resizable(True, True)

title_label = tk.Label(root, text="Currency Converter", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

base_currency_label = tk.Label(frame, text="Base Currency:", font=("Arial", 12))
base_currency_label.grid(row=0, column=0, padx=10, pady=5)

base_currency_var = tk.StringVar(value="USD")
base_currency_combo = ttk.Combobox(frame, textvariable=base_currency_var, values=currencies, font=("Arial", 12), state="readonly", width=10)
base_currency_combo.grid(row=0, column=1, padx=10, pady=5)
base_currency_combo.current(0)

base_flag_label = tk.Label(frame)
base_flag_label.grid(row=0, column=2, padx=10)
update_flag(base_flag_label, base_currency_var.get())

target_currency_label = tk.Label(frame, text="Target Currency:", font=("Arial", 12))
target_currency_label.grid(row=1, column=0, padx=10, pady=5)

target_currency_var = tk.StringVar(value="EUR")
target_currency_combo = ttk.Combobox(frame, textvariable=target_currency_var, values=currencies, font=("Arial", 12), state="readonly", width=10)
target_currency_combo.grid(row=1, column=1, padx=10, pady=5)
target_currency_combo.current(1)

amount_label = tk.Label(frame, text="Amount:", font=("Arial", 12))
amount_label.grid(row=2, column=0, padx=10, pady=5)

amount_entry = ttk.Entry(frame, font=("Arial", 12), width=10)
amount_entry.grid(row=2, column=1, padx=10, pady=5)

convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()
