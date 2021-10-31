from main import *
pygame.init()
f=pygame.display.set_mode((taille_echec*100,100))
fps=pygame.time.Clock()
font=pygame.font.SysFont('DejaVu Sans',100,bold=True)

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
