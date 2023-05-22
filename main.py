from tkinter import *
from random import randint, choice
from tkinter import messagebox

# Каркас
window = Tk()
window.resizable(width=False, height=False)
window.title('Приложение кинотеатра')
window.geometry('520x360')
window['bg'] = 'white'


#Надписи
firstText = Label(window, text = 'Чебурашка', font = ('Arial Bold', 15), fg = 'black', bg = 'white')
firstText.place(x = 25, y = 10)

secondText = Label(window, text = 'Титаник', font = ('Arial Bold', 15), fg = 'black', bg = 'white')
secondText.place(x = 25, y = 100)


# Надписи для полей ввода

#Сколько осталось билетов
stillfirstText = 3
stillsecondText = 2

#Цена за фильмы
priceForFirstFilm = 250
priceForSecondFilm = 100

stillFirstText = Label(window, text = f"Осталось билетов: {str(stillfirstText)}", font = ('Arial Bold', 15), fg = 'black', bg = 'white')
stillFirstText.place(x = 200, y = 55)

stillFirstText = Label(window, text = f"Цена: {str(priceForFirstFilm)}", font = ('Arial Bold', 15), fg = 'black', bg = 'white')
stillFirstText.place(x = 200, y = 25)

stillFirstText = Label(window, text = 'Осталось билетов: ' + str(stillsecondText), font = ('Arial Bold', 15), fg = 'black', bg = 'white')
stillFirstText.place(x = 200, y = 155)

stillFirstText = Label(window, text = 'Цена ' + str(priceForSecondFilm), font = ('Arial Bold', 15), fg = 'black', bg = 'white')
stillFirstText.place(x = 200, y = 125)

# Поля для ввода

enterFirstText = Entry(fg='black', width=25)
enterFirstText.place(x = 35, y = 60)

secondEnterText = Entry(fg='black', width=25)
secondEnterText.place(x = 35, y = 160)

window.mainloop()