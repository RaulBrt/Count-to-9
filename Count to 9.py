##|==============================================================================|
##|                                  COUNT TO 9                                  |
##|                                                                              |
##|                              Feito pelo Grupo 8                              |
##|                                                                              |
##|                              Raul Teixeira Berto                             |
##|                            Matheus Cheleagao Silva                           |
##|                             Sergio Ricardo Salgado                           |
##|==============================================================================|

#SFX = Efeitos de som
#VFX = Efeitos visuais




#BIBLIOTECAS============================================================================================


import pygame, math, time, sys
from pygame.locals import *
import random



#FUNÇÕES================================================================================================
def makedeck(): #Função para colocar cartas no deck
        global deck
        count = 0
        while(count<4):
                turn = 0					   	
                while(turn<10):	           ##	 	
                        deck.append(count) ##Colocar 10 cartas com valor "count no deck"
                        turn+=1            ##
                count+=1 #Aumentar o valor de "Count"
def dealcards(): #Função para distribuir as cartas
        global hand
        count = 0
        turn = 0
        while(count<4):
                while(turn<len(players)):                                                ##
                        hand[turn].append(int(deck.pop(random.randint(0,len(deck)-1))))  ##Dar tira uma carta de indice aleatorio da lista "deck" e coloca na lista "hand" de indice "turn"
                        turn+=1                                                          ##Repetir o processo 4 vezes
                turn=0
                count+=1
        turn=0
        while(turn<len(players)): ##Organizar as mãos dos jogadores, ajuda com a visualização e é necessario para o computador escolher qual carta jogar
                hand[turn].sort()
                turn+=1
def checkcard(hold): #Função para verificar qual foi a carta escolhida pelos jogadores
        if(hold>-9):
                if (hold==0):
                        card = carta0
                elif (hold==1):
                        card = carta1
                elif (hold==2):
                        card = carta2
                elif (hold==3):
                        card = carta3
                else:
                    card = backver
                return card
        else:
            return backver

def drawhand1(): #Função para desenhar na tela a mão do jogador 1
        count = 24*casa #casa = 16 pixels, conta utilizada para facilitar o posicionamento dos elementos na tela
        top = 37 #Coordenada y do topo das cartas
        screen.blit(tag1,(36*casa,33*casa)) #Desenha o nome do jogador acima da mão
        for i in range(0,len(hand[0])):
        		carta = hand[0][i]
        		top = 37
        		if (cursor[1] in range(top*casa,res[1])):
        			if (cursor[0] in range(count,count+8*casa)):#Se o mouse estiver sobre a carta que esta sendo desenhada, a carta é desenhada 2 casas acima
        				top-=2
        		screen.blit(checkcard(carta),(count,top*casa))#Desenha a carta
        		count+=8*casa#Passa para a posiçao da proxima carta
def drawhand2(): #Função para desenhar na tela a mão do jogador 2
       if("2" in players): #Se o jogador 2 ainda estiver no jogo
                count=6*casa
                screen.blit(tag2,(12*casa,18*casa))#Desenha o nome do jogador
                for i in range(1,len(hand[players.index("2")])):
                        screen.blit(backhor,(-2*casa,count))#Desenha uma carta virada de acordo com o numero de cartas na mao do jogador
                        count+=8*casa
def drawhand3(): #Função para desenhar na tela a mão do jogador 3, funciona do mesmo jeito que a função "drawhand2" mudando apenas a posiçao das cartas
        if("3" in players):
                count=48*casa
                screen.blit(tag3,(36*casa,12*casa))
                for i in range(1,len(hand[players.index("3")])):
                        screen.blit(backver,(count,-2*casa))
                        count-=8*casa
def drawhand4():#Função para desenhar na tela a mão do jogador 4, funciona do mesmo jeito que a função "drawhand2" mudando apenas a posiçao das cartas
        if("4" in players):
                count=30*casa
                screen.blit(tag4,(67*casa,18*casa))
                for i in range(1,len(hand[players.index("4")])):
                        screen.blit(backhor,(70*casa,count))
                        count-=8*casa
