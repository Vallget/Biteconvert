from customtkinter import *

conversion_rates = {
    'Bit': 1 / 8,
    'Byte': 1,
    'Kilobyte': 1024,
    'Megabyte': 1024 ** 2,
    'Gigabyte': 1024 ** 3,
    'Terabyte': 1024 ** 4,
    'Petabyte': 1024 ** 5
}

def convert():
    try:
        input_value = float(user_input.get())
        input_unit = datainput.get()
        output_unit = dataoutput.get()
        
        value_in_bytes = input_value * conversion_rates[input_unit]
        converted_value = value_in_bytes / conversion_rates[output_unit]
        user_output.configure(text=converted_value)
        
    except ValueError:
        user_output.configure(text='Invalid input')
    

root = CTk()
root.title('Biteconvert')
root.geometry('320x250')
root.resizable(width=False, height=False)
set_appearance_mode('dark')

datainput = CTkOptionMenu(
    root, 
    values=['Byte', 'Bit', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte', 'Petabyte'],
    corner_radius=10,
    width=135,
    height=40
    )
datainput.place(x=15, y=40)

dataoutput = CTkOptionMenu(
    root, 
    values=['Bit', 'Byte', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte', 'Petabyte'],
    corner_radius=10,
    width=135,
    height=40
    )
dataoutput.place(x=15, y=150)

user_input = CTkEntry(
    root,
    width=135,
    height=40
    )
user_input.place(x=170, y=40)

user_output = CTkLabel(
    root,
    text='',
    bg_color='grey',
    width=135,
    height=40
    )
user_output.place(x=170, y=150)

conv = CTkButton(
    root,
    text='convert',
    width=7,
    height=7,
    command=convert
)
conv.place(x=210, y=105)

root.mainloop()
