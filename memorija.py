
from tkinter import *
from tkinter import messagebox
import random
import tkinter

dictionaryGlobal = {}

root = Tk()
root.title("Memory game")

button_list = []

openedButtons = []


def generate_random_num():
    number_list = []
    i = 0
    while i < 18:
        n = random.randint(0, 100)
        """ posto je broj nasumican moze se vratiti broj koji vec imam pa nam to ne valja i ovako radimo da nam vrace novi broj sve dok ne vrati
        broj koji nemamo u listi"""
        while n in number_list:
            n = random.randint(0, 100)
        number_list.append(n)
        number_list.append(n)
        i += 1
    return number_list


def autoGenerateButton():
    i = 0
    while i < 36:
        buttonName = "button" + str(i)
        button = tkinter.Button(root, text=str(
            i), height=7, width=14, name=buttonName)
        button.grid(row=i/6, column=(i == 0 and 0 or i % 6))
        button_list.append(button)
        i += 1


def add_buttons():
    button1 = Button(root, text="", height=7, width=14)
    button1.config(command=lambda: valueByButtonName("button1", button1))

    button2 = Button(root, text="", height=7, width=14)
    button2.config(command=lambda: valueByButtonName("button2", button2))

    button3 = Button(root, text="", height=7, width=14)
    button3.config(command=lambda: valueByButtonName("button3", button3))

    button4 = Button(root, text="", height=7, width=14)
    button4.config(command=lambda: valueByButtonName("button4", button4))

    button5 = Button(root, text="", height=7, width=14)
    button5.config(command=lambda: valueByButtonName("button5", button5))

    button6 = Button(root, text="", height=7, width=14)
    button6.config(command=lambda: valueByButtonName("button6", button6))

    button7 = Button(root, text="", height=7, width=14)
    button7.config(command=lambda: valueByButtonName("button7", button7))

    button8 = Button(root, text="", height=7, width=14)
    button8.config(command=lambda: valueByButtonName("button8", button8))

    button9 = Button(root, text="", height=7, width=14)
    button9.config(command=lambda: valueByButtonName("button9", button9))

    button10 = Button(root, text="", height=7, width=14)
    button10.config(command=lambda: valueByButtonName("button10", button10))

    button11 = Button(root, text="", height=7, width=14)
    button11.config(command=lambda: valueByButtonName("button11", button11))

    button12 = Button(root, text="", height=7, width=14)
    button12.config(command=lambda: valueByButtonName("button12", button12))

    button13 = Button(root, text="", height=7, width=14)
    button13.config(command=lambda: valueByButtonName("button13", button13))

    button14 = Button(root, text="", height=7, width=14)
    button14.config(command=lambda: valueByButtonName("button14", button14))

    button15 = Button(root, text="", height=7, width=14)
    button15.config(command=lambda: valueByButtonName("button15", button15))

    button16 = Button(root, text="", height=7, width=14)
    button16.config(command=lambda: valueByButtonName("button16", button16))

    button17 = Button(root, text="", height=7, width=14)
    button17.config(command=lambda: valueByButtonName("button17", button17))

    button18 = Button(root, text="", height=7, width=14)
    button18.config(command=lambda: valueByButtonName("button18", button18))

    button19 = Button(root, text="", height=7, width=14)
    button19.config(command=lambda: valueByButtonName("button19", button19))

    button20 = Button(root, text="", height=7, width=14)
    button20.config(command=lambda: valueByButtonName("button20", button20))

    button21 = Button(root, text="", height=7, width=14)
    button21.config(command=lambda: valueByButtonName("button21", button21))

    button22 = Button(root, text="", height=7, width=14)
    button22.config(command=lambda: valueByButtonName("button22", button22))

    button23 = Button(root, text="", height=7, width=14)
    button23.config(command=lambda: valueByButtonName("button23", button23))

    button24 = Button(root, text="", height=7, width=14)
    button24.config(command=lambda: valueByButtonName("button24", button24))

    button25 = Button(root, text="", height=7, width=14)
    button25.config(command=lambda: valueByButtonName("button25", button25))

    button26 = Button(root, text="", height=7, width=14)
    button26.config(command=lambda: valueByButtonName("button26", button26))

    button27 = Button(root, text="", height=7, width=14)
    button27.config(command=lambda: valueByButtonName("button27", button27))

    button28 = Button(root, text="", height=7, width=14)
    button28.config(command=lambda: valueByButtonName("button28", button28))

    button29 = Button(root, text="", height=7, width=14)
    button29.config(command=lambda: valueByButtonName("button29", button29))

    button30 = Button(root, text="", height=7, width=14)
    button30.config(command=lambda: valueByButtonName("button30", button30))

    button31 = Button(root, text="", height=7, width=14)
    button31.config(command=lambda: valueByButtonName("button31", button31))

    button32 = Button(root, text="", height=7, width=14)
    button32.config(command=lambda: valueByButtonName("button32", button32))

    button33 = Button(root, text="", height=7, width=14)
    button33.config(command=lambda: valueByButtonName("button33", button33))

    button34 = Button(root, text="", height=7, width=14)
    button34.config(command=lambda: valueByButtonName("button34", button34))

    button35 = Button(root, text="", height=7, width=14)
    button35.config(command=lambda: valueByButtonName("button35", button35))

    button36 = Button(root, text="", height=7, width=14)
    button36.config(command=lambda: valueByButtonName("button36", button36))

    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=0, column=3)
    button5.grid(row=0, column=4)
    button6.grid(row=0, column=5)
    button7.grid(row=1, column=0)
    button8.grid(row=1, column=1)
    button9.grid(row=1, column=2)
    button10.grid(row=1, column=3)
    button11.grid(row=1, column=4)
    button12.grid(row=1, column=5)
    button13.grid(row=2, column=0)
    button14.grid(row=2, column=1)
    button15.grid(row=2, column=2)
    button16.grid(row=2, column=3)
    button17.grid(row=2, column=4)
    button18.grid(row=2, column=5)
    button19.grid(row=3, column=0)
    button20.grid(row=3, column=1)
    button21.grid(row=3, column=2)
    button22.grid(row=3, column=3)
    button23.grid(row=3, column=4)
    button24.grid(row=3, column=5)
    button25.grid(row=4, column=0)
    button26.grid(row=4, column=1)
    button27.grid(row=4, column=2)
    button28.grid(row=4, column=3)
    button29.grid(row=4, column=4)
    button30.grid(row=4, column=5)
    button31.grid(row=5, column=0)
    button32.grid(row=5, column=1)
    button33.grid(row=5, column=2)
    button34.grid(row=5, column=3)
    button35.grid(row=5, column=4)
    button36.grid(row=5, column=5)


