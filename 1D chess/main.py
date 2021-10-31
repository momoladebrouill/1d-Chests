import random,math
taille_echec=8
selected=False
player=1
highliters=[]
class Pion:
    def __init__(self,clan,pos):
        self.clan=clan
        self.pos=pos
    
    def can_goes(self):
        for i in self.moves:
            if 0<=self.pos+i<taille_echec:
                yield self.pos+i
    
    __repr__=lambda self : f"{self.repr} {self.clan} {self.pos}"

class Roi(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♔"
        self.moves=[-1,1]
        
class Tour(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♖"
    def can_goes(self):
        for der in range(-1,2,2):
            av=1
            while 0<=self.pos+der*av<taille_echec:
                
                if type(echequier[self.pos+der*(av-1)])==Vide or echequier[self.pos+der*(av-1)]==self:
                    yield self.pos+der*av
                else:
                    break
                av+=1
                    
class Cheval(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♘"
        self.moves=[-2,2]
    
        
class Vide(Pion):
    def __init__(self,pos):
        super().__init__(' ',0)
        self.repr=" "
        self.clan=0
        self.moves=[]
        
    __repr__=lambda self : " "

    
def on_click(pos):
    global selected, player,highliters
    if selected:
        if pos in highliters:
            echequier[selected.pos],echequier[pos]=Vide(selected.pos),selected
            selected.pos=pos
            selected=False
            player=1 if player==-1 else -1
        else:
            selected=False
        highliters=[]
                    
    else:
        selected=echequier[pos]
        if selected.clan!=player:
                selected=False
        else:
            highliters=list(selected.can_goes())
    return highliters
    
echequier=[Vide(i) for i in range(taille_echec)]
ordre=[Roi,Cheval,Tour,Tour,Cheval,Roi]

for i in range(-3,3):
    echequier[i]=ordre[i](int(math.copysign(1,i)),
                          (taille_echec+i)%taille_echec)
