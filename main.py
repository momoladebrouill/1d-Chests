import random,math,pygame
taille_echec=8

class Pion:
    def __init__(self,clan,pos):
        self.clan=clan
        self.pos=pos
    __repr__=lambda self : f"{self.repr} {self.clan} {self.pos}"
    def can_goes(self):
        for i in self.moves:
            if 0<=self.pos+i<taille_echec:
                yield self.pos+i

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

echequier=[Vide(i) for i in range(taille_echec)]
ordre=[Roi,Cheval,Tour,Tour,Cheval,Roi]

for i in range(-3,3):
    echequier[i]=ordre[i](int(math.copysign(1,i)),
                          (taille_echec+i)%taille_echec)
pygame.init()
f=pygame.display.set_mode((taille_echec*100,100))
fps=pygame.time.Clock()
font=pygame.font.SysFont('Consolas',100,bold=True)
#pygame.font.SysFont(
B=True
highliters=[]
couls=[(50,0,0),(10,10,10)]
selected=False
player=1
while B:
    pygame.display.flip()
    fps.tick(60)
    f.fill(0)
    for i in range(taille_echec):
        pygame.draw.rect(f,couls[i%2],(i*100,0,100,100))
    for carre in highliters:
        pygame.draw.rect(f,(250,120,0),(carre*100,0,100,100))
    for pion in echequier:
        mot=font.render(pion.repr,0,(255,255,255) if pion.clan<0 else (255,0,0))
        f.blit(mot,(pion.pos*100,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            B=0
            pygame.quit()
        elif event.type==pygame.MOUSEBUTTONUP:
            if selected:
                if int(event.pos[0]/100) in highliters:
                    echequier[selected.pos],echequier[int(event.pos[0]/100)]=Vide(selected.pos),selected
                    selected.pos=int(event.pos[0]/100)
                    selected=False
                    highliters=[]
                    player=1 if player==-1 else -1
                else:
                    selected=False
                    highliters=[]
                    
            else:
                selected=echequier[int(event.pos[0]/100)]
                if selected.clan!=player:
                    selected=False
                else:
                    highliters=list(selected.can_goes())
            
                
            
pygame.quit()
