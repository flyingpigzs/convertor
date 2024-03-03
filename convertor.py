# Import necessary modules from tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# When user submit the request by clicking "Convert" button, we need to indentify each request and handle it
# to corresponding function.
def submit():
  submitted_value = int(entry.get())
  selected_value = combo_box.get()
  match selected_value:
    case 'Fahrenheit to Celsius':
      result = fa_to_ce(submitted_value)
      messagebox.showinfo("Result", result)
    case 'Celsius To Fahrenheit':
      result = ce_to_fa(submitted_value)
      messagebox.showinfo("Result", result)
    case 'Miles To Kilometres':
      result = mi_to_km(submitted_value)
      messagebox.showinfo("Result", result)
    case 'Kilometres to Miles':
      result = km_to_mi(submitted_value)
      messagebox.showinfo("Result", result)
    case 'Pounds to Kilograms':
      result = lb_to_kg(submitted_value)
      messagebox.showinfo("Result", result)
    case 'Kilograms to Pounds':
      result = kg_to_lb(submitted_value)
      messagebox.showinfo("Result", result)
    case _:
      messagebox.showerror('Invalid input')

# Display different unit when selecting different value in the dropdown box.
def on_select():
  selected_value = combo_box.get()
  result = ''
  match selected_value:
    case 'Fahrenheit to Celsius':
      result = 'Fahrenheit'
    case 'Celsius To Fahrenheit':
      result = 'Celsius'
    case 'Miles To Kilometres':
      result = 'Miles'
    case 'Kilometres to Miles':
      result = 'Kilometres'
    case 'Pounds to Kilograms':
      result = 'Pounds'
    case 'Kilograms to Pounds':
      result = 'Kilograms'
    case _:
      messagebox.showerror('Invalid input')
  unit.configure(text=result)

# 6 converting methods
def fa_to_ce(value):
  converted_value = (value - 32) / 1.8
  converted_value = round(converted_value, 2)
  return converted_value

def ce_to_fa(value):
  converted_value = value * 1.8 + 32
  converted_value = round(converted_value, 2)
  return converted_value

def mi_to_km(value):
  converted_value = value * 1.609
  converted_value = round(converted_value, 2)
  return converted_value

def km_to_mi(value):
  converted_value = value * 0.621371
  converted_value = round(converted_value, 2)
  return converted_value

def lb_to_kg(value):
  converted_value = value * 2.20462
  converted_value = round(converted_value, 2)
  return converted_value

def kg_to_lb(value):
  converted_value = value / 2.20462
  converted_value = round(converted_value, 2)
  return converted_value

# Main window
win_main = tk.Tk()
win_main.title('Convertor')
win_main.geometry('500x300')

# Instruction Message
msg_main_text = 'Select what unit you want to convert:'
msg_main = tk.Label(text=msg_main_text)
msg_main.pack()

# Dropdown box
options = ['Fahrenheit to Celsius', 'Celsius To Fahrenheit', 'Miles To Kilometres', 'Kilometres to Miles', 'Pounds to '
                                                                                                       'Kilograms',
           'Kilograms to Pounds']
combo_box = ttk.Combobox(win_main, values=options, state='readonly', justify='center')
combo_box.pack()
cb = ttk.Combobox()
combo_box.bind("<<ComboboxSelected>>", lambda event:on_select())

# In order to place input box and unit in the same line, we need to define a frame and put
# them in the frame together
frame = ttk.Frame(win_main)
frame.pack()

# Input box
entry = ttk.Entry(frame, width=5, justify='center')
entry.pack(side='left')

# Unit
unit = tk.Label(frame, text='')
unit.pack(side='left')

# Submit button
submit_button = ttk.Button(win_main, text='Convert', command=submit)
submit_button.pack()

# Mainloop
win_main.mainloop()