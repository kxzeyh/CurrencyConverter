# Currency Converter with Flag Display

## Overview

This project is a simple Currency Converter application built using Python's `tkinter` library for the GUI and the `Pillow` library for image processing. The application allows users to select a base currency and a target currency from a dropdown menu, input an amount, and then convert the amount using real-time exchange rates retrieved from an external API. The corresponding flags of the selected currencies are also displayed next to the dropdown menus.

## Features

- Real-time currency conversion using ExchangeRate-API.
- Display of national flags for the selected currencies.
- Simple and user-friendly graphical interface.
- Swap button to easily switch between base and target currencies.

## Modules Used

### 1. `tkinter`
- **Purpose**: Provides the graphical user interface (GUI) for the application.
- **Components**: 
  - `Tk()`: Creates the main window.
  - `Label()`: Used for displaying text and images.
  - `Entry()`: For user input (e.g., the amount to convert).
  - `Button()`: For performing actions (e.g., convert, swap).
  - `ttk.Combobox`: Provides dropdown menus for selecting currencies.

### 2. `Pillow` (PIL)
- **Purpose**: Handles image processing tasks such as opening, resizing, and displaying images.
- **Key Functions**:
  - `Image.open()`: Opens an image file.
  - `Image.resize()`: Resizes the image to fit within the GUI.
  - `ImageTk.PhotoImage()`: Converts images into a format that can be displayed in the `tkinter` interface.

### 3. `requests`
- **Purpose**: Sends HTTP requests to the ExchangeRate-API to retrieve current exchange rates.
- **Key Functions**:
  - `requests.get()`: Sends a GET request to the API and retrieves data in JSON format.

## API Used

### ExchangeRate-API
- **URL**: [https://www.exchangerate-api.com/](https://www.exchangerate-api.com/)
- **Purpose**: Provides real-time currency exchange rates.
- **API Key**: A unique API key is required to access the API. The key is used to authenticate requests.
- **Example Request**:
  ```python
  url = f"https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD"
  response = requests.get(url)
  data = response.json()