def player():#Turno do jogador
        index=4
        global turno
        global start
        pygame.draw.rect(screen,white,(37*casa,33*casa,7*casa,1.5*casa))#"Acende" o nome do jogador 1
        screen.blit(tag1,(36*casa,33*casa))#Desenha o nome do jogador acima do retangulo
        if (len(hand[0]) == 0):#Se o jogador não tiver cartas na mão
                players.pop(turno) #Remove o jogador "turno" da lista de jogadores
                soma.append(20) #Coloca o numero 20 na lista de cartas jogadas
                win = False
        else:
            if (1 in click): #Se o jogador pressionou algum botão do mouse
                    pos=cursor #Verificar a posição do cursor
                    if(pos[1]>=37*casa):#Se a coordenada y do mouse estiver abaixo do topo das cartas
                            pygame.mixer.Sound.play(slip) #SFX
                            if(pos[0] in range (24*casa,32*casa)): #Verificar coordenada x do mouse
                                    index=0
                            elif(pos[0] in range (32*casa+1,40*casa) and len(hand[0])>=2):
                                    index=1
                            elif(pos[0] in range (40*casa+1,48*casa) and len(hand[0])>=3):
                                    index=2
                            elif(pos[0] in range (48*casa+1,56*casa) and len(hand[0])>=4):
                                    index=3
            if (index<4):
                    if (len(hand[0])>0):
                            soma.append(hand[turno].pop(index))#Tira a carta selecionada da mão e coloca na mesa
                            if(sum(soma)>9):#Se a soma das cartas na mesa for maior que 9, remover o jogador "turno" do jogo
                                    players.pop(turno)
                            turno+=1 #Passa o turno
                            start = pygame.time.get_ticks()#Inicia o cronometro para o proximo jogador
def drawdiscard():#Desenha as cartas da pilha de descarte
        screen.blit(backbig,(21*casa,16*casa))#Carta virada
        if (len(soma)>0 and soma[-1]>-9):
                screen.blit(checkcard(soma[-1]),(51*casa,16*casa))#Ultima carta jogada
        if (len(soma)>1):
                screen.blit(checkcard(soma[-2]),(41*casa,16*casa))#Penultima carta jogada
        if (len(soma)>2):
                screen.blit(checkcard(soma[-3]),(31*casa,16*casa))#Antepenultima carta jogada
def ai():#Turnos do computador
        global hand
        global turno
        global players
        global start
        global wait
        if (len(hand[turno])==0 or hand[turno][-1]==-9):#Se o jogador "turno" nao tiver mais cartas na mao, remover ele da lista e recomeçaolr o jogo
                players.pop(turno)
                soma.append(20)
        else:
                count = -1
                if ("2" in players):#Se o jogador 2 ainda estiver jogando
                        i2 = players.index("2")#Verificar index do jogador 2
                        if (turno==i2):
                                pygame.draw.rect(screen,white,(12*casa,19*casa,1.5*casa,7*casa))#"Acende" o nome do jogador
                                screen.blit(tag2,(12*casa,18*casa))
                if ("3" in players):#Faz a mesma coisa que a condiçao acima
                        i3 = players.index("3")
                        if (turno==i3):
                                pygame.draw.rect(screen,white,(37*casa,12*casa,7*casa,1.5*casa))
                                screen.blit(tag3,(36*casa,12*casa))
                if ("4" in players):#Faz a mesma coisa que a condiçao acima
                        i4 = players.index("4")
                        if (turno==i4):
                                pygame.draw.rect(screen,white,(67*casa,19*casa,1.5*casa,7*casa))
                                screen.blit(tag4,(67*casa,18*casa))
                end = pygame.time.get_ticks()#verifica quamto tempo se passou desde o inicio do programa
                if(end-start>=wait):#Se tiver passado "wait" milissegundos desde o fim do ultimo turno
                        while((sum(soma)+hand[turno][count])>9):#Enquanto a soma da mesa mais a carta "selecionada" for maior que 9
                                if(hand[turno][count]!=-9):#Se a carta selecionada for diferente de -9
                                        count-=1#Seleciona uma carta diferente
                        global tst
                        tst = hand[turno][count]#Guarda na memoria a carta escolhida
                        pygame.mixer.Sound.play(slip)#SFX
                        soma.append(hand[turno].pop(count))#Joga a carta escolhida
                        if (tst == -9):#Se a carta escolhida for -9
                                transin()#VFX
                                players.remove(players[turno])#Remove o jogador de indice "turno" do jogo
                                soma.append(20)#Força o recomeço do jogo
                        turno+=1#Passa o turno
                        if (turno>len(players)-1):#Se o turno for maior que o numero de jogadores
                                turno=0#Passa o turno para o jogador de indice 0
                        start = pygame.time.get_ticks()#Recomeça o cronometro
                        wait = random.randint(500,3500)#Escolhe um tempo aleatorio de espera
