from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

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

# Create main application window
root = Tk()
root.title("Text Translator")
root.geometry("800x400")
root.resizable(True, True)

# Create and place widgets
source_lang_label = Label(root, text="Source Language:")
source_lang_label.pack(pady=5)

source_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()))
source_lang_combo.set('english')
source_lang_combo.pack(pady=5)

target_lang_label = Label(root, text="Target Language:")
target_lang_label.pack(pady=5)

target_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()))
target_lang_combo.set('bulgarian')
target_lang_combo.pack(pady=5)

input_text_label = Label(root, text="Input Text:")
input_text_label.pack(pady=5)

input_text_widget = Text(root, height=10, width=50)
input_text_widget.pack(pady=5)

output_text_label = Label(root, text="Translated Text:")
output_text_label.pack(pady=5)

output_text_widget = Text(root, height=10, width=50)
output_text_widget.pack(pady=5)

translate_button = Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=5)

root.mainloop()
