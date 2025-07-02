import tkinter as tk
from tkinter import font as tkfont
import sys

class TextRedirector:
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")
        self.widget.yview("end")  # Auto-scroll

    def flush(self):
        pass

def main():
    root = tk.Tk()
    root.title("Print Redirection Example")

    text_font = tkfont.Font(family="Helvetica", size=16)
    text_widget = tk.Text(root, font=text_font, fg="green",bg="black")
    text_widget.pack(padx=10, pady=10)

    # Deshabilita la edición en el widget de texto
    text_widget.configure(state="disabled")

    # Redirige sys.stdout al widget de texto
    sys.stdout = TextRedirector(text_widget)

    #-- ingreso de texro personalizado
    print("Menu")
    print("1. Nueva partida")
 
    root.mainloop()

if __name__ == "__main__":
    main()