def txt(text,size,posx,posy,cor):#Funçao para escrever coisas na tela
        fnt=pygame.font.Font("font/anderson_four_feather_falls.ttf",size)#Fonte
        fonte = pygame.font.SysFont(None,size)#Tamanho da fonte
        surface = fonte.render(text,True,cor)#Cria a superficie do texto
        txtrect = surface.get_rect()#Verifica o tamanho da caixa de texto
        txtrect.midtop = (posx+4.5*casa,posy)#Posiciona o meio do topo da caixa de texto
        screen.blit(surface,txtrect)#Desenha o texto
def game():#Loop do jogo
        while(len(players)>1 and players[0]=="1"):
                global hand
                global cursor
                global soma
                global click
                global turno
                global hand
                global win
                lose = False
                tst=0#Limpa a variavel tst
                soma = []#Lista de cartas jogadas (limpa a lista)
                hand=[[],[-9],[-9],[-9]]#Lista das listas das maos dos jogadores (limpa a lista) (-9 é necessario para computadores perderem)
                makedeck()#Coloca as cartas no deck
                dealcards()#Distribui as cartas
                turno = random.randint(0,len(players)-1)#Escolhe um jogador aleatoriamente para começar
                click = pygame.mouse.get_pressed()#Verifica estado dos botoes do mouse
                cursor = pygame.mouse.get_pos()#Verifica posiçao do mouse
                transout()#VFX
                while(sum(soma)<=9):#Enquanto ninguem tiver perdido (loop da rodada)
                        time.sleep(0.01)#Espera um pouco
                        if (tst < 0):#Se uma carta escolhida tiver valor negativo
                                break #Sai do loop da rodada
                        click = pygame.mouse.get_pressed()#Verifica botoes do mouse
                        cursor = pygame.mouse.get_pos()#Verifica posicao do mouse
                        screen.fill(black)
                        screen.blit(mesa, (0, 0))#Desenha a mesa
                        drawhand1()#Desenha a mao do jogador 1
                        drawhand2()#Desenha a mao do jogador 2
                        drawhand3()#Desenha a mao do jogador 3
                        drawhand4()#Desenha a mao do jogador 4
                        drawdiscard()#Desenha a pilha de descarte
                        screen.blit(chip,(57*casa,36*casa))#Desenha a ficha
                        txt(str(sum(soma)),120,57*casa,38*casa,(135,35,35))#Escreve o numero na fichq
                        if turno==0:
                                player()#Vez do jogador
                        else:
                                ai()#Vez do computador
                        pygame.display.update()#Atualizar tela
                        for event in pygame.event.get():
                                key = pygame.key.get_pressed()#Verifica input do teclado
                                if event.type == pygame.QUIT or key[K_ESCAPE]:#Se o botao x da janela ou se a tecla esc foram pressionados
                                        pygame.quit()#Fecha o modulo pygame
                                        sys.exit()#Fecha o sistema do python
                                if (key[K_f]):#Se a tecla f foi pressionada
                                        drawscreen()#Entra/sai do fullscreen
                if(len(players)==1):#Se somente tiver 1 jogador na mesa
                    win = True #Ganhou
                    transout()#VFX
                    break #Sai do loop de jogo
        if(players[0] != "1"):#Se o primeiro elemento da lista de jogadores nao for "1"
            win = False #Perdeu
            turno = 0
            transinnotxt() #VFX
            transout() #VFX
            pygame.mixer.music.stop() #Pare a musica que esta tocando
