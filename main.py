#!/usr/bin/env python3

from tkinter import *
#algorithm from the Book "Algorithmen und Problemlösungen in C++" by Donia Logofaku

def prim():

    try:
        i=int(eintrag.get())
        if i == 1:
            ausgabe["text"] = "1 ist Keine Primzahl"
        elif i>2 and i%2==0:
            ausgabe["text"]="Ist zusammengestezt"
        else:
            n=3
            isprim=True
            while isprim and n*n <=i:
                    if i%n==0:
                        isprim = False
                    else:
                        n+=2
            if isprim==True:
                ausgabe["text"]="ist eine Primzahl"
            else:
                ausgabe["text"]="ist zusammengestezt"


    except ValueError:
        ausgabe["text"]="Keine natürliche Zahl"




master=Tk()
master.geometry("500x500")
master.title("Primzahlen Rechner")
frame=Frame(master)
frame.pack()

eintrag=Entry(master,width=20)
eintrag.pack(padx=5,pady=5)

ausgabe=Label(master,text='Ergebnis',background='white',justify='center',width=20)
ausgabe.pack()


button=Button(master,text="Rechne",command = prim)
button.place(relx=0.5,rely=0.5,y=10, anchor = CENTER)

master.mainloop()




