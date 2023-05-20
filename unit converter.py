import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import random

# Conversion factors
CONVERSION_FACTORS = {
    # Length units
    "Meter": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Inch": 39.37,
        "Foot": 3.281,
        "Yard": 1.094,
        "Mile": 0.0006214
    },
    # Mass units
    "Kilogram": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1000000,
        "Pound": 2.205,
        "Ounce": 35.274
    },
    # Temperature units
    "Celsius": {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: (x * 9/5) + 32,
        "Kelvin": lambda x: x + 273.15
    },
    # Volume units
    "Liter": {
        "Liter": 1,
        "Milliliter": 1000,
        "Cubic Meter": 0.001,
        "Cubic Foot": 0.03531,
        "Gallon": 0.2642
    },
    # Time units
    "Second": {
        "Second": 1,
        "Minute": 1/60,
        "Hour": 1/3600,
        "Day": 1/86400,
        "Week": 1/604800,
        "Month": 1/2628000,
        "Year": 1/31536000
    },
    # Speed units
    "Meter per Second": {
        "Meter per Second": 1,
        "Kilometer per Hour": 3.6,
        "Mile per Hour": 2.237
    },
    # Area units
    "Square Meter": {
        "Square Meter": 1,
        "Square Kilometer": 0.000001,
        "Square Foot": 10.764,
        "Square Mile": 0.0000003861,
        "Acre": 0.0002471
    },
    # Pressure units
    "Pascal": {
        "Pascal": 1,
        "Kilopascal": 0.001,
        "Bar": 0.00001,
        "Pound per Square Inch": 0.000145
    },
    # Energy units
    "Joule": {
        "Joule": 1,
        "Kilojoule": 0.001,
        "Calorie": 0.239,
        "Kilocalorie": 0.000239,
        "Electronvolt": 6.242e+18
    }
}


# List of units
UNITS = {
    # Length units
    "Meter": "m",
    "Kilometer": "km",
    "Centimeter": "cm",
    "Millimeter": "mm",
    "Inch": "in",
    "Foot": "ft",
    "Yard": "yd",
    "Mile": "mi",
    # Mass units
    "Kilogram": "kg",
    "Gram": "g",
    "Milligram": "mg",
    "Pound": "lb",
    "Ounce": "oz",
    # Temperature units
    "Celsius": "°C",
    "Fahrenheit": "°F",
    "Kelvin": "K",
    # Volume units
    "Liter": "L",
    "Milliliter": "mL",
    "Cubic Meter": "m³",
    "Cubic Foot": "ft³",
    "Gallon": "gal",
    # Time units
    "Second": "s",
    "Minute": "min",
    "Hour": "hr",
    "Day": "day",
    "Week": "week",
    "Month": "month",
    "Year": "year",
    # Speed units
    "Meter per Second": "m/s",
    "Kilometer per Hour": "km/h",
    "Mile per Hour": "mph",
    # Area units
    "Square Meter": "m²",
    "Square Kilometer": "km²",
    "Square Foot": "ft²",
    "Square Mile": "mi²",
    "Acre": "acre",
    # Pressure units
    "Pascal": "Pa",
    "Kilopascal": "kPa",
    "Bar": "bar",
    "Pound per Square Inch": "psi",
    # Energy units
    "Joule": "J",
    "Kilojoule": "kJ",
    "Calorie": "cal",
    "Kilocalorie": "kcal",
    "Electronvolt": "eV",
}

def convert():
    try:
        value = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()
        
        result = value * CONVERSION_FACTORS[from_unit][to_unit]
        result_label.config(text=f"{result:.4f}")
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Unit Converter")

# Generate a random background color
random_color = "#" + "%06x" % random.randint(0, 0xFFFFFF)

# Set the background color
window.configure(background=random_color)

# Set the fixed screen size
window.geometry("400x300")

# Set the style
style = ttk.Style()
style.theme_use("clam")

# Create a frame
frame = ttk.Frame(window, padding="20")
frame.grid(sticky="nsew")

# Set responsive grid weights
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
frame.rowconfigure(4, weight=1)

# Font settings
font = Font(family="Arial", size=14)

# From unit selection
from_label = ttk.Label(frame, text="From:", font=font)
from_label.grid(row=0, column=0, padx=10, pady=10)
from_var = tk.StringVar()
from_dropdown = ttk.Combobox(frame, textvariable=from_var, values=list(UNITS.keys()), state="readonly", font=font)
from_dropdown.grid(row=0, column=1, padx=10, pady=10)

# To unit selection
to_label = ttk.Label(frame, text="To:", font=font)
to_label.grid(row=1, column=0, padx=10, pady=10)
to_var = tk.StringVar()
to_dropdown = ttk.Combobox(frame, textvariable=to_var, values=list(UNITS.keys()), state="readonly", font=font)
to_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Entry for value to convert
entry = ttk.Entry(frame, font=font)
entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Convert button
convert_button = ttk.Button(frame, text="Convert", command=convert)
convert_button.configure(style="TButton")
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Result label
result_label = ttk.Label(frame, text="", font=font)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Make the window responsive
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Start the Tkinter event loop
window.mainloop()