def menu():#Loop do menu
        global path
        screen.blit(mesa,(0,0))#Desenha a mesa
        screen.blit(logo,(26*casa,0*casa))#Desenha o logo
        txt("Tom Jobim - Garota de Ipanema",30,64*casa,43*casa,white)
        clk = pygame.mouse.get_pressed() #Verifica os botoes do mouse
        mousepos = pygame.mouse.get_pos() #Verifica a posiçao do mousr
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: #Se um botao for pressionado
                    transmenu() #VFX
                    path = "regras" #Passa para o loop das regras
                key = pygame.key.get_pressed()#Verifica teclas do teclado
                if event.type == pygame.QUIT or key[K_ESCAPE]:##Sai do jogo
                        pygame.quit()
                        sys.exit()
                if (key[K_f]):
                        drawscreen()#Entra/Sai do fullscreen
def regra():#loop das regras
        global path
        screen.blit(regras,(0,0))#Desenha as regras
        txt("Tom Jobim - Garota de Ipanema",30,64*casa,43*casa,white)
        pygame.display.update()#Atualiza a tela
        key = pygame.key.get_pressed()#Verifica teclas do teclado
        mousepos = pygame.mouse.get_pos()#Verifica posiçao do mouse
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:#Se um botao do mouse for pressionado
                        if (mousepos[0] in range(0,res[0]) and mousepos[1] in range(0,res[1])):#Se o mouse estiver dentro da tela do jogo
                                transreg()#VFX
                                path = "game" #Muda para o loop do jogo
                elif (event.type == pygame.QUIT or key[K_ESCAPE]):#Sai do jogo
                        pygame.quit()
                        sys.exit()
                if (key[K_f]):#Entra/sai do fullscreen
                        drawscreen()
def transmenu():#VFX (transiçao)
        contar = 0
        while(contar <= 960):#Enquanto "contar" for menor ou igual a 960
                count=res[0]#Posiçao do lado esquerdo da tela
                pygame.mixer.Sound.play(slip)#SFX
                while (True):#Loop infinito
                        screen.blit(mesa, (0, 0))#Desenhar a mesa
                        if (contar > 0):
                                screen.blit(cartatrans,(0,0))   #Desenhar as cartas que nao se movem
                        if (contar > 320):
                                screen.blit(cartatrans,(320,0))
                        if (contar > 640):
                                screen.blit(cartatrans,(640,0))
                        if (contar > 960):
                                screen.blit(cartatrans,(960,0))
                        screen.blit(cartatrans,(count,0))#Desenha uma carta na posiçao ("count",0)
                        count-=64 #Subtrair 64 de "count"
                        pygame.display.update()#Atualizar a tela
                        if (count < contar):#Se "count" for menor que "contar", Sai do loop infinito
                                    break
                contar+=res[0]/4 #Adiciona 1/4 do x da tela a "contar"
        cntr = 0
       #Remover as cartas da tela
        while (cntr > -1532):#Enquanto "cntr" for maior que -1532
                pygame.mixer.Sound.play(drag)#SFX
                screen.blit(regras, (0, 0))#Desenhar as regras
                screen.blit(curtain,(cntr,0))#Desenhar a "cortina"
                cntr-=32 #Subitrair 32 de "cntr"
                pygame.display.update()#Atualizar a tela
        pygame.mixer.Sound.stop(drag)#SFX
def transreg():#VFX (transiçao)
        contar = 0
        while(contar <= 960):
                count=res[0]
                pygame.mixer.Sound.play(slip)
                while (True):
                        screen.blit(regras, (0, 0))
                        if (contar > 0):
                                screen.blit(cartatrans,(0,0))
                        if (contar > 320):
                                screen.blit(cartatrans,(320,0))
                        if (contar > 640):
                                screen.blit(cartatrans,(640,0))
                        if (contar > 960):
                                screen.blit(cartatrans,(960,0))

                        screen.blit(cartatrans,(count,0))
                        count-=64
                        pygame.display.update()
                        if (count < contar):
                                    break;
                contar+=res[0]/4
