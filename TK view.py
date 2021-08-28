from main import *
import tkinter as tk

f=tk.Tk()
#l=tk.Label(f,text=,font="Consolas 200")
#l.pack()
#l["background"]="#ff0000"
#l.bind('<Button-1>',lambda e: print('grr'))
labels=[tk.Button(f,text=i.repr,font="Consolas 50 bold",width=2) for i in echequier]

for place,label in enumerate(labels):
    label.grid(column=place,row=0)
    label.pack_propagate(0)
    label.bind('<Button-1>',lambda e:changefor(e))
    
def colorize(to_blick=[]):
    for pos,label in enumerate(labels):
        labels[pos]['text']=echequier[pos].repr
        labels[pos]['foreground']="#ffffff" if echequier[pos].clan==1 else "#000000"
        if pos in to_blick:
            labels[pos]["background"]="#FBD9B5" if pos%2 else "#FFFBE7"
        else:
            labels[pos]["background"]="#1C1AAF" if pos%2 else "#605FC7"

def changefor(e):
    plac=str(e.widget)[-1]
    plac= (0 if plac=="l" else int(plac)-1)
    colorize(on_click(plac))

colorize()

        
