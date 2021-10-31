import tkinter as tk
from random import random
from colorsys import hsv_to_rgb
from functools import partial
from main import *
hsv=lambda  h,s: "#%02x%02x%02x" % tuple(int(c) for c in hsv_to_rgb(h,s,150))
maincoul=random()
def colorize(to_blick=[]):
    for ind,but in enumerate(buttons):
        tuplepos=divmod(ind,8)[::-1]
        pos=Pos(tuplepos[0],tuplepos[1])
        buttons[ind]['text']=plato[pos].repr #f'{label.grid_info()["row"]}{label.grid_info()["column"]}'
        buttons[ind]['foreground']="#ffffff" if plato[pos].clan=="B" else "#000000"
        if pos in to_blick:
            buttons[ind]["relief"]="sunken"
            buttons[ind]["background"]= hsv(maincoul,1) if (pos[0]+pos[1])%2 else hsv(1-maincoul,1)
        else:
            buttons[ind]["relief"]="flat"
            buttons[ind]["background"]= hsv(maincoul,.5) if (pos[0]+pos[1])%2 else hsv(1-maincoul,.5)
def changefor(e):
    if type(e)==tuple:
        colorize(on_click(e))
    
f=tk.Tk()
f.title('Chess by momoladebrouill')
buttons=[]
for pos,piece in plato:
    but=tk.Button(f,text=piece.repr,
                  font="Consolas 25",width=3,height=1,
                  command=partial(changefor, pos))
    but.grid(row=pos[1],column=pos[0])
    buttons.append(but)

f.bind('<Button-1>',changefor)
colorize()


        
