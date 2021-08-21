from main import *
import tkinter as tk

f=tk.Tk()
#l=tk.Label(f,text=,font="Consolas 200")
#l.pack()
#l["background"]="#ff0000"
#l.bind('<Button-1>',lambda e: print('grr'))
labels=[tk.Label(f,text=i.repr,font="Consolas 50",width=2) for i in echequier]
for place,label in enumerate(labels):
    label.grid(column=place,row=0)
    label.pack_propagate(0)
    label.bind('<Button-1>',lambda e:changefor(e))
def changefor(e):
    #for place,label in enumerate(labels):
     #   label["background"]="#ffffff" if place%2 else "#000000"
    plac=str(e.widget)[-1]
    plac= (0 if plac=="l" else int(plac)-1)
    to_blick=on_click(plac)
    for pos in range(8):
        labels[pos]['text']=echequier[pos].repr
        if pos in to_blick:
            labels[pos]['background']="#aa00aa"
        else:
            labels[pos]['background']="#aaaaaa"
        
