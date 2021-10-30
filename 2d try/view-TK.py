import tkinter as tk
import main

def colorize(to_blick=[]):
    for ind,label in enumerate(buttons):
        pos=divmod(ind,8)[::-1]
        buttons[ind]['text']=main.plato[pos].repr
        buttons[ind]['foreground']="#ffffff" if main.plato[pos].clan=="B" else "#000000"
        if pos in to_blick:
            buttons[ind]["background"]="#FBD9B5" if (pos[0]+pos[1])%2 else "#FFFBE7"
        else:
            buttons[ind]["background"]="#1C1AAF" if (pos[0]+pos[1])%2 else "#605FC7"
def changefor(e):
    f.title(f'{int(e.x/40*8)} {int(e.y/40*8)}')
    #colorize(main.on_click(plac))
    
f=tk.Tk()
f.title('Chess by momoladebrouill')
buttons=[]
for pos,piece in main.plato:
    but=tk.Label(f,text=piece.repr,
                  font="Consolas 25 bold",width=2)
    but.grid(row=pos[1],column=pos[0])
    buttons.append(but)
f.bind('<Button-1>',changefor)
colorize()

        