def dictionary(list):
    i = 0
    """dinamicki pravimo dictionary tako sto nam je key string button plus vrijednosto od 1 do 36"""
    while i < 36:
        buttName = "button"+str(i+1)
        dictionaryGlobal[buttName] = str(list[i])
        i += 1


def valueByButtonName(buttonName, buttonObj):
    """ovo nam je lista otvorenih buttona,ovo nam treba da bi pamtio trenutno otvorene buttone  i provjeravamo da li su im isti brojevii posle je praznimo."""
    global openedButtons
    """odje provjeravamo da li je dugme na koje je kliknuto zatvoreno odnosno da li je tekst prazan,ako jeste onda ga "otkirvamo" tj. dajemo muvrijednost"""
    if buttonObj['text'] == "":
        buttonObj.configure(text=dictionaryGlobal.get(buttonName))
    else:
        return

    if len(openedButtons) == 0:
        openedButtons.append(buttonObj)
    elif len(openedButtons) == 2:
        openedButtons[0].configure(text="")
        openedButtons[1].configure(text="")
        openedButtons = []
        openedButtons.append(buttonObj)
        """ovo else je slucaj kad je vec otvoreno jedno dugme(button) i sad smo otvorili drugo pa provjeramo prvo jesu li isti brojevi tj jesu li im tekstovi isti ako jesu znaci imamo pogodak, polja su otvorena i uklanjam im komandu onclick,tj tu metodu koja je bila vezana za njih jer oni vise ne igraju"""
    else:
        openedButton = openedButtons[0]
        if(openedButton["text"] == buttonObj["text"]):
            buttonObj.configure(command=lambda: None)
            openedButton.configure(command=lambda: None)
            openedButton.configure(bg='green')
            buttonObj.configure(bg='green')
            openedButtons = []
        else:
            openedButtons.append(buttonObj)


def main():
    """prvo pravimo buttone i postavljamo ih """
    add_buttons()
    """ onda pravimo listu od 2 puta po 18 jedinstvenih brojeva"""
    shuffle_list = generate_random_num()
    """shuffle"""
    random.shuffle(shuffle_list)
    """napravimo dictionary da povezemo buttone i brojeve"""
    dictionary(shuffle_list)
    root.mainloop()


print(main())
