import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from googletrans import Translator

def translate_text(text, target_lang):
    try:
        translator = Translator()
        translated = translator.translate(text, dest=target_lang).text
        return translated
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")
        return ""

def on_translate():
    lang_map = {
        'English to Hindi': 'hi',
        'Hindi to English': 'en',
        'English to Marathi': 'mr',
        'Marathi to English': 'en'
    }
    lang_pair = language_var.get()
    target_lang = lang_map.get(lang_pair, 'en')

    text = input_text.get("1.0", tk.END).strip()
    if text:
        output_text.delete("1.0", tk.END)
        translated_text = translate_text(text, target_lang)
        output_text.insert(tk.END, translated_text)

root = tk.Tk()
root.title("Translator")
root.geometry("500x450")
root.configure(bg="#e6f2ff")

style = ttk.Style()
style.theme_use('clam')

style.configure("TLabel", foreground="#003366", background="#e6f2ff", font=("Helvetica", 14, "bold"))
style.configure("TButton", background="#0066cc", foreground="white", font=("Helvetica", 12, "bold"), padding=5)
style.map('TButton', background=[('active', '#004c99')])

ttk.Label(root, text="Translator", font=("Helvetica", 18), background="#e6f2ff", foreground="#003366").pack(pady=15)

language_var = tk.StringVar(value="English to Hindi")
language_menu = ttk.Combobox(root, textvariable=language_var, values=("English to Hindi", "Hindi to English", "English to Marathi", "Marathi to English"), font=("Helvetica", 12))
language_menu.pack(pady=5)
language_menu.config(width=30)

input_text = scrolledtext.ScrolledText(root, width=50, height=6, font=("Helvetica", 12), wrap=tk.WORD, relief=tk.GROOVE, borderwidth=2)
input_text.pack(pady=10)

translate_button = ttk.Button(root, text="Translate", command=on_translate)
translate_button.pack(pady=10)

output_text = scrolledtext.ScrolledText(root, width=50, height=6, font=("Helvetica", 12), wrap=tk.WORD, relief=tk.GROOVE, borderwidth=2)
output_text.pack(pady=10)

for widget in root.winfo_children():
    widget.pack_configure(padx=10, pady=5)

root.mainloop()
