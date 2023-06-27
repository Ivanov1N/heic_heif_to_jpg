import customtkinter as ctk
from customtkinter import filedialog
from PIL import Image
import pillow_heif


# Creating app window
window = ctk.CTk()
window.title('My HEIC/HEIF to JPG converter')
window.geometry('700x320')
window.resizable(width=False, height=False)
window.grid_columnconfigure(0, minsize=200)

# Convert and save function
def convert():
    try: 
        if len(heic_path) == 0:
            pass
        else:
            heif_file = pillow_heif.read_heif(heic_path)
            image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw")
            new_filepath=filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[('JPEG File', '*.jpg')])
            image.save(new_filepath, format('jpeg'))
            result_label.configure(text="Converted and saved!", text_color='green')
    except NameError:
        result_label.configure(text="Please load HEIC/HEIF file!", text_color='red')
    except FileNotFoundError:
        result_label.configure(text='Convert again!')
        
# Heic file loading function
def load_heic(event=None):
    t = filedialog.askopenfilename()
    if  t[-5:] in ('.heic', '.heif'):
        global heic_path
        heic_path = t
        heic_entry.configure(text=heic_path[t.rfind('/')+1:], text_color='blue')
        result_label.configure(text="...")
        heic_check.configure (text = 'OK', text_color='green')
    else:
        heic_entry.configure(text='')
        result_label.configure(text="...")
        heic_check.configure(text='X', text_color='red')
        if 'heic_path' in globals():
            del globals()['heic_path']
def refresh_func ():
    result_label.configure(text='...')
    heic_entry.configure(text='')
    heic_check.configure(text='')
    if 'heic_path' in globals():
        del globals()['heic_path']
           
# Creating and placing widgets
# Frame and labels
results_frame = ctk.CTkFrame(window, width=300, height=100, fg_color='light blue')
results_frame.place(relx = 0.226, rely = 0.67, anchor='center')
heic_label = ctk.CTkLabel(window, text='Load HEIC/HEIF image:', bg_color='transparent')
heic_label.grid(row=0, column=0, sticky='w')
heic_entry = ctk.CTkLabel(window, text='', width=250, bg_color='white')
heic_entry.grid(row=0, column=2, sticky='w')
messages_label = ctk.CTkLabel(window, text='Results:', font=('Arial', 12))
messages_label.grid(row=9, column=0, sticky='w')
result_label = ctk.CTkLabel(results_frame, text='...')
result_label.place(x=0, y=0, relx=0.04)
heic_check = ctk.CTkLabel(window, text='', font=('Arial', 12, 'bold'))
heic_check.grid(row=0, column=3, sticky='w', padx=10)

# Buttons
heic_browse_button = ctk.CTkButton(window, text='Browse...', command=load_heic)
heic_browse_button.grid(row=0, column=1, pady=10, padx=20, sticky='w')
start_button = ctk.CTkButton(window, text='CONVERT AND SAVE', command=convert)
start_button.grid(row=8, column=1, pady=30)
refresh_button = ctk.CTkButton(window, text='RESET', command=refresh_func)
refresh_button.grid(row=8, column=2, pady=30)

window.mainloop()


    













