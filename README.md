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


## Project Structure

CurrencyConverter/
│
├── main.py               # Main Python script containing the application logic
├── flags/                # Directory containing flag images
│   ├── USD.png           # Example flag image for the US dollar
│   ├── EUR.png           # Example flag image for the Euro
│   ├── ...
└── README.md             # This README file

### How to Run the Project
## Prerequisites
- **Python 3.x**: Make sure Python is installed on your system.
- **Install Required Modules**: Run the following command to install the necessary Python libraries:
- pip install tkinter pillow requests

### Steps
## Obtain an API Key:

- Sign up at ExchangeRate-API to obtain a free API key.
- Replace YOUR_API_KEY in the main.py script with your actual API key.
- Prepare Flag Images:

- Download flag images for each currency you want to support.
- Save these images in the flags/ directory with filenames matching the currency codes (e.g., USD.png, EUR.png).

## Run the Application:

- Navigate to the project directory.
- Execute the main.py script using Python:
```python
  python main.py
  Using the Application:
```

- Select the base currency and target currency from the dropdown menus.
- Enter the amount you want to convert.
- Click the "Convert" button to see the result.
- Use the "Swap" button to switch between base and target currencies.

## Notes
- **Error Handling**: The application includes basic error handling to alert the user if the exchange rate data cannot be retrieved or if the flag image is not found.
- **Customization**: You can easily add more currencies by adding the relevant flag images to the flags/ directory and updating the currencies dictionary in the script.

## License
- This project is for educational purposes and is provided as-is without any warranties. You are free to modify and distribute the code as you see fit.
