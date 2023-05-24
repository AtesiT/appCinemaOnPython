from tkinter import *
from random import randint, choice
from tkinter import messagebox

stillfirstText = 3
stillsecondText = 2

def toChangeAmountOfTicketsAndChangeAmountMoneyFirstButton ():
    value = enterFirstText.get()
    intValue = int(value)
    global stillfirstText
    global stillsecondText
    global amountOfMoney

    if (intValue == 0):
        stillfirstText = stillfirstText - intValue
        messagebox.showinfo('Ошибка', ("Вы ничего не приобрели"))
        enterFirstText.delete(0, 'end')
    elif (intValue > stillfirstText + 1):
        stillfirstText = stillfirstText - intValue
        messagebox.showinfo('Ошибка', ("Столько билетов нет"))
        enterFirstText.delete(0, 'end')
    else:
        stillfirstText = stillfirstText - intValue
        amountOfMoney = amountOfMoney - intValue*priceForFirstFilm
        print(amountOfMoney)
        messagebox.showinfo('Успешно', ("Вы купили билет(ы)"))
        enterFirstText.delete(0, 'end')
        onDisplayMoney.config(text=f"У вас на карте: {str(amountOfMoney)}")
        onStillFirstText.config(text=f"Осталось билетов: {str(stillfirstText)}")

def toChangeAmountOfTicketsAndChangeAmountMoneySecondButton ():
    value = secondEnterText.get()
    intValue = int(value)
    global stillfirstText
    global stillsecondText
    global amountOfMoney

    if (intValue == 0):
        stillsecondText = stillsecondText - intValue
        messagebox.showinfo('Ошибка', ("Вы ничего не приобрели"))
        secondEnterText.delete(0, 'end')
    elif (intValue > stillsecondText + 1):
        stillsecondText = stillsecondText - intValue
        messagebox.showinfo('Ошибка', ("Столько билетов нет"))
        secondEnterText.delete(0, 'end')
    else:
        stillsecondText = stillsecondText - intValue
        amountOfMoney = amountOfMoney - intValue*priceForSecondFilm
        print(amountOfMoney)
        messagebox.showinfo('Успешно', ("Вы купили билет(ы)"))
        secondEnterText.delete(0, 'end')
        onDisplayMoney.config(text=f"У вас на карте: {str(amountOfMoney)}")
        onStillSecondText.config(text=f"Осталось билетов: {str(stillsecondText)}")


# Каркас
window = Tk()
window.resizable(width=False, height=False)
window.title('Приложение кинотеатра')
window.geometry('520x360')
window['bg'] = 'white'


#Названия фильмов
firstText = Label(window, text = 'Чебурашка', font = ('Arial Bold', 15), fg = 'black', bg = 'white')
firstText.place(x = 25, y = 10)

secondText = Label(window, text = 'Титаник', font = ('Arial Bold', 15), fg = 'black', bg = 'white')
secondText.place(x = 25, y = 100)


# Надписи для полей ввода

#Сколько осталось билетов у фильмов
# stillfirstText = 3
# stillsecondText = 2

#Цена за фильмы
priceForFirstFilm = 250
priceForSecondFilm = 100

onStillFirstText = Label(window, text = f"Осталось билетов: {str(stillfirstText)}", font = ('Arial Bold', 15), fg = 'black', bg = 'white')
onStillFirstText.place(x = 200, y = 55)

onStillPriceFirstText = Label(window, text = f"Цена: {str(priceForFirstFilm)}", font = ('Arial Bold', 15), fg = 'black', bg = 'white')
onStillPriceFirstText.place(x = 200, y = 25)

onStillSecondText = Label(window, text = 'Осталось билетов: ' + str(stillsecondText), font = ('Arial Bold', 15), fg = 'black', bg = 'white')
onStillSecondText.place(x = 200, y = 155)

onStillPriceSecondText = Label(window, text = 'Цена ' + str(priceForSecondFilm), font = ('Arial Bold', 15), fg = 'black', bg = 'white')
onStillPriceSecondText.place(x = 200, y = 125)

# Поля для ввода

enterFirstText = Entry(fg='black', width=25)
enterFirstText.place(x = 35, y = 60)

secondEnterText = Entry(fg='black', width=25)
secondEnterText.place(x = 35, y = 160)

#Денег на карте
amountOfMoney = 1000

onDisplayMoney = Label(window, text = f"У вас на карте: {str(amountOfMoney)}", font = ('Arial Bold', 15), fg = 'black', bg = 'white')
onDisplayMoney.place(x = 25, y = 200)

# Кнопки
btn = Button(window, text = 'Купить', command = toChangeAmountOfTicketsAndChangeAmountMoneyFirstButton, width= '10', height='1', fg='blue', bg = 'white' )
btn.place(x = 310, y = 25)

btn = Button(window, text = 'Купить', command = toChangeAmountOfTicketsAndChangeAmountMoneySecondButton, width= '10', height='1', fg='blue', bg = 'white' )
btn.place(x = 310, y = 125)
window.mainloop()