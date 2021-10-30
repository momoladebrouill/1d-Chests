import random,math
taille_echec=8
selected=False
player=1
highliters=[]

class Echqier():
    def __init__(self,taillex=8,tailley=8):
        self.array=["_" for _ in range(taillex*tailley)]
        self.larg=taillex
        self.haut=tailley
        self.total=taillex*tailley
    def __repr__(self):
        t=""
        for i in range(self.total):
            if i%self.larg==0:
                t+="\n"
            t+=str(self.array[i])+" "
        return t
    def __getitem__(self,pos):
        x,y=(pos.x,pos.y) if type(pos)==Pos else pos
        return self.array[self.larg*y+x]
    def __contains__(self,pos):
        return -1<pos.x<self.larg and -1<pos.y<self.haut
    def __setitem__(self,pos,item):
        if type(pos)==Pos:
            x,y=pos.x,pos.y
        else:
            x,y=pos
        self.array[self.larg*y+x]=item
    def __iter__(self):
        self.it=0
        return self
    def __next__(self):
        try:
            self.it+=1
            return divmod(self.it-1,self.larg)[::-1],self.array[self.it-1]
        except IndexError:
            raise StopIteration
        

class Pos():
    def __init__(self,x,y):
        self.x,self.y=x,y
    def __add__(self,other):
        if type(other)==type(self):
            self.x+=other.x
            self.y+=other.y
        else:
            self.x+=other[0]
            self.y+=other[1]
    def __repr__(self):
        return str(self.x)+str(self.y)
    def __mul__(self,fac):
        return Pos(self.x*fac,self.y*fac)
    def __getitem__(self,num):
        return [self.x,self.y][num]


class Pion():
    def __init__(self,clan,pos):
        self.clan=clan
        self.pos=pos
    
    def can_goes(self):
        for i in self.moves:
            if 0<=self.pos+i<taille_echec:
                yield self.pos+i
    
    __repr__=lambda self : f"{self.repr} {self.clan} {self.pos}"
class Esclave(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♟"
        self.moves=[(0,-1 if self.clan=="B" else 1)]

class Roi(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♔"
        self.moves=[
            (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)
            ]
        
class Tour(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♖"
    def can_goes(self):
        for der in [(-1,0),(1,0),(0,-1),(0,1)]:
            av=1 # Nombre de jour de croisade
            camp=self.pos+Pos(der[0],der[1])*av # Lieu de campement
            while camp in plato:
                yield camp
                av+=1
                camp=self.pos+Pos(der[0],der[1])*av
class Fou(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♝"
    def can_goes(self):
        for der in [(-1,-1),(1,1),(1,-1),(-1,1)]:
            av=1 # Nombre de jour de croisade
            camp=self.pos+Pos(der[0],der[1])*av # Lieu de campement
            while camp in plato:
                yield camp
                av+=1
                camp=self.pos+Pos(der[0],der[1])*av
class Reine(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♕"
    def can_goes(self):
        for der in [(-1,-1),(1,1),(1,-1),(-1,1),(-1,0),(1,0),(0,-1),(0,1)]:
            av=1 # Nombre de jour de croisade
            camp=self.pos+Pos(der[0],der[1])*av # Lieu de campement
            while camp in plato:
                yield camp
                av+=1
                camp=self.pos+Pos(der[0],der[1])*av
                    
class Cheval(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♘"
        self.moves=[
            (2,1),(2,-1),(-2,1),(-2,-1),
            (1,2),(1,-2),(-1,2),(-1,-2)]
    
        
class Vide(Pion):
    def __init__(self,pos):
        super().__init__(' ',0)
        self.repr=" "
        self.clan=0
        self.moves=[]
        self.pos=pos
    #__repr__=lambda self : "_"

    
def on_click(pos):
    global selected, player,highliters
    if selected:
        if pos in highliters:
            plato[selected.pos],plato[pos]=Vide(selected.pos),selected
            selected.pos=pos
            selected=False
            player=1 if player==-1 else -1
        else:
            selected=False
        highliters=[]
                    
    else:
        selected=plato[pos]
        if selected.clan!=player:
                selected=False
        else:
            highliters=list(selected.can_goes())
    return highliters
    
plato=Echqier()
for y in range(8):
    for x in range(8):
        plato[x,y]=Vide(Pos(y,x))
ordre=[Tour,Cheval,Fou,Reine,Roi,Fou,Cheval,Tour]
for ind,typ in enumerate(ordre):
    plato[ind,0]=typ("B",Pos(ind,0))
    plato[ind,1]=Esclave("B",Pos(ind,1))
for ind,typ in enumerate(ordre[::-1]):
    plato[ind,-1]=typ("N",Pos(ind,plato.haut-1))
    plato[ind,-2]=Esclave("N",Pos(ind,plato.haut-2))

#for i in range(-3,3):echequier[i]=ordre[i](int(math.copysign(1,i)),(taille_echec+i)%taille_echec)
