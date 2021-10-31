

selected=False
player="B"
highliters=[]

class Echqier():
    def __init__(self,taillex=8,tailley=8):
        self.array=["_" for _ in range(taillex*tailley)]
        self.larg=taillex
        self.haut=tailley
        self.total=taillex*tailley
    def __repr__(self):
        t="+"+"- "*16+"+"
        for i in range(self.total):
            if i%self.larg==0:
                t+="|\n|"
            t+=str(self.array[i])+" "
        t+="|\n+--------+"
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
        return Pos(self.x+other.x,self.y+other.y) if type(other)==Pos else Pos(self.x+other[0],self.y+other[1])
    def __repr__(self):
        return str(self.x)+str(self.y)
    def __mul__(self,fac):
        return Pos(self.x*fac,self.y*fac)
    def __getitem__(self,num):
        return [self.x,self.y][num]
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y


class Pion():
    def __init__(self,clan,pos):
        self.clan=clan
        self.pos=pos
    
    def can_goes(self):
        if self.movetype=="until_meet":
            for der in self.moves:
                av=1 # Nombre de jour de croisade
                camp=self.pos+Pos(der[0],der[1])*av # Lieu de campement
                while camp in plato:
                    if plato[camp].clan==self.clan:
                        break
                    elif type(plato[camp])!=Vide:
                        yield camp
                        av+=1
                        camp=self.pos+Pos(der[0],der[1])*av
                        break
                    else:
                        yield camp
                        av+=1
                        camp=self.pos+Pos(der[0],der[1])*av
                    
        elif self.movetype=="absolute":
            for i in self.moves:
                if self.pos+i in plato:
                    if plato[self.pos+i].clan!=self.clan:
                        yield self.pos+i
        else:
            return []
    
    __repr__=lambda self : f"{self.repr}{self.clan}"
class Esclave(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♟"
        self.movetype="absolute"
        self.moves=[(0,-1 if self.clan=="N" else 1)]
        

class Roi(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♔"
        self.movetype="absolute"
        self.moves=[
            (-1,-1),(-1,0),(-1,1),(0,-1),
            (0,1),(1,-1),(1,0),(1,1)
            ]
        
class Tour(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♖"
        self.movetype="until_meet"
        self.moves=[(-1,0),(1,0),(0,-1),(0,1)]
    
class Fou(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♝"
        self.movetype="until_meet"
        self.moves=[(-1,-1),(1,1),(1,-1),(-1,1)]
   
class Reine(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♕"
        self.movetype="until_meet"
        self.moves=[(-1,-1),(1,1),(1,-1),(-1,1),(-1,0),(1,0),(0,-1),(0,1)]
        
                    
class Cheval(Pion):
    def __init__(self,clan,pos):
        super().__init__(clan,pos)
        self.repr="♘"
        self.movetype="absolute"
        self.moves=[
            (2,1),(2,-1),(-2,1),(-2,-1),
            (1,2),(1,-2),(-1,2),(-1,-2)
            ]
    
        
class Vide(Pion):
    def __init__(self):
        super().__init__(" ",None)
        self.repr=" "
        self.movetype="No"
        self.moves=[]
    #__repr__=lambda self : "_"

    
def on_click(pos):
    global selected, player,highliters
    #highliters=list(plato[pos].can_goes())
    tuplepos=pos
    pos=Pos(tuplepos[0],tuplepos[1])
    if selected:
        if pos in highliters:
            plato[selected.pos],plato[pos]=Vide(),selected
            selected.pos=pos
            selected=False
            player="B" if player=="N" else "N"
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
        plato[x,y]=Vide()
        
ordre=[Tour,Cheval,Fou,Reine,Roi,Fou,Cheval,Tour]
for ind,typ in enumerate(ordre):
    plato[ind,0]=typ("B",Pos(ind,0))
    plato[ind,1]=Esclave("B",Pos(ind,1))
for ind,typ in enumerate(ordre[::-1]):
    plato[ind,-1]=typ("N",Pos(ind,plato.haut-1))
    plato[ind,-2]=Esclave("N",Pos(ind,plato.haut-2))

