import tkinter as tk
from tkinter import ttk
import requests
import os
from dotenv import load_dotenv

class TextTranslatorApp:
    def __init__(self,root):
        self.root = root
        root.title("Text Translator")
        self.create_widgets()


    def create_widgets(self):
        label1 = tk.Label(self.root,text="Enter text to translate:")
        self.entry = tk.Entry(self.root, width=50)
        label2 = tk.Label(self.root,text="Choose source language:")
        self.source_lang = ttk.Combobox(self.root,values=["en", "es", "fr", "vi", "ja", "zh"])
        self.source_lang.set("en")
        label3 = tk.Label(self.root,text="Enter target language:")
        self.target_lange = ttk.Combobox(self.root,values=["en", "es", "fr", "vi", "ja", "zh"])
        self.target_lange.set("vi")
        translate_button = ttk.Button(self.root,text="Translate",command=self.translate_text)
        self.result_label = tk.Label(self.root,text="Translated text will appear here:")
        label1.grid(row=0,column=0, padx=10, pady=10,)
        self.entry.grid(row=0,column=1, padx=10, pady=10)

        label2.grid(row=1,column=0, padx=10, pady=10,)
        self.source_lang.grid(row=1,column=1, padx=10, pady=10)

        label3.grid(row=2,column=0, padx=10, pady=10)
        self.target_lange.grid(row=2,column=1, padx=10, pady=10)
        translate_button.grid(row=3,column=0, columnspan=2, pady=10)
        self.result_label.grid(row=4,column=0, columnspan=2, pady=10)

    def translate_text(self):
        # Tải các biến từ file .env vào môi trường
        load_dotenv()

        # Lấy giá trị của API_KEY từ biến môi trường
        # os.getenv() là cách an toàn để đọc, nó sẽ trả về None nếu không tìm thấy
        api_key = os.getenv("API_KEY")
        #already disabled on Google Cloud
        text_to_translate=self.entry.get()
        url=f"https://translation.googleapis.com/language/translate/v2?key={api_key}"
        params={
            "q": text_to_translate,
            "source": self.source_lang.get(),
            "target": self.target_lange.get(),
        }
        response = requests.get(url, params=params)
        translated_text = response.json()["data"]["translations"][0]["translatedText"]
        self.result_label.config(text=translated_text)

if __name__=="__main__":
    root = tk.Tk()
    app = TextTranslatorApp(root)
    root.mainloop()