def transin():#VFX (transiçao)
    contar = 0
    while(contar <= 960):
            count=res[0]
            pygame.mixer.Sound.play(slip)
            while (True): #Desenha a mesa, as maos, o descarte e a ficha
                    screen.blit(mesa, (0, 0))
                    drawhand1()
                    drawhand2()
                    drawhand3()
                    drawhand4()
                    drawdiscard()
                    screen.blit(chip,(57*casa,41*casa))
                    if (contar > 0):
                            screen.blit(cartatrans,(0,0))
                    if (contar > 320):
                            screen.blit(cartatrans,(320,0))
                    if (contar > 640):
                            screen.blit(cartatrans,(640,0))
                    if (contar > 960):
                            screen.blit(cartatrans,(960,0))
                    screen.blit(cartatrans,(count,0))
                    txt("Jogador {} perdeu".format(players[turno]),144,36*casa,20*casa,black)#Escreve um texto na tela informando que um jogador perdeu
                    count-=64
                    pygame.display.update()
                    if (count < contar):
                                break;
            contar+=res[0]/4
def transinnotxt():#VFX (transiçao)
    contar = 0
    while(contar <= 960):
            count=res[0]
            pygame.mixer.Sound.play(slip)
            while (True):
                    screen.blit(mesa, (0, 0))
                    drawhand1()
                    drawhand2()
                    drawhand3()
                    drawhand4()
                    drawdiscard()
                    screen.blit(chip,(57*casa,41*casa))
                    if (contar > 0):
                            screen.blit(cartatrans,(0,0))
                    if (contar > 320):
                            screen.blit(cartatrans,(320,0))
                    if (contar > 640):
                            screen.blit(cartatrans,(640,0))
                    if (contar > 960):
                            screen.blit(cartatrans,(960,0))
                    screen.blit(cartatrans,(count,0))
                    count-=64
                    pygame.display.update()
                    if (count < contar):
                                break;
            contar+=res[0]/4   
def transout():#VFX (transiçao)
        cntr = 0
        while (cntr > -1532):
                pygame.mixer.Sound.play(drag)
                screen.blit(mesa,(0,0))
                drawhand1()
                drawhand2()
                drawhand3()
                drawhand4()
                drawdiscard()
                screen.blit(chip,(57*casa,41*casa))
                screen.blit(curtain,(cntr,0))
                cntr-=64
                pygame.display.update()
        pygame.mixer.Sound.stop(drag)
def drawscreen():#Funçao entrar/sair do fullscreen
        global full
        if (full == False):
                screen=pygame.display.set_mode(res,FULLSCREEN, 32)#Tela em fullscreen
                full = True
        elif (full == True):
                screen=pygame.display.set_mode(res,0, 32)#Tela em modo janela
                full = False            


#Variaveis=====================================================================
full = True #Controla se o jogo está ou nao em fullscreen
black = (0,0,0) #Preto
white = (255,255,255)#Branco
players=["1","2","3","4"]#Lista dos jogadores ainda em jogo
deck=[]#Lista do deck
pygame.init() #Inicia o modulo pygame
pygame.font.init() #Inicia o modulo font (escrever na tela) do pygame
path = "menu" #Controla em qual loop o jogo está (menu,regras,game)
res = [1280,720]#Tamanho da tela
casa = 16 #Tamanho de uma "casa" (16 px), facilita o posicionamento dos elementos na tela
screen=pygame.display.set_mode(res,FULLSCREEN, 32) #Janela do jogo
pygame.display.set_caption("Count to 9") #Nome que aparece no topo da janela
start = pygame.time.get_ticks()#Verifica quantos milissegundos se passaram desde o inicio do programa
wait = random.randint(1000,3000) #Tempo de espera aleatorio
click = pygame.mouse.get_pressed() #Verifica os botoes do mouse
win = "" #Controla se o jogador ganhou ou perdeu
pygame.mixer.init() #Inicia o modulo de som do pygame
key = pygame.key.get_pressed() #Verifica as teclas do teclado


