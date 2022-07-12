from tkinter import *


# Functionality
def miles_to_km():
    miles = float(miles_inpt.get())
    km = miles * 1.609
    km_output_label.config(text=f'{km}')


# Window setup
window = Tk()
window.title('Miles to Km Converter')
window.config(padx=20, pady=20)


# Miles input widget & label
miles_inpt = Entry(width=7)
miles_inpt.grid(column=1, row=0)
miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)


# 'is equal' label
is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)


# Km output label
km_output_label = Label(text='0')
km_output_label.grid(column=1, row=1)

# Km label
km_label = Label(text='Km')
km_label.grid(column=2, row=1)

# Calculate button
calculate_btn = Button(text='Calculate', command=miles_to_km)
calculate_btn.grid(column=1, row=2)










































window.mainloop()