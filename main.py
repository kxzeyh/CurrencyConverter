import tkinter as tk
from tkinter import ttk, messagebox
import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/3a2af7d89f02d2d2cc69c173/latest/USD"
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
