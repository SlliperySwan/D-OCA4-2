import time
import curses
from curses.textpad import rectangle
import random
import copy

def intro(stdscr, y, x, played, tinta=-1, tinta_fundo=-1):
    intro_tela = curses.newpad(10, 64)
    sair = curses.newpad(1, 100)
    sair.nodelay(True)
    stdscr.refresh()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_CYAN)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_GREEN)
    amarelo = curses.color_pair(1)
    branco = curses.color_pair(2)
    vermelho = curses.color_pair(3)
    azul = curses.color_pair(4)
    magenta = curses.color_pair(5)
    ciano = curses.color_pair(6)
    verde = curses.color_pair(7)
    tintas = [amarelo, branco, vermelho, azul, magenta, ciano, verde]
    if tinta == -1:
        tinta = random.randint(0, 6)
        tinta_fundo = random.randint(0, 6)
        while tinta_fundo == tinta:
            tinta_fundo = random.randint(0, 6)
    titulo = [[1, 1, 1, 1, 1, 2, 0, 0, 1, 1, 1, 2, 0, 0, 0, 1, 1, 1, 1, 2, 0, 0, 1, 1, 1, 1, 2, 0, 0, 1, 1, 1, 1, 2, 0, 0, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 0, 1, 1, 1, 1, 2, 0],
              [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 2],
              [1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2],
              [1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 0, 0, 0, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2],
              [1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 0, 0, 0, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 1, 2],
              [1, 1, 2, 0, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2],
              [1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 0],
              [1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 0, 1, 1, 2, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2],
              [1, 1, 1, 1, 1, 2, 0, 0, 1, 1, 1, 2, 1, 2, 0, 1, 1, 1, 1, 2, 0, 0, 1, 1, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2]]
    start_time = time.time()
    for i in range(63):
        if played == 0:
            sair.addstr(0, 0, "PULAR INTRO [ESC] ({:.2f})".format(3.96 - time.time() + start_time), curses.A_BOLD)
            sair.refresh(0, 0, y - 1, 0, y - 1, x - 1)
            try:
                key = sair.getkey()
                if ord(key) == 27:
                    return tinta, tinta_fundo
            except:
                pass
            if i < 54:
                if titulo[0][i] in [1, 2]:
                    intro_tela.addstr(0, i, " ", branco)

                elif titulo[0][i] == 0:
                    intro_tela.addstr(0, i, " ")
            if 0 < i < 55:
                if titulo[1][i - 1] in [1, 2]:
                    intro_tela.addstr(1, i - 1, " ", branco)

                elif titulo[1][i - 1] == 0:
                    intro_tela.addstr(1, i - 1, " ")
            if 1 < i < 56:
                if titulo[2][i - 2] in [1, 2]:
                    intro_tela.addstr(2, i - 2, " ", branco)

                elif titulo[2][i - 2] == 0:
                    intro_tela.addstr(2, i - 2, " ")
            if 2 < i < 57:
                if titulo[3][i - 3] in [1, 2]:
                    intro_tela.addstr(3, i - 3, " ", branco)

                elif titulo[3][i - 3] == 0:
                    intro_tela.addstr(3, i - 3, " ")
            if 3 < i < 58:
                if titulo[4][i - 4] in [1, 2]:
                    intro_tela.addstr(4, i - 4, " ", branco)
                elif titulo[4][i - 4] == 0:
                    intro_tela.addstr(4, i - 4, " ")
            if 4 < i < 59:
                if titulo[5][i - 5] in [1, 2]:
                    intro_tela.addstr(5, i - 5, " ", branco)
                elif titulo[5][i - 5] == 0:
                    intro_tela.addstr(5, i - 5, " ")
            if 5 < i < 60:
                if titulo[6][i - 6] in [1, 2]:
                    intro_tela.addstr(6, i - 6, " ", branco)
                elif titulo[6][i - 6] == 0:
                    intro_tela.addstr(6, i - 6, " ")
            if 6 < i < 61:
                if titulo[7][i - 7] in [1, 2]:
                    intro_tela.addstr(7, i - 7, " ", branco)
                elif titulo[7][i - 7] == 0:
                    intro_tela.addstr(7, i - 7, " ")
            if 7 < i < 62:
                if titulo[8][i - 8] in [1, 2]:
                    intro_tela.addstr(8, i - 8, " ", branco)
                elif titulo[8][i - 8] == 0:
                    intro_tela.addstr(8, i - 8, " ")
            if 8 < i:
                if titulo[9][i - 9] in [1, 2]:
                    intro_tela.addstr(9, i - 9, " ", branco)
                elif titulo[9][i - 9] == 0:
                    intro_tela.addstr(9, i - 9, " ")
        intro_tela.refresh(0, 0, y // 6, x // 2 - 27, y - 1, x - 1)
        if played == 0:
            time.sleep(0.050)
        if i < 54:
            if titulo[0][i] == 1:
                intro_tela.addstr(0, i, " ", tintas[tinta])
            elif titulo[0][i] == 2:
                intro_tela.addstr(0, i, " ", tintas[tinta_fundo])
            elif titulo[0][i] == 0:
                intro_tela.addstr(0, i, " ")
        if 0 < i < 55:
            if titulo[1][i - 1] == 1:
                intro_tela.addstr(1, i - 1, " ", tintas[tinta])
            elif titulo[1][i - 1] == 2:
                intro_tela.addstr(1, i - 1, " ", tintas[tinta_fundo])
            elif titulo[1][i - 1] == 0:
                intro_tela.addstr(1, i - 1, " ")
        if 1 < i < 56:
            if titulo[2][i - 2] == 1:
                intro_tela.addstr(2, i - 2, " ", tintas[tinta])
            elif titulo[2][i - 2] == 2:
                intro_tela.addstr(2, i - 2, " ", tintas[tinta_fundo])
            elif titulo[2][i - 2] == 0:
                intro_tela.addstr(2, i - 2, " ")
        if 2 < i < 57:
            if titulo[3][i - 3] == 1:
                intro_tela.addstr(3, i - 3, " ", tintas[tinta])
            elif titulo[3][i - 3] == 2:
                intro_tela.addstr(3, i - 3, " ", tintas[tinta_fundo])
            elif titulo[3][i - 3] == 0:
                intro_tela.addstr(3, i - 3, " ")
        if 3 < i < 58:
            if titulo[4][i - 4] == 1:
                intro_tela.addstr(4, i - 4, " ", tintas[tinta])
            elif titulo[4][i - 4] == 2:
                intro_tela.addstr(4, i - 4, " ", tintas[tinta_fundo])
            elif titulo[4][i - 4] == 0:
                intro_tela.addstr(4, i - 4, " ")
        if 4 < i < 59:
            if titulo[5][i - 5] == 1:
                intro_tela.addstr(5, i - 5, " ", tintas[tinta])
            elif titulo[5][i - 5] == 2:
                intro_tela.addstr(5, i - 5, " ", tintas[tinta_fundo])
            elif titulo[5][i - 5] == 0:
                intro_tela.addstr(5, i - 5, " ")
        if 5 < i < 60:
            if titulo[6][i - 6] == 1:
                intro_tela.addstr(6, i - 6, " ", tintas[tinta])
            elif titulo[6][i - 6] == 2:
                intro_tela.addstr(6, i - 6, " ", tintas[tinta_fundo])
            elif titulo[6][i - 6] == 0:
                intro_tela.addstr(6, i - 6, " ")
        if 6 < i < 61:
            if titulo[7][i - 7] == 1:
                intro_tela.addstr(7, i - 7, " ", tintas[tinta])
            elif titulo[7][i - 7] == 2:
                intro_tela.addstr(7, i - 7, " ", tintas[tinta_fundo])
            elif titulo[7][i - 7] == 0:
                intro_tela.addstr(7, i - 7, " ")
        if 7 < i < 62:
            if titulo[8][i - 8] == 1:
                intro_tela.addstr(8, i - 8, " ", tintas[tinta])
            elif titulo[8][i - 8] == 2:
                intro_tela.addstr(8, i - 8, " ", tintas[tinta_fundo])
            elif titulo[8][i - 8] == 0:
                intro_tela.addstr(8, i - 8, " ")
        if 8 < i:
            if titulo[9][i - 9] == 1:
                intro_tela.addstr(9, i - 9, " ", tintas[tinta])
            elif titulo[9][i - 9] == 2:
                intro_tela.addstr(9, i - 9, " ", tintas[tinta_fundo])
            elif titulo[9][i - 9] == 0:
                intro_tela.addstr(9, i - 9, " ")
        intro_tela.refresh(0, 0, y // 6, x // 2 - 27, y - 1, x - 1)
        if played == 0:
            time.sleep(0.010)
    sair.addstr(0, 0, " " * 42)
    sair.refresh(0, 0, y - 1, 0, y - 1, x - 1)
    return tinta, tinta_fundo

def menu(stdscr, y, x, selec):
    menu_tela = curses.newpad(y - 1, 16)
    menu_tela.nodelay(True)
    stdscr.refresh()
    while True:
        menu_tela.clear()
        menu_tela.addstr(0, 2, "INICIAR JOGO")
        menu_tela.addstr(1, 5, "OPÇÕES")
        menu_tela.addstr(y // 2 - 1, 3, "SAIR [ESC]", curses.A_BOLD)
        if selec == 0:
            menu_tela.addstr(0, 0, "> INICIAR JOGO <", curses.A_BOLD)
        elif selec == 1:
            menu_tela.addstr(1, 3, "> OPÇÕES <", curses.A_BOLD)
        menu_tela.refresh(0, 0, y // 2, x // 2 - 8, y - 1, x - 1)
        try:
            key = stdscr.getkey()
        except:
            continue
        if ord(key) == 27:
            return 2
        elif key == "w":
            if selec == 0:
                selec = 1
            else:
                selec -= 1
        elif key == "s":
            if selec == 1:
                selec = 0
            else:
                selec += 1
        elif key in [curses.KEY_ENTER, "\n", "\r"]:
            return selec

def quant_item(backup, i, j):
    total = 0
    parcela = {backup["mapa_info"][i][2][j][0]-1:0}
    for n in range(backup["mapa_info"][i][2][j][0], backup["mapa_info"][i][2][j][1]+1):
        total+=(backup["mapa_info"][i][2][j][2]-abs(backup["mapa_info"][i][2][j][2]-n)+backup["mapa_info"][i][2][j][3])
        parcela[n] = total
    parcela[backup["mapa_info"][i][2][j][1]+1] = total+1
    rng = random.randint(1, total)
    for n in range(backup["mapa_info"][i][2][j][0], backup["mapa_info"][i][2][j][1]+1):
        if parcela[n-1] <= rng < parcela[n+1]:
            return n

def atak(backup, lugar, inimigo):
    total = 0
    parcela = {}
    for i in backup["mapa_info"][lugar][6][inimigo][6]:
        parcela[backup["mapa_info"][lugar][6][inimigo][6][i][6]+total] = i
        total += backup["mapa_info"][lugar][6][inimigo][6][i][6]
    rng = random.randint(1, total)
    for i in parcela:
        if rng >= i:
            selec = i
        else:
            return parcela[i]
        return parcela[i]

def gerar_itens(stdscr, y, x, backup, itens):
    count2 = 0
    start = time.time()
    for i in backup["mapa_info"]:
        for j in backup["mapa_info"][i][2]:
            if random.randint(1, 10) <= backup["mapa_info"][i][2][j][4] and backup["mapa_info"][i][3][1]+itens[j][1] <= backup["mapa_info"][i][3][0]:
                if itens[j][2] in [0, "Munição"] or itens[j][0] == "Vela":
                    backup["mapa_info"][i][4][itens[j][0]] = quant_item(backup, i, j)
                elif itens[j][0] not in ["Besta"]:
                    backup["mapa_info"][i][4][f"{itens[j][0]}{backup["count1"]:03}"] = "Único"
                else:
                    backup["mapa_info"][i][4][f"{itens[j][0]}{backup["count1"]:03}"] = "Vazio"
                backup["mapa_info"][i][3][1] += itens[j][1]
            time.sleep(random.randint(5, 25)/1000)
            stdscr.addstr(y//2, 0, ("CARREGANDO ITENS"+"."*(count2//8%4)).center(x), curses.A_BOLD)
            stdscr.refresh()
            backup["count1"] += 1
            count2 += 1
    return backup

def gerar_inimigos(stdscr, y, x, backup, inimigos):
    count1 = 1
    count2 = 0
    start = time.time()
    for i in backup["mapa_info"]:
        for j in backup["mapa_info"][i][5]:
            if random.randint(1, 10) <= backup["mapa_info"][i][5][j][1] and len(backup["mapa_info"][i][6]) < backup["max_ini"]:
                backup["mapa_info"][i][6][count1] = [inimigos[backup["mapa_info"][i][5][j][0]][0]+str(count1),
                                                     inimigos[backup["mapa_info"][i][5][j][0]][1][0]+random.randint(-inimigos[backup["mapa_info"][i][5][j][0]][1][1], inimigos[backup["mapa_info"][i][5][j][0]][1][2]),
                                                     inimigos[backup["mapa_info"][i][5][j][0]][1][3]+random.randint(-inimigos[backup["mapa_info"][i][5][j][0]][1][4], inimigos[backup["mapa_info"][i][5][j][0]][1][5]),
                                                     0,
                                                     [0, 0, 0, 0, 0],
                                                     inimigos[backup["mapa_info"][i][5][j][0]][2]]
                backup["mapa_info"][i][6][count1].insert(3, backup["mapa_info"][i][6][count1][1])
                count1 += 1
            else:
                break
            time.sleep(random.randint(5, 25)/1000)
            stdscr.addstr(y//2, 0, ("CARREGANDO INIMIGOS"+"."*(count2//8%4)).center(x), curses.A_BOLD)
            stdscr.refresh()
            count2 += 1
        count1 = 1
    return backup

def mover(y, x, mapa, backup, key = 0):
    with open("lugares.txt", "r", encoding="utf8") as arquivo1:
        linha1 = arquivo1.readlines()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    verde = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    vermelho = curses.color_pair(2)

    movimento = curses.newwin(y//2, x//2, 0, 0)
    mapa_tela = curses.newwin(11, 74, 1, x//4-37)

    movimento.border()
    movimento.refresh()
    
    mapa_tela.border()
    mapa_tela.refresh()

    coordy = backup["coordy"]
    coordx = backup["coordx"]
    
    mapa_real = curses.newpad(21, 169)
    for i in range(7):
        if i in [0, 6]:
            mapa_real.addstr(3*i, 0, " "*168, verde)
            mapa_real.addstr(3*i+1, 0, "Floresta".center(24)*7, verde)
            mapa_real.addstr(3*i+2, 0, " "*168, verde)
        else:
            mapa_real.addstr(3*i, 0, " "*24, verde)
            mapa_real.addstr(3*i+1, 0, "Floresta".center(24), verde)
            mapa_real.addstr(3*i+2, 0, " "*24, verde)
            mapa_real.addstr(3*i, 144, " "*24, verde)
            mapa_real.addstr(3*i+1, 144, "Floresta".center(24), verde)
            mapa_real.addstr(3*i+2, 144, " "*24, verde)

    direcoes = ["W", "NORTE ", "S", "SUL   ", "D", "LESTE ", "A", "OESTE "]
              
    for y0 in range(5):
        for x0 in range(5):
            if backup["mapa_info"][mapa[y0][x0]][0] == 1:
                if x0 == 0:
                    if backup["mapa_info"][mapa[y0][x0]][1][2] == backup["mapa_info"][mapa[y0][x0+1]][1][3] == 0:
                        rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)
                    else:
                        rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-1)
                elif x0 == 4:
                    if backup["mapa_info"][mapa[y0][x0]][1][3] == backup["mapa_info"][mapa[y0][x0-1]][1][2] == 0:
                        rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)
                    else:
                        rectangle(mapa_real, 3*y0+3, 24*(x0+1), 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)
                elif 0 < x0 < 4:                 
                    if backup["mapa_info"][mapa[y0][x0]][1][2] == backup["mapa_info"][mapa[y0][x0+1]][1][3] == 0 and backup["mapa_info"][mapa[y0][x0]][1][3] == backup["mapa_info"][mapa[y0][x0-1]][1][2] == 1:
                        rectangle(mapa_real, 3*y0+3, 24*(x0+1), 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)
                        
                    elif backup["mapa_info"][mapa[y0][x0]][1][2] != backup["mapa_info"][mapa[y0][x0+1]][1][3] and backup["mapa_info"][mapa[y0][x0]][1][3] == backup["mapa_info"][mapa[y0][x0-1]][1][2] == 1:
                        rectangle(mapa_real, 3*y0+3, 24*(x0+1), 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)

                    elif backup["mapa_info"][mapa[y0][x0]][1][2] != backup["mapa_info"][mapa[y0][x0+1]][1][3] and backup["mapa_info"][mapa[y0][x0]][1][3] == backup["mapa_info"][mapa[y0][x0-1]][1][2] == 0:
                        rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)
                        
                    elif backup["mapa_info"][mapa[y0][x0]][1][2] == backup["mapa_info"][mapa[y0][x0+1]][1][3] == 1 and backup["mapa_info"][mapa[y0][x0]][1][3] == backup["mapa_info"][mapa[y0][x0-1]][1][2] == 0:
                        rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-1)
                        
                    elif backup["mapa_info"][mapa[y0][x0]][1][2] == backup["mapa_info"][mapa[y0][x0+1]][1][3] == 1 and backup["mapa_info"][mapa[y0][x0]][1][3] != backup["mapa_info"][mapa[y0][x0-1]][1][2]:
                        rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-1)

                    elif backup["mapa_info"][mapa[y0][x0]][1][2] == backup["mapa_info"][mapa[y0][x0+1]][1][3] == 0 and backup["mapa_info"][mapa[y0][x0]][1][3] != backup["mapa_info"][mapa[y0][x0-1]][1][2]:
                        rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)

                    elif backup["mapa_info"][mapa[y0][x0]][1][2] == backup["mapa_info"][mapa[y0][x0+1]][1][3] == 0 and backup["mapa_info"][mapa[y0][x0]][1][3] == backup["mapa_info"][mapa[y0][x0-1]][1][2] == 0:
                        rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)
                        
                    else:
                        rectangle(mapa_real, 3*y0+3, 24*(x0+1), 3*y0+5, 24*(x0+2)-1)
                else:
                    rectangle(mapa_real, 3*y0+3, 24*(x0+1), 3*y0+5, 24*(x0+2)-1)
    for y0 in range(5):
        for x0 in range(5):
            if y0 != 0:
                if backup["mapa_info"][mapa[y0][x0]][1][0] == backup["mapa_info"][mapa[y0][x0]][0] == backup["mapa_info"][mapa[y0-1][x0]][1][1] == backup["mapa_info"][mapa[y0-1][x0]][0] == 1:
                    mapa_real.addch(3*y0+2, 24*(x0+1)+9, curses.ACS_URCORNER)
                    mapa_real.addstr(3*y0+2, 24*(x0+1)+10, "     ")
                    mapa_real.addch(3*y0+2, 24*(x0+1)+14, curses.ACS_ULCORNER)
                    mapa_real.addch(3*y0+3, 24*(x0+1)+9, curses.ACS_LRCORNER)
                    mapa_real.addstr(3*y0+3, 24*(x0+1)+10, "     ")
                    mapa_real.addch(3*y0+3, 24*(x0+1)+14, curses.ACS_LLCORNER)
            if x0 != 0:
                if backup["mapa_info"][mapa[y0][x0]][1][3] == backup["mapa_info"][mapa[y0][x0]][0] == backup["mapa_info"][mapa[y0][x0-1]][1][2] == backup["mapa_info"][mapa[y0][x0-1]][0] == 1:
                    mapa_real.addch(3*y0+5, 24*(x0+1)-1, curses.ACS_HLINE)
                    mapa_real.addch(3*y0+5, 24*(x0+1), curses.ACS_HLINE)
                    mapa_real.addstr(3*y0+4, 24*(x0+1)-1, "  ") 
                    mapa_real.addch(3*y0+3, 24*(x0+1)-1, curses.ACS_HLINE)
                    mapa_real.addch(3*y0+3, 24*(x0+1), curses.ACS_HLINE)
                    
            if y0 == backup["coordy"] and x0 == backup["coordx"]:
                mapa_real.addstr(3*y0+4, 24*(x0+1)+11-len(mapa[y0][x0])//2, f"> {mapa[y0][x0][:-1]} <", curses.A_BOLD)
            elif backup["mapa_info"][mapa[y0][x0]][0] == 1 and len(backup["mapa_info"][mapa[y0][x0]][6]) != 0:
                mapa_real.addstr(3*y0+4, 24*(x0+1)+13-len(mapa[y0][x0])//2, mapa[y0][x0][:-1], curses.A_BOLD | vermelho)
            elif backup["mapa_info"][mapa[y0][x0]][0] == 1:
                mapa_real.addstr(3*y0+4, 24*(x0+1)+13-len(mapa[y0][x0])//2, mapa[y0][x0][:-1])
                
    rectangle(mapa_real, 2, 23, 18, 144)

    movimento.addstr(12, x//4-37, "DESCRIÇÃO: ", curses.A_BOLD)
    for i in range(3):
        movimento.addstr(13+i, x//4-37, linha1[(backup["coordy"]*5+backup["coordx"])*3+i].rstrip())
        
    movimento.addstr(17, x//4-37, "MOVIMENTO:", curses.A_BOLD)
    for i in range(4):
        movimento.addstr(18+i, x//4-37, f"{direcoes[2*i]} - {direcoes[2*i+1]}")
            
        if (i == 0 and backup["coordy"] == 0) or (i == 1 and backup["coordy"] == 4) or (i == 2 and backup["coordx"] == 4) or (i == 3 and backup["coordx"] == 0):
            movimento.addstr(" (Fora do mapa)")
            
        elif i == 0 and (backup["coordy"], backup["coordx"]) == (4, 4):
            movimento.addstr(" (Passagem subterrânea)")
        elif i == 0 and backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][1][0] == 0:
            if backup["mapa_info"][mapa[backup["coordy"]-1][backup["coordx"]]][1][1] == 1:
                movimento.addstr(" (Porta trancada)")
            else:
                movimento.addstr(" (Parede)")
        elif i == 0 and backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][1][0] == 1:
            if backup["mapa_info"][mapa[backup["coordy"]-1][backup["coordx"]]][1][1] == 0:
                movimento.addstr(" (Destrancar porta)")

        elif i == 1 and (backup["coordy"], backup["coordx"]) in [(1, 3), (1, 4)]:
            movimento.addstr(" (Passagem subterrânea)")
        elif i == 1 and backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][1][1] == 0:
            if backup["mapa_info"][mapa[backup["coordy"]+1][backup["coordx"]]][1][0] == 1:
                movimento.addstr(" (Porta trancada)")
            else:
                movimento.addstr(" (Parede)")
        elif i == 1 and backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][1][1] == 1:
            if backup["mapa_info"][mapa[backup["coordy"]+1][backup["coordx"]]][1][0] == 0:
                movimento.addstr(" (Destrancar porta)")

          
        elif i == 2 and backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][1][2] == 0:
            if backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]+1]][1][3] == 1:
                movimento.addstr(" (Porta trancada)")
            else:
                movimento.addstr(" (Parede)")
        elif i == 2 and backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][1][2] == 1:
            if backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]+1]][1][3] == 0:
                movimento.addstr(" (Destrancar porta)")

        elif i == 3 and (backup["coordy"], backup["coordx"]) == (3, 4):
            movimento.addstr(" (Passagem subterrânea)")
        elif i == 3 and backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][1][3] == 0:
            if backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]-1]][1][2] == 1:
                movimento.addstr(" (Porta trancada)")
            else:
                movimento.addstr(" (Parede)")
        elif i == 3 and backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][1][3] == 1:
            if backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]-1]][1][2] == 0:
                movimento.addstr(" (Destrancar porta)")

    movimento.refresh()

    auy = aux = 0

    if key in ["W", "NORTE"] and backup["coordy"] != 0 and backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][1][0] == 1:
        if mapa[backup["coordy"]][backup["coordx"]] == "Sala do trono1" and backup["mapa_info"]["Sala de jantar1"][1][1] == 0:
            backup["mapa_info"]["Sala de jantar1"][1][1] = 1
        else:
            auy = -3
            backup["coordy"] -= 1
            for i in range(0, -4, -1):
                mapa_real.refresh(3*backup["coordy"]-auy+i, 24*backup["coordx"], 2, x//4-36, 10, x//4+35)
                time.sleep(0.05)
        backup["turno"] +=1


    elif key in ["W", "NORTE"] and (backup["coordy"], backup["coordx"]) == (4, 4):
            backup["coordy"] -= 3
            auy = -9

            for i in range(0, -10, -1):
                mapa_real.refresh(3*backup["coordy"]-auy+i, 24*backup["coordx"], 2, x//4-36, 10, x//4+35)
                time.sleep(0.05)
            backup["turno"] +=1

            
    elif key in ["S", "SUL"] and backup["coordy"] != 4 and backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][1][1] == 1:
        if mapa[backup["coordy"]][backup["coordx"]] == "Dispensa1" and backup["mapa_info"]["Entrada1"][1][0] == 0:
            backup["mapa_info"]["Entrada1"][1][0] = 1
        elif mapa[backup["coordy"]][backup["coordx"]] == "Quarto do rei1" and backup["mapa_info"]["Quarto secreto1"][1][0] == 0:
            backup["mapa_info"]["Quarto secreto1"][1][0] = 1
        else:
            auy = 3
            backup["coordy"] += 1
            for i in range(0, 4):
                mapa_real.refresh(3*backup["coordy"]-auy+i, 24*backup["coordx"], 2, x//4-36, 10, x//4+35)
                time.sleep(0.05)
        backup["turno"] +=1

            
    elif key in ["S", "SUL"] and (backup["coordy"], backup["coordx"]) == (1, 3):
            auy = 6
            backup["coordy"] += 2
            for i in range(0, 7):
                mapa_real.refresh(3*backup["coordy"]-auy+i, 24*backup["coordx"], 2, x//4-36, 10, x//4+35)
                time.sleep(0.05)
            aux = 24
            backup["coordx"] += 1
            for i in range(0, 25):
                mapa_real.refresh(3*backup["coordy"], 24*backup["coordx"]-aux+i, 2, x//4-36, 10, x//4+35)
                time.sleep(0.01)
            backup["turno"] +=1


    elif key in ["S", "SUL"] and (backup["coordy"], backup["coordx"]) == (1, 4):
            auy = 9
            backup["coordy"] += 3
            for i in range(0, 10):
                mapa_real.refresh(3*backup["coordy"]-auy+i, 24*backup["coordx"], 2, x//4-36, 10, x//4+35)
                time.sleep(0.05)
            backup["turno"] +=1
            
            
    elif key in ["D", "LESTE"] and backup["coordx"] != 4 and backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][1][2] == 1:
        if mapa[backup["coordy"]][backup["coordx"]] == "Jardim1" and backup["mapa_info"]["Guarita2"][1][3] == 0:
            backup["mapa_info"]["Guarita2"][1][3] = 1
        else:
            aux = 24
            backup["coordx" ] += 1
            for i in range(0, 25):
                mapa_real.refresh(3*backup["coordy"], 24*backup["coordx"]-aux+i, 2, x//4-36, 10, x//4+35)
                time.sleep(0.01)
        backup["turno"] +=1
            
            
    elif key in ["A", "OESTE"] and backup["coordx"] != 0 and backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][1][3] == 1:
        aux = -24
        backup["coordx"] -= 1
        for i in range(0, -25, -1):
            mapa_real.refresh(3*backup["coordy"], 24*backup["coordx"]-aux+i, 2, x//4-36, 10, x//4+35)
            time.sleep(0.01)
        backup["turno"] +=1
        
        
    elif key in ["A", "OESTE"] and (backup["coordy"], backup["coordx"]) == (3, 4):
        aux = -24
        backup["coordx"] -= 1
        for i in range(0, -25, -1):
            mapa_real.refresh(3*backup["coordy"], 24*backup["coordx"]-aux+i, 2, x//4-36, 10, x//4+35)
            time.sleep(0.01)
        auy = -6
        backup["coordy"] -= 2
        for i in range(0, -7, -1):
            mapa_real.refresh(3*backup["coordy"]-auy+i, 24*backup["coordx"], 2, x//4-36, 10, x//4+35)
            time.sleep(0.05)
        backup["turno"] +=1
        
    else:
        if (mapa[backup["coordy"]][backup["coordx"]] == "Quarto do rei1" and
            [backup["equip"]["Mão direita"], backup["equip"]["Mão esquerda"]] == ["Cálice de prata", "Cálice de ouro"] and
            backup["mapa_info"]["Quarto do rei1"][1][1] == 0 and
            len(backup["mapa_info"]["Quarto do rei1"][4]) == 10 and
            list(backup["mapa_info"]["Quarto do rei1"][4].keys())[0][:-3] in ["Crisântemo", "Camélia"] and
            list(backup["mapa_info"]["Quarto do rei1"][4].keys())[4][:-3] == "Borboleteira" and
            list(backup["mapa_info"]["Quarto do rei1"][4].keys())[6][:-3] == "Narciso" and
            list(backup["mapa_info"]["Quarto do rei1"][4].keys())[9][:-3] in ["Rosa", "Ranúnculo"]):
            backup["mapa_info"]["Quarto do rei1"][1][1] = 1
            mover(y, x, mapa, backup)
        else:
            mapa_real.refresh(3*backup["coordy"], 24*backup["coordx"], 2, x//4-36, 10, x//4+35)
        
    backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][0] = 1
    return backup
           
def selec_item(painel, tipo, c):
    painel.addstr(17-c, 4, " "*30)
    painel.addstr(17-c, 4, "SELECIONE UM ITEM: ", curses.A_BOLD)
    key = str(painel.getstr().decode("utf-8")).upper()
    if key in [str(i) for i in range(1, len(tipo)+1)]:
        key = int(key)
        return key
    else:
        return 11

def selec_alvo(painel, tipo, c):
    painel.addstr(17-c, 4, " "*30)
    painel.addstr(17-c, 4, "SELECIONE UM ALVO: ", curses.A_BOLD)
    key = str(painel.getstr().decode("utf-8")).upper()
    if key in [str(i) for i in range(1, 6)]:
        key = int(key)
        return key
    else:
        return 11

def selec_atak(mapa, backup, inimigo):
    atk = atak(backup, mapa[backup["coordy"]][backup["coordx"]], inimigo)
    atk = backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][6][inimigo][6][atk]
    for i in range(atk[1]):
        if atk[2] == 0:
            backup["vida"][1] -= max(atk[0]-backup["defesa"]-backup["escudo"], 1)
            backup["escudo"] -= max(atk[0]-backup["defesa"], 1)
            if backup["escudo"] <= 0:
                backup["escudo"] = 0
            for i in range(atk[4]):
                backup["dot"][i] = atk[5]
        elif atk[2] == 1:
            if atk[3] == 0:
                backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][6][inimigo][4] += atk[0]
            else:
                tabela = list(backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][6].keys())
                for i in range(atk[3]):
                    try:
                        if len(tabela) == 0:
                            alvo = list(opps.keys())[0]
                        else:
                            alvo = random.randint(0, len(tabela)-1)
                        backup["mapa_info"][mapa[coordy][coordx]][6][tabela[alvo]][4] += atk[0]
                        tabela.pop(alvo)
                    except:
                        pass
        elif atk[2] == 2:
            if atk[3] == 0:
                backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][6][inimigo][1] += atk[0]
            else:
                tabela = list(backup["mapa_info"][mapa[backup["coordy"]][backup["coordx"]]][6].keys())
                for i in range(atk[3]):
                    try:
                        if len(tabela) == 0:
                            alvo = list(opps.keys())[0]
                        else:
                            alvo = random.randint(0, len(tabela)-1)
                        backup["mapa_info"][mapa[coordy][coordx]][6][tabela[alvo]][1] += atk[0]
                        tabela.pop(alvo)
                    except:
                        pass
                
def cura(backup, cura):
    backup["vida"][1] += cura
    if backup["vida"][1] > backup["vida"][0]:
        backup["vida"][1] = backup["vida"][0]

def mana(backup, mano):
    backup["mana"][1] += mano
    if backup["mana"][1] > backup["mana"][0]:
        backup["mana"][1] = backup["mana"][0]
        
def dano(backup, dano):
    backup["vida"][1] -= dano

def escudo(backup, escudo):
    backup["escudo"] += escudo

def jogar(stdscr, y, x, mapa, backup, itens):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    vida = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)
    mena = curses.color_pair(2)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
    shield = curses.color_pair(3)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    equipado = curses.color_pair(4)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    flo = curses.color_pair(5)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_RED)
    vida_boss = curses.color_pair(6)
    with open("itens.txt", "r", encoding="utf8") as arquivo1:
        linha1 = arquivo1.readlines()

    stdscr.clear()
    curses.echo()
    rectangle(stdscr, y//2, 0, y-1, x//2-1)
    rectangle(stdscr, 0, x//2+1, y//2-1, x-1)
    stdscr.refresh()

    selec = 0

    combat = curses.newwin(y//2-2, x//2-2, 1, 1)
    
    painel = curses.newwin(y//2-2, x//2-2, y//2+1, 1)

    loot = curses.newwin(y//2-2, x//2-3, 1, x//2+2)

    invt = curses.newwin(y//2, x//2-1, y//2, x//2+1)

    desc = curses.newwin(y//2-15, x//2-10, y//2+14, x//2+5)

    mover(y, x, mapa, backup)
    
    text = -1
    
    while True:
        old = backup["turno"]
        coordy = backup["coordy"]
        coordx = backup["coordx"]
        table = backup["mapa_info"][mapa[coordy][coordx]][4]
        opps = backup["mapa_info"][mapa[coordy][coordx]][6]
        invent = backup["invent"]
        equip = backup["equip"]

        if len(opps) == 0:
            y_fugir = coordy
            x_fugir = coordx

        c = 0

        if backup["person"] == "GUERREIRO":
                backup["escudo"] = len(opps)
                
        painel.clear()
        painel.addstr(0, 4, "STATUS:", curses.A_BOLD)
        painel.addstr(1, 4, f"Turno: {backup["turno"]}" + (f" (Faltam {200-backup["turno"]} turnos para morrer!)" if backup["turno"] >= 100 else ""))
        
        painel.addstr(2, 4, "Vida: ["+" "*(backup["vida"][0]+backup["escudo"])+f"] ({backup["vida"][1]}" + (f"+{backup["escudo"]}" if backup["escudo"] != 0 else "") + f"/{backup["vida"][0]})")
        painel.addstr(2, 11, backup["vida"][1]*" ", vida)
        painel.addstr(backup["escudo"]*" ", shield)

        if backup["mana"][0] != 0:
            painel.addstr(3, 4, "Mana: ["+" "*backup["mana"][0]+f"] ({backup["mana"][1]}/{backup["mana"][0]})")
            painel.addstr(3, 11, backup["mana"][1]*" ", mena)
        else:
            c += 1

        if len(opps) == 0:
            painel.addstr(5-c, 4, "ITENS:", curses.A_BOLD)
            painel.addstr(6-c, 4, "P - PEGAR")
            painel.addstr(7-c, 4, "T - PEGAR TUDO")
        else:
            painel.addstr(5-c, 4, "COMBATE:", curses.A_BOLD)
            painel.addstr(6-c, 4, "F - FUGIR")
            c += 1
            
        painel.addstr(8-c, 4, "INVENTÁRIO:", curses.A_BOLD)
        painel.addstr(9-c, 4, "E - EQUIPAR/DESEQUIPAR/USAR")
        painel.addstr(10-c, 4, "L - LARGAR")
        painel.addstr(11-c, 4, "C - LARGAR TUDO")
        painel.addstr(12-c, 4, "I - INSPECIONAR")
        painel.addstr(14-c, 4, "GERAL:", curses.A_BOLD)
        painel.addstr(15-c, 4, "Q - SAIR")
        painel.addstr(17-c, 4, "ESCOLHA UMA AÇÃO: ", curses.A_BOLD)
        painel.refresh()

        l_table = {index+1:key for (index, key) in enumerate(table)}
        
        count = 1

        loot.clear()
        if len(opps) == 0:
            loot.addstr(0, 4, "ITENS:", curses.A_BOLD)
            for value in l_table.values():
                for i in itens:
                    if value[:-3] == itens[i][0]:
                        loot.addstr(count, 4, f"{count:02} - {value[:-3]}"+(f" [{table[value]}]" if table[value] != "Único" else ""))
                        if itens[i][2] == "Flor":
                            loot.addstr(count, 28, "     [FLOR]", curses.A_BOLD | flo)
                        elif itens[i][2] == "Tesouro":
                            loot.addstr(count, 28, "  [TESOURO]", curses.A_BOLD | flo) 
                        else:
                            loot.addstr(count, 28, "  [EQUIPAR]")
                        count += 1
                        break
                    elif value == itens[i][0]:
                        loot.addstr(count, 4, f"{count:02} - {value}"+(f" x {table[value]}" if table[value] > 1 else ""))
                        if itens[i][2] == "Munição" or itens[i][0] == "Vela":
                            loot.addstr(count, 28, "  [EQUIPAR]")
                        else:
                            loot.addstr(count, 28, " [CONSUMIR]")
                        count += 1
                        break
                    
            for i in range(len(table), 10):
                loot.addstr(i+1, 4, f"{i+1:02} - vazio")
        else:
            loot.addstr(0, 4, "INIMIGOS:", curses.A_BOLD)
            for i in opps:
                if backup["mapa_info"][mapa[coordy][coordx]][6][i][1] > 0:
                    if backup["mapa_info"][mapa[coordy][coordx]][6][i][3] <= 25:
                        loot.addstr(2*i-1, 4, f"{i} - {backup["mapa_info"][mapa[coordy][coordx]][6][i][0][:-1]}: ")
                        loot.addstr(f"["+" "*(backup["mapa_info"][mapa[coordy][coordx]][6][i][3]+backup["mapa_info"][mapa[coordy][coordx]][6][i][4])+f"] ({backup["mapa_info"][mapa[coordy][coordx]][6][i][1]}" +
                                   (f"+{backup["mapa_info"][mapa[coordy][coordx]][6][i][4]}" if backup["mapa_info"][mapa[coordy][coordx]][6][i][4] != 0 else "") + f"/{backup["mapa_info"][mapa[coordy][coordx]][6][i][3]})")
                        loot.addstr(2*i-1, 11+len(backup["mapa_info"][mapa[coordy][coordx]][6][i][0][:-1]), backup["mapa_info"][mapa[coordy][coordx]][6][i][1]*" ", vida)
                        loot.addstr(backup["mapa_info"][mapa[coordy][coordx]][6][i][4]*" ", shield)
                    elif backup["mapa_info"][mapa[coordy][coordx]][6][i][1] > 0:
                        loot.addstr(2*i-1, 4, f"{i} - {backup["mapa_info"][mapa[coordy][coordx]][6][i][0][:-1]}: ")
                        loot.addstr(f"["+" "*int(backup["mapa_info"][mapa[coordy][coordx]][6][i][3]**(1/2)*2+backup["mapa_info"][mapa[coordy][coordx]][6][i][4]**(1/2)*2)+f"] ({backup["mapa_info"][mapa[coordy][coordx]][6][i][1]}"+
                                   (f"+{backup["mapa_info"][mapa[coordy][coordx]][6][i][4]}" if backup["mapa_info"][mapa[coordy][coordx]][6][i][4] != 0 else "") + f"/{backup["mapa_info"][mapa[coordy][coordx]][6][i][3]})")
                        loot.addstr(2*i-1, 11+len(backup["mapa_info"][mapa[coordy][coordx]][6][i][0][:-1]), int(backup["mapa_info"][mapa[coordy][coordx]][6][i][1]/backup["mapa_info"][mapa[coordy][coordx]][6][i][3]**(1/2)*2)*" ", vida_boss)
                        loot.addstr(int(backup["mapa_info"][mapa[coordy][coordx]][6][i][4]/backup["mapa_info"][mapa[coordy][coordx]][6][i][3]**(1/2)*2)*" ", shield)
            combat.clear()
            combat.addstr(0, 4, f"SALA: {mapa[coordy][coordx][:-1]}", curses.A_BOLD)

            count = 1
            
            if equip["Mão direita"][:-3] == "Adaga":
                combat.addstr(2, 4, f"{equip["Mão direita"][:-3]}:")
                combat.addstr(3, 4, "1 - Furar:")
                combat.addstr(4, 4, "    Causa 6 de dano, +12 se o alvo estiver sozinho.")
                              
            elif equip["Mão direita"][:-3] == "Arco":
                combat.addstr(2, 4, f"{equip["Mão direita"][:-3]}:")
                combat.addstr(3, 4, "1 - Tiro certo [1 Munição]:")
                combat.addstr(4, 4, "    Flecha causa 8 de dano, 50% de +4.")
                combat.addstr(5, 4, "    Flecha letal causa 5 de dano e envenena o alvo [5/5].")
                combat.addstr(6, 4, "2 - Tiro triplo [1 - 3 Munição]:")
                combat.addstr(7, 4, "    Flecha causa 7 de dano.")
                combat.addstr(8, 4, "    Flecha letal causa 4 de dano e envenena o alvo [5/5].")
                combat.addstr(9, 4, "    Os alvos são aleatórios.")
            elif equip["Mão direita"][:-3] == "O Bacamarte":
                combat.addstr(2, 4, f"{equip["Mão direita"][:-3]}"+("(Carregado com Nada):" if backup["bacamarte"] == 1 else
                                                               "(Descarregado):"))
                combat.addstr(3, 4, "1 - Tiro da sorte [Precisa estar carregado]:")
                combat.addstr(4, 4, "    Causa entre 4 e 28 de dano.")
                combat.addstr(5, 4, "2 - Carregar")
                combat.addstr(6, 4, "    Carrega com Nada o bacamarte que não precisa ser carregado.")
                combat.addstr(7, 4, "3 - Porrada desesperada")
                combat.addstr(8, 4, "    Causa 6 de dano.")
            elif equip["Mão direita"][:-3] == "Besta":
                combat.addstr(2, 4, f"{equip["Mão direita"][:-3]}"+("(Carregado com Flecha):" if backup["invent"]["Besta"] == "Flecha" else
                                                               "(Carregado com Flecha letal):" if backup["besta"] == "Flecha letal" else
                                                               "(Descarregado):"))
                combat.addstr(3, 4, "1 - Tiro perfurante")
                combat.addstr(4, 4, "2 - Carregar")
            elif equip["Mão direita"][:-3] == "Espada de ferro":
                combat.addstr(2, 4, f"{equip["Mão direita"][:-3]}:")
                combat.addstr(3, 4, "1 - Ataque lateral")
                combat.addstr(4, 4, "2 - Empalar")
            elif equip["Mão direita"][:-3] == "Espada de madeira":
                combat.addstr(2, 4, f"{equip["Mão direita"][:-3]}:")
                combat.addstr(3, 4, "1 - Ataque farpado")
            elif equip["Mão direita"][:-3] == "Espada de sangue":
                combat.addstr(2, 4, f"{equip["Mão direita"][:-3]}:")
                combat.addstr(3, 4, "1 - Drenar saúde")
                combat.addstr(4, 4, "2 - Lacerar")
                combat.addstr(5, 4, "3 - Vingança autodestrutiva")
            elif equip["Mão direita"][:-3] == "Espatula":
                combat.addstr(2, 4, f"{equip["Mão direita"][:-3]}:")
                combat.addstr(3, 4, "1 - Bon Appétit")
                combat.addstr(4, 4, "2 - Fazer omeletes")
            elif equip["Mão direita"][:-3] == "Grimório: Gelo":
                combat.addstr(2, 4, f"{equip["Mão direita"][:-3]}:")
                combat.addstr(3, 4, "1 - Congelar (3)")
                combat.addstr(4, 4, "2 - Ulcerar  (2)")
                combat.addstr(5, 4, "3 - Necrosar (3)")
            elif equip["Mão direita"][:-3] == "Grimório: Fogo":
                combat.addstr(2, 4, f"{equip["Mão direita"][:-3]}:")
                combat.addstr(3, 4, "1 - Bola de fogo (3)")
                combat.addstr(4, 4, "2 - Tempestade de fogo (5)")
                combat.addstr(5, 4, "3 - Pulverizar (2)")
            elif equip["Mão direita"][:-3] == "Rapieira":
                combat.addstr(2, 4, f"{equip["Mão direita"][:-3]}:")
                combat.addstr(3, 4, "1 - Ataques rápidos")
                combat.addstr(4, 4, "2 - Ripostar")
                combat.addstr(5, 4, "3 - Estocada")
            else:
                combat.addstr(2, 4, "Punhos:")
                combat.addstr(3, 4, "1 - Soco")

            if  backup["person"] == "MAGO":
                combat.addstr(6, 4, "Habilidades:")
                combat.addstr(7, 4, "4 - Apocalipse (10)")
            combat.refresh()
        loot.refresh()
            
        due = []
        for key in invent:
            if type(invent[key]) == int and invent[key] <= 0:
                due.append(key)            
        for key in due:
            del invent[key]

        invt.clear()
        invt.border()
        l_invent = {index+1:key for (index, key) in enumerate(invent)}

        count = 1
        invt.addstr(1, 5, "INVENTÁRIO:", curses.A_BOLD)
        for value in l_invent.values():
            for i in itens:
                if value[:-3] == itens[i][0]:
                    invt.addstr(count+1, 5, f"{count:02} - {value[:-3]}")
                    if itens[i][2] == "Flor":
                        invt.addstr(count+1, 29, "     [FLOR]", curses.A_BOLD | flo)
                    elif value in equip.values():
                        invt.addstr(count+1, 29, " [EQUIPADO]", curses.A_BOLD | equipado)
                    else:
                        invt.addstr(count+1, 29, "  [EQUIPAR]")
                    count += 1
                    break
                elif value == itens[i][0]:
                    invt.addstr(count+1, 5, f"{count:02} - {value} x {invent[value]}")
                    if itens[i][0] in equip.values():
                        invt.addstr(count+1, 29, " [EQUIPADO]", curses.A_BOLD | equipado)
                    elif itens[i][2] != 0:
                        invt.addstr(count+1, 29, "  [EQUIPAR]")
                    else:
                        invt.addstr(count+1, 29, " [CONSUMIR]")
                    count += 1
                    break

        for i in range(len(invent), 10):
            invt.addstr(i+2, 5, f"{i+1:02} - vazio")

        invt.addstr(13, 5, "DESCRIÇÃO:", curses.A_BOLD)
        
        count = 1
        invt.addstr(1, 41, "EQUIPAMENTO:", curses.A_BOLD)
        for key in equip:
            invt.addstr(count+1, 41, f"{key+":":<13}" +(f"{equip[key][:-3]}" if equip[key] != "vazio" else "vazio"), curses.A_BOLD if equip[key] != "vazio" else curses.color_pair(0))
            count += 1    
        invt.refresh()

        desc.clear()
        if text != -1:
            for j in range(4):
                desc.addstr(j, 1, linha1[4*text+j])
            desc.refresh()
      
        key = str(painel.getstr().decode("utf-8")).upper()
        
        if key in ["W", "S", "D", "A", "NORTE", "SUL", "LESTE", "OESTE"] and len(opps) == 0:
            backup = mover(y, x, mapa, backup, key)

        elif key in ["1", "2", "3", "4", "5"] and len(opps) != 0:
            if equip["Mão direita"][:-3] == "Adaga":
                if key == "1":
                    if len(opps) == 1:
                        alvo = list(opps.keys())[0]
                    else:
                        alvo = selec_alvo(painel, backup["mapa_info"][mapa[coordy][coordx]][6], c)
                    try:
                        if len(backup["mapa_info"][mapa[coordy][coordx]][6]) == 1:
                            backup["mapa_info"][mapa[coordy][coordx]][6][alvo][1] -= (max(18-backup["mapa_info"][mapa[coordy][coordx]][6][alvo][2], 1))
                        else:
                            backup["mapa_info"][mapa[coordy][coordx]][6][alvo][1] -= (max(6-backup["mapa_info"][mapa[coordy][coordx]][6][alvo][2], 1))
                        backup["turno"] += 1
                    except:
                        pass
                    
            elif equip["Mão direita"][:-3] == "Arco":
                if key == "1":
                    if backup["equip"]["Munição"] == "Flecha":
                        if len(opps) == 1:
                            alvo = list(opps.keys())[0]
                        else:
                            alvo = selec_alvo(painel, backup["mapa_info"][mapa[coordy][coordx]][6], c)
                        try:
                            backup["mapa_info"][mapa[coordy][coordx]][6][alvo][1] -= (max(8+4*random.randint(0, 1)-backup["mapa_info"][mapa[coordy][coordx]][6][alvo][2], 1))
                            backup["invent"]["Flecha"] -= 1
                            if backup["invent"]["Flecha"] == 0:
                                    backup["equip"]["Munição"] = "vazio"
                            backup["turno"] += 1
                        except:
                            pass
                    elif backup["equip"]["Munição"] == "Flecha letal":
                        if len(opps) == 1:
                            alvo = list(opps.keys())[0]
                        else:
                            alvo = selec_alvo(painel, backup["mapa_info"][mapa[coordy][coordx]][6], c)
                        try:
                            backup["mapa_info"][mapa[coordy][coordx]][6][alvo][1] -= (max(5-backup["mapa_info"][mapa[coordy][coordx]][6][alvo][2], 1))
                            backup["mapa_info"][mapa[coordy][coordx]][6][alvo][5] = [5, 5, 5, 5, 5]
                            backup["invent"]["Flecha letal"] -= 1
                            if backup["invent"]["Flecha letal"] == 0:
                                    backup["equip"]["Munição"] = "vazio"
                            backup["turno"] += 1
                        except:
                            pass
                elif key == "2":
                    if backup["equip"]["Munição"] == "Flecha":
                        tabela = list(opps.keys())
                        for i in range(3):
                            if "Flecha" in backup["invent"]:
                                try:
                                    if len(tabela) == 0:
                                        alvo = list(opps.keys())[0]
                                    else:
                                        alvo = random.randint(0, len(tabela)-1)
                                    backup["mapa_info"][mapa[coordy][coordx]][6][tabela[alvo]][1] -= (max(7-backup["mapa_info"][mapa[coordy][coordx]][6][tabela[alvo]][2], 1))
                                    tabela.pop(alvo)
                                    backup["invent"]["Flecha"] -= 1
                                    if backup["invent"]["Flecha"] == 0:
                                        del backup["invent"]["Flecha"]
                                        backup["equip"]["Munição"] = "vazio"
                                    backup["turno"] += 1
                                except:
                                    pass
                    elif backup["equip"]["Munição"] == "Flecha letal":
                        tabela = list(opps.keys())
                        for i in range(3):
                            if "Flecha letal" in backup["invent"]:
                                try:
                                    if len(tabela) == 0:
                                        selec = 0
                                    else:
                                        selec = random.randint(0, len(tabela)-1)
                                    backup["mapa_info"][mapa[coordy][coordx]][6][tabela[selec]][1] -= (max(4-backup["mapa_info"][mapa[coordy][coordx]][6][tabela[selec]][2], 1))
                                    backup["mapa_info"][mapa[coordy][coordx]][6][alvo][5] = [5, 5, 5, 5, 5]
                                    tabela.pop(selec)
                                    backup["invent"]["Flecha letal"] -= 1
                                    if backup["invent"]["Flecha letal"] == 0:
                                        del backup["invent"]["Flecha letal"]
                                        backup["equip"]["Munição"] = "vazio"
                                    backup["turno"] += 1
                                except:
                                    pass   
                            
            elif equip["Mão direita"][:-3] == "O Bacamarte":
                pass
            elif equip["Mão direita"][:-3] == "Besta":
                pass
            elif equip["Mão direita"][:-3] == "Espada de ferro":
                if key == "1":
                    if len(opps) == 1:
                        alvo = list(opps.keys())[0]
                    else:
                        alvo = selec_alvo(painel, backup["mapa_info"][mapa[coordy][coordx]][6], c)
                    if alvo in opps:
                        for i in range(-1, 2):
                            try:
                                backup["mapa_info"][mapa[coordy][coordx]][6][alvo+i][1] -= (max(5-backup["mapa_info"][mapa[coordy][coordx]][6][alvo+i][2], 1))
                            except:
                                continue
                        backup["turno"] += 1
                elif key == "2":
                    if len(opps) == 1:
                        alvo = list(opps.keys())[0]
                    else:
                        alvo = selec_alvo(painel, backup["mapa_info"][mapa[coordy][coordx]][6], c)
                    try:
                        backup["mapa_info"][mapa[coordy][coordx]][6][alvo][1] -= (max(10-backup["mapa_info"][mapa[coordy][coordx]][6][alvo][2], 1))
                        backup["turno"] += 1
                    except:
                        pass

            elif equip["Mão direita"][:-3] == "Espada de madeira":
                pass
            elif equip["Mão direita"][:-3] == "Espada de sangue":
                pass
            elif equip["Mão direita"][:-3] == "Espatula":
                pass
            elif equip["Mão direita"][:-3] == "Grimório: Gelo":
                pass
            elif equip["Mão direita"][:-3] == "Grimório: Fogo":
                pass
            elif equip["Mão direita"][:-3] == "Rapieira":
                pass
            else:
                if key == "1":
                    if len(opps) == 1:
                        alvo = list(opps.keys())[0]
                    else:
                        alvo = selec_alvo(painel, backup["mapa_info"][mapa[coordy][coordx]][6], c)
                    try:
                        backup["mapa_info"][mapa[coordy][coordx]][6][alvo][1] -= (max(4-backup["mapa_info"][mapa[coordy][coordx]][6][alvo][2], 1))
                        backup["turno"] += 1
                    except:
                        pass
                pass
            if  backup["person"] == "MAGO" and ataque == 4 and mana[0] >= 10:
                for alvo in opps:
                    backup["mapa_info"][mapa[coordy][coordx]][6][alvo][1] -= (max(5+backup["exp"]-backup["mapa_info"][mapa[coordy][coordx]][6][alvo][2], 1))
                
                pass
                
        elif key in ["F", "FUGIR"] and len(opps) != 0:
            backup["coordy"] = y_fugir
            backup["coordx"] = x_fugir
            mover(y, x, mapa, backup)
            
        elif key in ["P", "PEGAR"] and (len(invent) < 10 or (invent.keys() & table.keys())) and len(opps) == 0:
            key  = selec_item(painel, table, c)
            if key != 11:
                try:
                    invent[l_table[key]] += table[l_table[key]]
                    del table[l_table[key]]
                except:
                    if len(invent) < 10:
                        invent[l_table[key]] = table[l_table[key]]    
                        del table[l_table[key]]

        elif key in ["T", "PEGAR TUDO"] and len(opps) == 0:
            for i in range(1, len(table)+1):
                if l_table[i] in invent:
                    invent[l_table[i]] += table[l_table[i]]
                    del table[l_table[i]]
                elif len(invent) < 10:
                    invent[l_table[i]] = table[l_table[i]]
                    del table[l_table[i]]
            
        elif key in ["E", "EQUIPAR", "USAR"]:
            key = selec_item(painel, invent, c)
            for i in itens:
                try:
                    if itens[i][0] == l_invent[key][:-3] and itens[i][2] != "Flor":
                        if l_invent[key] == equip[itens[i][2]]:
                            equip[itens[i][2]] = "vazio"
                        else:
                            equip[itens[i][2]] = l_invent[key]
                            if itens[i][0] in ["Arco", "Bacamarte sem balas", "Besta", "Grimório: Fogo", "Grimório: Gelo"]:
                                equip["Mão esquerda"] = "vazio"
                            elif itens[i][2] == "Mão esquerda" and equip["Mão direita"][:-3] in ["Arco", "Bacamarte sem balas", "Besta", "Grimório: Fogo", "Grimório: Gelo"]:
                                equip["Mão direita"] = "vazio"
                        break
                    elif itens[i][0] == l_invent[key]:
                        if itens[i][0] in equip.values():
                            equip[itens[i][2]] = "vazio"
                        elif itens[i][2] == 0:
                            if l_invent[key] in ["Bolinho", "Bolo", "Pão", "Poção de cura"]:
                                if l_invent[key] in ["Bolinho", "Pão"]:
                                    cura(backup, 1)
                                elif l_invent[key] == "Bolo":
                                    cura(backup, 2)
                                elif l_invent[key] == "Poção de cura":
                                    cura(backup, 3+int(0.3*(backup["vida"][0]-backup["vida"][1])))          
                            elif l_invent[key] == "Poção de mana":
                                mana(backup, 6)
                            elif l_invent[key] == "Mapa":
                                for i in backup["mapa_info"]:
                                    if i not in ["Torre vermelha1", "Quarto secreto1"]:
                                        backup["mapa_info"][i][0] = 1          
                            elif l_invent[key] == "Vinho":
                                backup["vinho"] += random.randint(1, 3)   
                            invent[l_invent[key]] -= 1
                            turno += 1
                        elif itens[i][2] == "Munição":
                            equip["Munição"] = itens[i][0]
                        elif itens[i][0] == "Vela":
                            equip["Mão esquerda"] = "Vela"
                        break
                except:
                    continue

        elif key in ["I", "INSPECIONAR"]:
            key = selec_item(painel, invent, c)
            for i in itens:
                try:
                    if itens[i][0] in [l_invent[key][:-3], l_invent[key]]:
                        text = i-1
                        break
                except:
                    pass

        elif key in ["L", "LARGAR"] and (len(table) < 10 or (invent.keys() & table.keys())):
            key = selec_item(painel, invent, c)
            if key != 11: 
                try:
                    table[l_invent[key]] += invent[l_invent[key]]
                    del invent[l_invent[key]]
                except:
                    if len(table) < 10:
                        table[l_invent[key]] = invent[l_invent[key]]
                        del invent[l_invent[key]]

        elif key in ["C", "LARGAR TUDO"]:
            for i in range(1, len(invent)+1):
                if l_invent[i] in table:
                    table[l_invent[i]] += invent[l_invent[i]]
                    del invent[l_invent[i]]
                elif len(table) < 10:
                    table[l_invent[i]] = invent[l_invent[i]]
                    del invent[l_invent[i]]
            for i in equip:
                equip[i] = "vazio"
            
        elif key in ["Q", "SAIR", "^["]:
            break

        for i in ["Mão esquerda", "Capacete", "Peitoral", "Perneira", "Botas"]:
            if backup["equip"][i] in ["Capacete de ferro", "Couraça de couro", "Botas de ferro", "Escudo"]:
                backup["defesa"] += 2
            if backup["equip"][i] in ["Couraça de ferro", "Perneira de ferro"]:
                backup["defesa"] += 3
            
        new = backup["turno"]

        if new != old:
            if new%3 == 0:
                cura(backup, backup["vida_regen"])
            if new%3 == 0:
                mana(backup, backup["mana_regen"])
            
            for i in opps:
                backup["mapa_info"][mapa[coordy][coordx]][6][i][4] = 0
        
            if backup["dot"][0] != 0:
                dano(backup, backup["dot"][0])
                backup["dot"].pop(0)
                backup["dot"].append(0)
                if backup["vida"][1] <= 0 and backup["diff"] != "DIFÍCIL":
                    backup["vida"][1] = 1
                else:
                    backup["resultado"] = -2

            due = []
            if len(opps) >= 1:
                for i in backup["mapa_info"][mapa[coordy][coordx]][6]:
                    backup["mapa_info"][mapa[coordy][coordx]][6][i][1] -= backup["mapa_info"][mapa[coordy][coordx]][6][i][5][0]
                    backup["mapa_info"][mapa[coordy][coordx]][6][i][5].pop(0)
                    backup["mapa_info"][mapa[coordy][coordx]][6][i][5]+=[0]
                    if backup["mapa_info"][mapa[coordy][coordx]][6][i][1] <= 0:
                        due.append(i)
                for i in due:
                    del backup["mapa_info"][mapa[coordy][coordx]][6][i]
                if len(opps) == 0:
                    backup["exp"] += 1
            for i in opps:
                selec_atak(mapa, backup, i)
            backup["escudo"] = 0
            backup["defesa"] = 0
                
        for i in equip:
            if i == "Munição" and backup["equip"][i] not in invent:
                backup["equip"][i] = "vazio"
            elif backup["equip"][i] not in backup["invent"]:
                backup["equip"][i] = "vazio"
                
        if len(opps) == 0:
            mover(y, x, mapa, backup)

        if [coordy, coordx] == [4, 3]:
            backup["resultado"] = 1
            time.sleep(1)
            fim = curses.newpad(2, x)
            fim.addstr(" "*(x))
            for i in range(y-1):
                fim.refresh(0, 0, i, 0, i, x-1)
                time.sleep(0.05)

        if backup["turno"] >= 200:
            backup["resultado"] = -1
        if backup["vida"][1] <= 0:
            backup["resultado"] = -3
        if backup["resultado"] != 0:
            break

def opcoes(stdscr, y, x, backup):
    stdscr.clear()
    stdscr.addstr(0, 0, "< OPÇÕES >", curses.A_BOLD)
    stdscr.addstr(y - 1, x // 2 - 6, "VOLTAR [ESC]", curses.A_BOLD)
    stdscr.refresh()

    opcoes_tela = curses.newwin(y - 2, x // 4 - 1, 1, 1)
    opcoes_tela.nodelay(True)

    desc_borda = curses.newwin(y - 1, x // 2 - 2, 0, x // 4 + 1)
    desc_borda.border()
    desc_borda.addstr(0, x // 4 - 7, "< DETALHES >", curses.A_BOLD)
    desc_borda.refresh()

    desc = curses.newwin(y - 3, x // 2 - 4, 1, x // 4 + 2)
    desc.nodelay(True)

    with open("opcoes.txt", "r", encoding="utf8") as arquivo:
        linha = arquivo.readlines()

    ops = 0
    while True:
        opcoes_tela.clear()
        desc.clear()
        opcoes_tela.addstr(0, 2, "DIFICULDADE: {}".format(backup["diff"]))
        opcoes_tela.addstr(1, 2, "PERSONAGEM: {}".format(backup["person"]))
        if ops == 0:
            opcoes_tela.addstr(0, 2, "> DIFICULDADE: {} <".format(backup["diff"]), curses.A_BOLD)
        elif ops == 1:
            opcoes_tela.addstr(1, 2, "> PERSONAGEM: {} <".format(backup["person"]), curses.A_BOLD)
        opcoes_tela.refresh()
        desc.refresh()
        try:
            key = opcoes_tela.getkey()
        except:
            continue
        if ord(key) == 27:
            return backup
        elif key == "w":
            if ops == 0:
                ops = 1
            else:
                ops -= 1
        elif key == "s":
            if ops == 1:
                ops = 0
            else:
                ops += 1
        elif key in [curses.KEY_ENTER, "\n", "\r"]:
            subop = 0
            while ops == 0:
                opcoes_tela.clear()
                desc.clear()
                opcoes_tela.addstr(0, 2, "< DIFICULDADE >", curses.A_BOLD)
                opcoes_tela.addstr(1, 4, "FÁCIL")
                opcoes_tela.addstr(2, 4, "MÉDIO")
                opcoes_tela.addstr(3, 4, "DIFÍCIL")
                if subop == 0:
                    opcoes_tela.addstr(1, 4, "> FÁCIL <", curses.A_BOLD)
                    for i in range(5):
                        desc.addstr(linha[i])
                elif subop == 1:
                    opcoes_tela.addstr(2, 4, "> MÉDIO <", curses.A_BOLD)
                    for i in range(6):
                        desc.addstr(linha[i + 6])
                elif subop == 2:
                    opcoes_tela.addstr(3, 4, "> DIFÍCIL <", curses.A_BOLD)
                    for i in range(6):
                        desc.addstr(linha[i + 13])
                opcoes_tela.refresh()
                desc.refresh()
                try:
                    key = opcoes_tela.getkey()
                except:
                    continue
                if ord(key) == 27:
                    break
                elif key == "w":
                    if subop == 0:
                        subop = 2
                    else:
                        subop -= 1
                elif key == "s":
                    if subop == 2:
                        subop = 0
                    else:
                        subop += 1
                elif key in [curses.KEY_ENTER, "\n", "\r"]:
                    if subop == 0:
                        backup["diff"] = "FÁCIL"
                        break
                    elif subop == 1:
                        backup["diff"] = "MÉDIO"
                        break
                    elif subop == 2:
                        backup["diff"] = "DIFÍCIL"
                        break
            while ops == 1:
                opcoes_tela.clear()
                desc.clear()
                opcoes_tela.addstr(0, 2, "< PERSONAGEM >", curses.A_BOLD)
                opcoes_tela.addstr(1, 4, "GUERREIRO")
                opcoes_tela.addstr(2, 4, "LADINO")
                opcoes_tela.addstr(3, 4, "MAGO")
                if subop == 0:
                    opcoes_tela.addstr(1, 4, "> GUERREIO <", curses.A_BOLD)
                    for i in range(6):
                        desc.addstr(linha[i + 20])
                elif subop == 1:
                    opcoes_tela.addstr(2, 4, "> LADINO <", curses.A_BOLD)
                    for i in range(7):
                        desc.addstr(linha[i + 27])
                elif subop == 2:
                    opcoes_tela.addstr(3, 4, "> MAGO <", curses.A_BOLD)
                    for i in range(11):
                        desc.addstr(linha[i + 36])
                opcoes_tela.refresh()
                desc.refresh()
                try:
                    key = opcoes_tela.getkey()
                except:
                    continue
                if ord(key) == 27:
                    break
                elif key == "w":
                    if subop == 0:
                        subop = 2
                    else:
                        subop -= 1
                elif key == "s":
                    if subop == 2:
                        subop = 0
                    else:
                        subop += 1
                elif key in [curses.KEY_ENTER, "\n", "\r"]:
                    if subop == 0:
                        backup["person"] = "GUERREIRO"
                        break
                    elif subop == 1:
                        backup["person"] = "LADINO"
                        break
                    elif subop == 2:
                        backup["person"] = "MAGO"
                        break

def main(stdscr, mapa, backup, back_do_back, itens):
    stdscr.nodelay(True)
    curses.curs_set(0)
    y, x = stdscr.getmaxyx()

    start = time.time()
    while True:
        stdscr.addstr(y//2, x//2-14, f"MAXIMIZE A TELA [F11] ({time.time()-start:.2f})", curses.A_BOLD)
        stdscr.addstr(y//2+1, x//2-18, ">>> HIPER MEGA ULTRA RECOMENDADO! <<<", curses.A_BOLD)
        stdscr.addstr(y//2+2, x//2-16, ">>> NA VERDADE, OBRIGATÓRIO! <<<", curses.A_BOLD)
        key = stdscr.getch()
        if  key == curses.KEY_RESIZE:
            curses.resize_term(*stdscr.getmaxyx())
            break

    stdscr.clear()
    stdscr.refresh()
    y, x = stdscr.getmaxyx()
    selec = 0
    curses.curs_set(0)

    curses.init_pair(10, curses.COLOR_RED, curses.COLOR_BLACK)
    derrota = curses.color_pair(10)
    curses.init_pair(11, curses.COLOR_GREEN, curses.COLOR_BLACK)
    vitoria = curses.color_pair(11)
    
    tinta, tinta_fundo = intro(stdscr, y, x, 0)
    while True:
        stdscr.clear()
        intro(stdscr, y, x, 1, tinta, tinta_fundo)
        selec = menu(stdscr, y, x, selec)
        if selec == 0:
            back_do_back = copy.deepcopy(backup)

            if backup["diff"] == "FÁCIL":
                backup["vida_regen"] = 1
                backup["vida"][0] += 5
                backup["vida"][1] += 5
                backup["boss"] = 1
                backup["max_ini"] = 3
            elif backup["diff"] == "MÉDIO":
                backup["vida"][0] += 1
                backup["boss"] = 1.5
                backup["max_ini"] = 4
            else:
                backup["boss"] = 2
                backup["max_ini"] = 5
                
            if backup["person"] == "GUERREIRO":
                backup["invent"]["Espada de ferro000"] = "Único"
                backup["invent"]["Escudo001"] = "Único"
            elif backup["person"] == "LADINO":
                backup["invent"]["Adaga000"] = "Único"
                backup["invent"]["Arco001"] = "Único"
                backup["invent"]["Flecha"] = 25
            else:
                backup["invent"]["Grimório: Fogo000"] = "Único"
                backup["invent"]["Poção de cura"] = 2
                backup["invent"]["Poção de mana"] = 2
                backup["mana"][0] = 10
                backup["mana"][1] = 10
                backup["mana_regen"] = 3

            stdscr.clear()
            stdscr.addstr(y//4, 0, "VOCÊ FOI AMALDIÇOADO POR UMA BRUXA E ESTÁ ENVELHECENDO RAPIDAMENTE.".center(x), curses.A_BOLD)
            stdscr.addstr(y//4+1, 0, "AGORA, PRECISA ENCONTRAR A FONTE DA JUVENTITUDE,".center(x), curses.A_BOLD)
            stdscr.addstr(y//4+2, 0, "HÁ TEMPO SOTERRADA ABAIXO DA FORTALEZA DE UM REI OBSTINADO,".center(x), curses.A_BOLD)
            stdscr.addstr(y//4+3, 0, "ANTES QUE SEJA TARDE...".center(x), curses.A_BOLD)
            stdscr.refresh()
            
            backup = gerar_itens(stdscr, y, x, backup, itens)
            backup = gerar_inimigos(stdscr, y, x, backup, inimigos)
            
            stdscr.addstr(y//2, 0, "PRESSIONE QUALQUER TECLA PARA CONTINUAR...".center(x), curses.A_BOLD)
            stdscr.nodelay(False)
            stdscr.getkey()
            stdscr.nodelay(True)
            
            jogar(stdscr, y, x, mapa, backup, itens)
            
            while True:
                stdscr.clear()
                if backup["resultado"] < 0:
                    if backup["resultado"] == -1:
                        stdscr.addstr(y//2, 0, "MEUS PÊSAMES, VOCÊ SUCUMBIU DEVIDO AO ENVELHECIMENTO ACELERADO...".center(x), derrota)
                    elif backup["resultado"] == -2:
                        stdscr.addstr(y//2, 0, "MEUS PÊSAMES, VOCÊ TEVE UMA MORTE LENTA CAUSADA POR FOGO OU ENVENENAMENTO...".center(x), derrota)
                    elif backup["resultado"] == -3:
                        stdscr.addstr(y//2, 0, "MEUS PÊSAMES, VOCÊ FOI DERRUBADO POR UM GOLPE INIMIGO...".center(x), derrota)
                    stdscr.addstr(y//2+1, 0, f"Turnos: {backup["turno"]}".center(x), derrota)
                elif backup["resultado"] == 1:
                    stdscr.addstr(y//2, 0, f"PARABÉNS {backup["person"]}! VOCÊ BEBEU DA FONTE DA JUVENTUDE E CONSEGUIU SAIR COM VIDA DA FORTALEZA!".center(x), vitoria | curses.A_BOLD)
                    stdscr.addstr(y//2+1, 0, f"Turnos: {backup["turno"]}".center(x), vitoria)
                else:
                    break
                stdscr.addstr(y//2+2, 0, "PRESSIONE QUALQUER TECLA PARA CONTINUAR...".center(x), curses.A_BOLD)
                stdscr.refresh() 
                try:
                    key = stdscr.getkey()
                    break
                except:
                    continue
               
            backup = copy.deepcopy(back_do_back)
            curses.noecho()
        elif selec == 1:
            backup = opcoes(stdscr, y, x, backup)
        elif selec == 2:
            break
        
mapa = [["Cozinha1", "Sala de jantar1", "Encruzilhada1", "Guarita1", "Masmorra1"],
        ["Dispensa1", "Sala do trono1", "Salão principal1", "Expurgo1", "Catacumbas1"],
        ["Entrada1", "Corredor lateral1", "Encruzilhada2", "Quartéis1", "Paiol1"],
        ["Corredor vertical1", "Jardim1", "Guarita2", "Quarto do rei1", "Porão1"],
        ["Torre do vigia1", "Arcanium1", "Sala do tesouro1", "Quarto secreto1", "Torre vermelha1"]]

backup = {"mapa_info":
                    {
                    "Arcanium1":          [0, [1,0,0,1], {8:[1, 1, 1, 0, 10],
                                                          10:[1, 1, 1, 0, 1],
                                                          21:[1, 1, 1, 0, 10],
                                                          26:[1, 2, 1, 1, 8],
                                                          27:[2, 4, 3, 0, 10],
                                                          33:[1, 1, 1, 0, 10]},
                                          [150, 0], {}, {1:[14, 10]},
                                          {}],
                    "Catacumbas1":        [0, [1,0,0,0], {4:[1, 1, 1, 0, 1],
                                                          7:[1, 1, 1, 0, 1],
                                                          9:[1, 1, 1, 0, 1],
                                                          13:[1, 1, 1, 0, 1],
                                                          15:[1, 1, 1, 0, 1],
                                                          20:[5, 10, 6, 2, 10],
                                                          25:[1, 1, 1, 0, 1],
                                                          26:[1, 2, 1, 1, 10],
                                                          27:[1, 2, 2, 0, 5],
                                                          33:[1, 1, 1, 0, 10],
                                                          36:[8, 15, 9, 0, 10]},
                                          [150, 0], {}, {1:[1, 10],
                                                         2:[2, 9],
                                                         3:[1, 9],
                                                         4:[2, 9],
                                                         5:[1, 5]},
                                          {}],
                    "Corredor lateral1":  [0, [0,0,1,1], {33:[1, 1, 1, 0, 10]},
                                          [100, 0], {}, {1:[3, 5],
                                                         2:[4, 1]},
                                          {}],
                    "Corredor vertical1": [0, [1,1,0,0], {33:[1, 1, 1, 0, 10]},
                                          [100, 0], {}, {1:[3, 5],
                                                         2:[4, 1]},
                                          {}],
                    "Cozinha1":           [0, [0,1,1,0], {5:[2, 5, 3, 0, 10],
                                                          6:[2, 5, 3, 0, 10],
                                                          24:[2, 5, 3, 0, 10],
                                                          34:[1, 2, 1, 1, 10]},
                                          [200, 0], {}, {1:[12, 10],
                                                         2:[10, 9],
                                                         3:[10, 8],
                                                         4:[10, 7],
                                                         5:[10, 6]},
                                          {}],
                    "Dispensa1":          [0, [1,1,0,0], {5:[3, 6, 3, 0, 10],
                                                          6:[3, 6, 3, 0, 10],
                                                          19:[1, 1, 1, 0, 2],
                                                          24:[3, 6, 3, 0, 10],
                                                          26:[1, 2, 1, 1, 10],
                                                          30:[1, 1, 1, 0, 2],
                                                          34:[1, 2, 1, 1, 10]},
                                          [300, 0], {}, {1:[10, 10],
                                                         2:[11, 10],
                                                         3:[10, 5],
                                                         4:[10, 9],
                                                         5:[10, 2]},
                                          {}],
                    "Encruzilhada1":      [0, [0,1,1,1], {33:[1, 1, 1, 0, 10]},
                                          [100, 0], {}, {1:[5, 10],
                                                         2:[6, 10],
                                                         3:[6, 10],
                                                         4:[6, 10],
                                                         5:[6, 10]},
                                          {}],
                    "Encruzilhada2":      [0, [1,1,1,1], {33:[1, 1, 1, 0, 10]},
                                          [100, 0], {}, {1:[3, 5],
                                                         2:[4, 1]},
                                          {}],
                    "Entrada1":           [1, [0,1,1,0], {14:[1, 1, 1, 0, 10],
                                                          20:[5, 10, 6, 2, 10],
                                                          26:[1, 2, 1, 1, 10],
                                                          33:[1, 1, 1, 0, 10]},
                                          [100, 0], {}, {},
                                          {}],
                    "Expurgo1":           [0, [1,0,0,0], {12:[1, 1, 1, 0, 10],
                                                          17:[1, 1, 1, 0, 10],
                                                          22:[1, 1, 1, 0, 10],
                                                          33:[1, 1, 1, 0, 10]},
                                          [100, 0], {}, {1:[10, 10],
                                                         2:[11, 10],
                                                         3:[10, 5],
                                                         4:[10, 9],
                                                         5:[10, 2]},
                                          {}],
                    "Guarita1":           [0, [0,1,1,1], {1:[1, 1, 1, 0, 10],
                                                          2:[1, 1, 1, 0, 10],
                                                          4:[1, 1, 1, 0, 2],
                                                          7:[1, 1, 1, 0, 1],
                                                          9:[1, 1, 1, 0, 1],
                                                          15:[1, 1, 1, 0, 1],
                                                          16:[1, 1, 1, 0, 1],
                                                          20:[5, 10, 6, 2, 10]},
                                          [200, 0], {}, {1:[3, 10],
                                                         2:[3, 5]},
                                          {}],
                    "Guarita2":           [0, [1,1,1,0], {1:[1, 1, 1, 0, 10],
                                                          2:[1, 1, 1, 0, 10],
                                                          4:[1, 1, 1, 0, 10],
                                                          7:[1, 1, 1, 0, 1],
                                                          9:[1, 1, 1, 0, 1],
                                                          15:[1, 1, 1, 0, 1],
                                                          16:[1, 1, 1, 0, 1],
                                                          20:[5, 10, 6, 2, 10]},
                                          [200, 0], {}, {1:[3, 10],
                                                         2:[3, 5]},
                                          {}],
                    "Jardim1":            [0, [0,1,1,0], {14:[1, 1, 1, 0, 5],
                                                          23:[1, 1, 1, 0, 5],
                                                          29:[1, 1, 1, 0, 5],
                                                          31:[1, 1, 1, 0, 5],
                                                          32:[1, 1, 1, 0, 5],
                                                          33:[1, 1, 1, 0, 10]},
                                          [30, 0], {}, {1:[10, 2]},
                                          {}],
                    "Masmorra1":          [0, [0,1,0,1], {13:[1, 1, 1, 0, 1],
                                                          15:[1, 1, 1, 0, 1],
                                                          20:[5, 10, 6, 2, 10],
                                                          26:[1, 2, 1, 1, 8],
                                                          33:[1, 1, 1, 0, 10],
                                                          36:[8, 15, 9, 0, 10]},
                                          [200, 0], {}, {1:[13, 10],
                                                         2:[2, 10],
                                                         3:[1, 5],
                                                         4:[2, 5],
                                                         5:[6, 10]},
                                          {}],
                    "Paiol1":             [0, [0,1,0,1], {1:[1, 1, 1, 0, 10],
                                                          2:[1, 1, 1, 0, 10],
                                                          4:[1, 1, 1, 0, 2],
                                                          7:[1, 1, 1, 0, 1],
                                                          9:[1, 1, 1, 0, 1],
                                                          12:[1, 1, 1, 0, 10],
                                                          13:[1, 1, 1, 0, 1],
                                                          15:[1, 1, 1, 0, 1],
                                                          16:[1, 1, 1, 0, 1],
                                                          20:[5, 10, 6, 2, 10],
                                                          25:[1, 1, 1, 0, 1]},
                                          [200, 0], {}, {1:[3, 10],
                                                         2:[3, 9],
                                                         3:[3, 8]},
                                          {}],
                    "Porão1":             [0, [1,0,0,0], {33:[1, 1, 1, 0, 10]},
                                          [50, 0], {}, {1:[3, 10]},
                                          {}],
                    "Quartéis1":          [0, [0,0,1,1], {9:[1, 1, 1, 0, 1],
                                                          13:[1, 1, 1, 0, 1],
                                                          15:[1, 1, 1, 0, 1],
                                                          16:[1, 1, 1, 0, 1],
                                                          20:[5, 10, 6, 2, 10],
                                                          25:[1, 1, 1, 0, 1],
                                                          33:[1, 1, 1, 0, 10],
                                                          34:[1, 2, 1, 1, 10]},
                                          [200, 0], {}, {1:[3, 10],
                                                         2:[3, 10],
                                                         3:[3, 10],
                                                         4:[3, 10],
                                                         5:[3, 10]},
                                          {}],
                    "Quarto do rei1":     [0, [0,0,0,1], {11:[1, 1, 1, 0, 10],
                                                          16:[1, 1, 1, 0, 1],
                                                          33:[1, 1, 1, 0, 10],
                                                          34:[1, 2, 1, 1, 10]},
                                          [50, 0], {}, {1:[7, 10]},
                                          {}],
                    "Quarto secreto1":    [0, [0,0,0,0], {33:[1, 1, 1, 0, 10],
                                                          39:[2, 9, 5, 0, 10],
                                                          40:[1, 1, 1, 0, 10],
                                                          41:[1, 1, 1, 0, 10],
                                                          42:[1, 1, 1, 0, 10],
                                                          43:[1, 1, 1, 0, 10]},
                                          [100, 0], {}, {},
                                          {}],
                    "Sala de jantar1":    [0, [0,0,1,1], {5:[3, 6, 3, 0, 10],
                                                          6:[2, 5, 3, 0, 10],
                                                          19:[1, 1, 1, 0, 2],
                                                          24:[3, 6, 3, 0, 10],
                                                          33:[1, 1, 1, 0, 10],
                                                          34:[1, 2, 1, 1, 10],
                                                          37:[1, 1, 1, 0, 10]},
                                          [100, 0], {}, {1:[10, 10],
                                                         2:[10, 7],
                                                         3:[10, 7],
                                                         4:[10, 7],
                                                         5:[10, 7]},
                                          {}],
                    "Sala do trono1":     [0, [1,0,1,0], {28:[1, 1, 1, 0, 10],
                                                          33:[1, 1, 1, 0, 10]},
                                          [100, 0], {}, {1:[4, 10],
                                                         2:[3, 5],
                                                         3:[3, 5],
                                                         3:[3, 5]},
                                          {}],
                    "Sala do tesouro1":   [0, [1,0,0,0], {3:[1, 1, 1, 0, 10],
                                                          23:[1, 1, 1, 0, 10],
                                                          38:[1, 1, 1, 0, 10]},                                                    
                                          [200, 0], {}, {1:[3, 10],
                                                         2:[3, 10],
                                                         3:[3, 5],
                                                         4:[4, 1]},
                                          {}],
                    "Salão principal1":   [0, [1,1,0,1], {22:[1, 1, 1, 0, 10],
                                                          33:[1, 1, 1, 0, 10],
                                                          34:[1, 2, 1, 1, 10]},
                                          [100, 0], {}, {1:[4, 10],
                                                         2:[4, 9],
                                                         3:[4, 7],
                                                         4:[4, 4],
                                                         5:[4, 1]},
                                          {}], 
                    "Torre do vigia1":    [0, [1,0,1,0], {2:[1, 1, 1, 0, 10],
                                                          7:[1, 1, 1, 0, 1],
                                                          9:[1, 1, 1, 0, 1],
                                                          20:[5, 10, 6, 2, 10],
                                                          22:[1, 1, 1, 0, 10]},
                                          [200, 0], {}, {1:[8, 10],
                                                         2:[8, 10]},
                                          {}],
                    "Torre vermelha1":    [0, [0,0,0,0], {18:[1, 1, 1, 0, 10],
                                                          26:[1, 2, 1, 1, 10],
                                                          29:[1, 1, 1, 0, 10]},
                                          [200, 0], {}, {1:[9, 10],
                                                         2:[8, 10],
                                                         3:[8, 10],
                                                         4:[8, 1],
                                                         5:[8, 1]},
                                          {}]
                    },
          "invent":{},
          "equip":
                  {
                   "Mão direita":"vazio",
                   "Mão esquerda":"vazio",
                   "Botas":"vazio",
                   "Perneira":"vazio",
                   "Peitoral":"vazio",
                   "Capacete":"vazio",
                   "Munição":"vazio"
                   },
          "vida":[20, 20],
          "mana":[0, 0],
          "vida_regen":0,
          "mana_regen":0,
          "vinho":0,
          "dot": [0, 0, 0, 0, 0],
          "escudo":0,
          "defesa":0,
          "diff": "FÁCIL",
          "person": "GUERREIRO",
          "coordy": 2,
          "coordx": 0,
          "turno": 0,
          "boss": 1,
          "max_ini": 3,
          "resultado": 0,
          "count1":3,
          "exp":0,
          "bacamarte":0
          }

back_do_back = {}

itens = {
         1: ["Adaga"              , 50 , "Mão direita" ],
         2: ["Arco"               , 50 , "Mão direita" ],
         3: ["O Bacamarte"        , 100, "Mão direita" ],
         4: ["Besta"              , 50 , "Mão direita" ],
         5: ["Bolinho"            , 5  , 0             ],
         6: ["Bolo"               , 5  , 0             ],
         7: ["Botas de ferro"     , 40 , "Botas"       ],
         8: ["Borboleteira"       , 5  , "Flor"        ],
         9: ["Capacete de ferro"  , 50 , "Capacete"    ],
         10:["Chapéu de mago"     , 30 , "Capacete"    ],
         11:["Coroa"              , 30 , "Capacete"    ],
         12:["Couraça de couro"   , 40 , "Peitoral"    ],
         13:["Couraça de ferro"   , 80 , "Peitoral"    ],
         14:["Crisântemo"         , 5  , "Flor"        ],
         15:["Escudo"             , 60 , "Mão esquerda"],
         16:["Espada de ferro"    , 60 , "Mão direita" ],
         17:["Espada de madeira"  , 20 , "Mão direita" ],
         18:["Espada de sangue"   , 100, "Mão direita" ],
         19:["Espatula"           , 100, "Mão direita" ],
         20:["Flecha"             , 10 , "Munição"     ],
         21:["Grimório: Gelo"     , 100, "Mão direita" ],
         22:["Mapa"               , 20 , 0             ],
         23:["Narciso"            , 5  , "Flor"        ],
         24:["Pão"                , 5  , 0             ],
         25:["Perneira de ferro"  , 70 , "Perneira"    ],
         26:["Poção de cura"      , 20 , 0             ],
         27:["Poção de mana"      , 20 , 0             ],
         28:["Rapieira"           , 60 , "Mão direita" ],
         29:["Rosa"               , 5  , "Flor"        ],
         30:["Toque Blanche"      , 100, "Capacete"    ],
         31:["Camélia"            , 5  , "Flor"        ],
         32:["Ranúnculo"          , 5  , "Flor"        ],
         33:["Vela"               , 20 , "Mão esquerda"],
         34:["Vinho"              , 10 , 0             ],
         35:["Grimório: Fogo"     , 100, "Mão direita" ],
         36:["Flecha letal"       , 10 , "Munição"     ],
         37:["Cálice de prata"    , 5  , "Mão direita" ],
         38:["Cálice de ouro"     , 5  , "Mão esquerda"],
         39:["Joias"              , 0  , "Tesouro"     ],
         40:["Crânio de ouro"     , 0  , "Tesouro"     ],
         41:["Fonte da juventude" , 0  , "Tesouro"     ],
         42:["Pilha de ouro"      , 0  , "Tesouro"     ],
         43:["Baú do tesouro"     , 0  , "Tesouro"     ]
         }

#{ataque: valor, número de aplicações, tipo, alvos, dano dot, time dot, proporção}
inimigos = {
            1: ["Draugr"            , [15, 2, 2, 1, 1, 1]                     , {"Estocada":    [5, 1, 0, 1, 0, 0, 5],  "Empalar":     [7, 1, 0, 1, 0, 0, 3], "Bloquear" :[3, 1, 1, 0, 0, 0, 3]}],
            2: ["Draugr armadurado" , [15, 2, 2, 3, 0, 1]                     , {"Estocada":    [5, 1, 0, 1, 0, 0, 5],  "Empalar":     [6, 1, 0, 1, 0, 0, 2], "Bloquear" :[5, 1, 1, 0, 0, 0, 4]}],
            3: ["Guarda"            , [10, 1, 1, 0, 0, 0]                     , {"Empalar":     [3, 1, 0, 1, 0, 0, 2],  "Formação":    [2, 1, 1, 5, 0, 0, 1]}],
            4: ["Fantasma"          , [10, 0, 0, 0, 0, 0]                     , {"Assombrar":   [4, 1, 0, 1, 0, 0, 5],  "Retorno":     [10, 1, 2, 0, 0, 0, 1]}],
            5: ["Slime gigante"     , [int(50*backup["boss"]), 0, 0, 3, 0, 0] , {"Curar":       [5, 1, 2, 0, 0, 0, 1],  "Esmagar":     [6, 1, 0, 1, 0, 0, 1], "Veneno"   :[3, 1, 0, 1, 2, 5, 1]}],
            6: ["Slime pequeno"     , [5, 1, 1, 0, 0, 0]                      , {"Incomodar":   [2, 1, 0, 1, 0, 0, 1]}],
            7: ["Rei draugr"        , [30, 5, 5, 5, 1, 1]                     , {"Estocada":    [6, 1, 0, 1, 0, 0, 3],  "Determinação":[3, 1, 2, 0, 0, 0, 1], "Bloquear" :[5, 1, 1, 0, 0, 0, 2]}],
            8: ["Gárgula"           , [20, 0, 0, 6, 0, 0]                     , {"Arranhar":    [3, 1, 0, 1, 0, 0, 1]}],
            9: ["Leuchender Gloandi", [int(75*backup["boss"]), 0, 0, 5, 0, 0] , {"Marcar":      [6, 2, 0, 1, 0, 0, 3],  "Lacerar":     [3, 5, 0, 1, 0, 0, 1], "Infundir" :[1, 1, 0, 1, 3, 5, 3]}],
            10:["Rato"              , [5, 1, 1, 1, 1, 0]                      , {"Arranhar":    [3, 1, 0, 1, 0, 0, 1]}],
            11:["Rato grande"       , [10, 1, 2, 2, 0, 1]                     , {"Arranhar":    [3, 2, 0, 1, 0, 0, 1],  "Leptospirose":[4, 1, 0, 1, 1, 2, 1]}],
            12:["Le chef"           , [30, 0, 0, 3, 0, 1]                     , {"Espatulada":  [4, 1, 0, 1, 0, 0, 10], "Almoço":      [3, 1, 2, 0, 0, 0, 5], "TCSA"     :[15, 1, 0, 1, 0, 0, 1]}],
            13:["Atrómitos Ónkros"  , [int(50*backup["boss"]), 0, 0, 3, 0, 0] , {"Esmagar":     [6, 1, 0, 1, 0, 0, 1],  "Terremoto":   [2, 4, 0, 1, 0, 0, 1]}],
            14:["Mago"              , [15, 0, 0, 0, 0, 0]                     , {"Bola de fogo":[5, 1, 0, 1, 1, 3, 1],  "Choque":      [2, 5, 0, 1, 0, 0, 1], "Frostbite":[7, 1, 0, 1, 0, 0, 1]}]
            }

curses.wrapper(main, mapa, backup, back_do_back, itens)