#IMAGENS======================================================================
#Carregar imagens
carta1 = pygame.image.load('images/carta_um.png')
carta2 = pygame.image.load('images/carta_dois.png')
carta3 = pygame.image.load('images/carta_tres.png')
carta0 = pygame.image.load('images/carta_zero.png')
mesa = pygame.image.load('images/mesa_fundo.png')
backver = pygame.image.load('images/carta_verso2.png')
backhor = pygame.image.load('images/back_hor.png')
backbig = pygame.image.load('images/carta_verso2.png')
cartatrans = pygame.image.load('images/carta_trans.png')
chip = pygame.image.load('images/chip.png')
logo = pygame.image.load('images/logo.png')
curtain = pygame.image.load('images/curtain.png')
regras = pygame.image.load('images/regras.png')
tag1 = pygame.image.load('images/tag1.png')
tag2 = pygame.image.load('images/tag2.png')
tag3 = pygame.image.load('images/tag3.png')
tag4 = pygame.image.load('images/tag4.png')

#Sons==================================================
#Carregar sons
slip=pygame.mixer.Sound("sfx/card_slip.wav")
drag=pygame.mixer.Sound("sfx/card_drag.wav")
youlose=pygame.mixer.Sound("sfx/youlose.wav")
youwin=pygame.mixer.Sound("sfx/youwin.wav")
pygame.mixer.music.load("sfx/menubg.mp3")
pygame.mixer.music.set_volume(0.5)#Muda o volume para 50%
pygame.mixer.music.play(-1)#Repete a musica carregada infinitas vezes

#LOOP PRINCIPAL==============================================================
while(True):#Loop infinito
        if(path == "menu"):
                if (pygame.mixer.music.get_busy() == False):#Se não tiver nenhuma musica tocando
                        
                        pygame.mixer.music.load("sfx/menubg.mp3")#Carregar a musica
                        pygame.mixer.music.set_volume(0.5)##Muda o volume para 50%
                        pygame.mixer.music.play(-1)#Repete a musica carregada infinitas vezes
                menu()#loop do menu
                players=["1","2","3","4"]#Recolocar os jogadores no jogo
        elif(path == "game"):
                pygame.mixer.music.stop()#Parar a musica que esta tocando
                pygame.mixer.music.load("sfx/gamebg.mp3")#Carregar uma nova musica
                pygame.mixer.music.set_volume(0.5)#Mudar volume para 50%
                pygame.mixer.music.play(-1)#Repete a musica carregada infinitas vezes
                game()#Entrar na funçao "game"
        elif(path == "regras"):
                regra()#Entrar na funçao "regra"
        if(win == True):#Se o jogador tiver ganhado
            screen.blit(mesa,(0,0))#Desenhar a mesa
            pygame.mixer.music.stop()#Parar a musica
            pygame.mixer.Sound.play(youwin)#SFX
            txt("Você venceu",144,36*casa,20*casa,white)#Escrever na tela
            pygame.display.update()#Atualiza a tela
            time.sleep(pygame.mixer.Sound.get_length(youwin))#Espera a musica acabar
            win =""
            path = "menu"#Vai para o loop do menu
        elif(win == False):#Se o jogador tiver perdido
            screen.blit(mesa,(0,0))#Desenhar a mesa
            pygame.mixer.music.stop()#Parar a musica que esta tocando
            pygame.mixer.Sound.play(youlose)#SFX
            txt("Você perdeu",144,36*casa,20*casa,white)#Escrever na tela
            pygame.display.update()#Atualizar a tela
            time.sleep(pygame.mixer.Sound.get_length(youlose))#Esperar a musica acabar
            win =""
            path = "menu" #Vai para o loop do menu
        pygame.display.update()#Atualiza a tela
        for event in pygame.event.get():#Sai do jogo
                key = pygame.key.get_pressed()
                if event.type == pygame.QUIT or key[K_ESCAPE]:
                        pygame.quit()
                        sys.exit()
