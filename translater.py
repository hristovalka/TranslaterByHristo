from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk

def translate_text():
    source_lang = source_lang_combo.get()
    target_lang = target_lang_combo.get()
    input_text = input_text_widget.get("1.0", END).strip()

    if not input_text:
        output_text_widget.delete("1.0", END)
        output_text_widget.insert(END, "Please enter text to translate.")
        return

    try:
        translator = Translator()
        translated = translator.translate(input_text, src=source_lang, dest=target_lang)
        output_text_widget.delete("1.0", END)
        output_text_widget.insert(END, translated.text)
    except Exception as e:
        output_text_widget.delete("1.0", END)
        output_text_widget.insert(END, f"Translation error: {e}")

def toggle_theme():
    if root.get_theme() == "breeze":
        root.set_theme("equilux")
        root.configure(bg="#222222")
        frame.configure(bg="#222222")
        footer_label.configure(background="#222222", foreground="white")
    else:
        root.set_theme("breeze")
        root.configure(bg="#2c3e50")
        frame.configure(bg="#2c3e50")
        footer_label.configure(background="#2c3e50", foreground="white")

# Create main application window with a modern theme
root = ThemedTk(theme="breeze")
root.title("Text Translator")
root.geometry("800x600")
root.resizable(True, True)

# Set a unique background color
root.configure(bg="#2c3e50")

# Load an icon for the application (optional)
try:
    icon = Image.open("icon.png")
    icon = ImageTk.PhotoImage(icon)
    root.iconphoto(False, icon)
except Exception as e:
    print("Icon not found or could not be loaded")

# Styling options
style = ttk.Style()
style.configure('TLabel', font=('Arial', 14), background="#2c3e50", foreground="white")
style.configure('TButton', font=('Arial', 14), background="#3498db", foreground="white")
style.configure('TCombobox', font=('Arial', 14))

# Create and place widgets
frame = Frame(root, bg="#2c3e50")
frame.pack(pady=20)

source_lang_label = ttk.Label(frame, text="Source Language:")
source_lang_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

source_lang_combo = ttk.Combobox(frame, values=list(LANGUAGES.values()))
source_lang_combo.set('English')
source_lang_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)

target_lang_label = ttk.Label(frame, text="Target Language:")
target_lang_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

target_lang_combo = ttk.Combobox(frame, values=list(LANGUAGES.values()))
target_lang_combo.set('Bulgarian')
target_lang_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)

input_text_label = ttk.Label(frame, text="Input Text:")
input_text_label.grid(row=2, column=0, padx=10, pady=10, sticky=NW)

input_text_widget = Text(frame, height=10, width=50, font=('Arial', 12), bg="#ecf0f1", fg="#2c3e50", relief="flat", borderwidth=5, highlightthickness=2, highlightbackground="#3498db", highlightcolor="#3498db")
input_text_widget.grid(row=2, column=1, padx=10, pady=10)

output_text_label = ttk.Label(frame, text="Translated Text:")
output_text_label.grid(row=3, column=0, padx=10, pady=10, sticky=NW)

output_text_widget = Text(frame, height=10, width=50, font=('Arial', 12), bg="#ecf0f1", fg="#2c3e50", relief="flat", borderwidth=5, highlightthickness=2, highlightbackground="#3498db", highlightcolor="#3498db")
output_text_widget.grid(row=3, column=1, padx=10, pady=10)

# Create a custom rounded button using Canvas
def create_rounded_button(canvas, text, x, y, width, height, radius, color, command):
    # Create rounded rectangle
    points = [x+radius, y,
              x+width-radius, y,
              x+width, y,
              x+width, y+radius,
              x+width, y+height-radius,
              x+width, y+height,
              x+width-radius, y+height,
              x+radius, y+height,
              x, y+height,
              x, y+height-radius,
              x, y+radius,
              x, y]
    button_id = canvas.create_polygon(points, smooth=True, fill=color, outline=color)
    
    # Add text to the button
    text_id = canvas.create_text(x + width / 2, y + height / 2, text=text, font=('Arial', 14), fill="white")

    # Bind button click
    def on_click(event):
        command()
    
    canvas.tag_bind(button_id, "<Button-1>", on_click)
    canvas.tag_bind(text_id, "<Button-1>", on_click)

canvas = Canvas(frame, width=200, height=70, bg="#2c3e50", highlightthickness=0)
canvas.grid(row=4, column=0, columnspan=2, pady=20)
create_rounded_button(canvas, "Translate", 10, 10, 180, 50, 25, "#3498db", translate_text)

# Add a footer label (optional)
footer_label = ttk.Label(root, text="Powered by Google Translate", font=('Arial', 10), background="#2c3e50", foreground="white")
footer_label.pack(side=BOTTOM, pady=10)

# Create a menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Add theme toggle to the menu
theme_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Options", menu=theme_menu)
theme_menu.add_command(label="Toggle Theme", command=toggle_theme)

root.mainloop()
