# Программа часы

from tkinter import *
import time
import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except Exception:
    pass

root = Tk()
root.resizable(False, False)
root.config(bg='black')
root.title('Watch')
root.iconbitmap(r'C:\Users\user\Desktop\курс питон записи\GPT_tasks\watch\watch.ico')

def tick():
    # С помощью системного метода after мы указываем время в миллисекундах с которой функция будет вызывать саму себя
    watch.after(100, tick)
    # Далее в вставляем наше обновлённое время в лейбл где оно будет отображаться
    watch['text'] = time.strftime('%H:%M:%S')

watch = Label(root, font='Arial 70', fg='white', bg='black')
watch.pack()
tick() # Вызываем функцию один раз, чтобы запустить цикл


root.mainloop()