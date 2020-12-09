import tkinter as tk
 
window = tk.Tk()
 
def handle_keypress(event):
    """Выводит символ, связанный с нажатой клавишей"""
    print(event.char)
 
# Связывает событие нажатия клавиши с handle_keypress()
window.bind("<Key>", handle_keypress)
 
window.mainloop()
