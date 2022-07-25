from tkinter import *
from string import ascii_lowercase

ALPHABET = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}
PATH_INPUT = ''
PATH_OUTPUT = './output.txt'
FONT = 'Courier'
GREEN = '#5FD068'
BLUE ='#A5BECC'
DARK = '#354259'

def alphabet_position(text):
    text = text.lower()
    positions = [ALPHABET[char] for char in text if char in ALPHABET]
    
    return ' '.join(positions)


# Create Object and set Geometry
root = Tk()
root.geometry('420x220')
root.title('Encryptor 3000')
root.config(bg=DARK)

# Labels & Buttons
title = Label(root, text='ENCRYPTOR 3000', font=(FONT, 25), fg=BLUE, bg=DARK)
title.grid(column=0, row=0, pady=20)

file_path_btn = Button(root, text='Choose file...', relief='solid', bg='white', font=(FONT, 14), borderwidth=0, highlightbackground=DARK) # TODO: Add command to fetch file path
file_path_btn.grid(column=0, row=1)

frame = Frame(bg=DARK)
frame.grid(column=0, row=2)

inst_text = Label(frame, text='Press "Show output" to see the encrypted text\n or "Save as a .txt" to save into your disk.', font=(FONT, 14, 'italic'), fg=BLUE, bg=DARK)
inst_text.grid(column=0,row=2, pady=20, padx=30, columnspan=2)

convert_btn = Button(frame, text='Show output', relief='solid', bg='white', font=(FONT,14), borderwidth=0, highlightbackground=DARK) # TODO: Add command to display encrypted text (change inst_text label)
convert_btn.grid(column=0, row=3)

save_btn = Button(frame, text='Save as .txt file', relief='solid', bg='white', font=(FONT,14), borderwidth=0, highlightbackground=DARK) # TODO: Add command to save into file
save_btn.grid(column=1, row=3)

root.mainloop()