import time
import curses
from curses.textpad import rectangle
import random

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

def mover(stdscr, y, x, mapa, mapa_info, coordy, coordx, key = 0):   
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    verde = curses.color_pair(1)

    movimento = curses.newwin(y//2 if x//2 >= 76 else 18, x//2 if x//2 >= 76 else 76, 0, 0)
    mapa_tela = curses.newwin(11, 74, 1, x//4-37 if x//2 >= 76 else 1)

    movimento.border()
    movimento.refresh()
    
    mapa_tela.border()
    mapa_tela.refresh()

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

    direcoes = ["NORTE (N)", "SUL   (S) ", "LESTE (L)", "OESTE (O)"]
              
    for y0 in range(5):
        for x0 in range(5):
            if x0 == 0:
                if mapa_info[mapa[y0][x0]][1][2] == mapa_info[mapa[y0][x0+1]][1][3] == 0:
                    rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)
                else:
                    rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-1)
            elif x0 == 4:
                if mapa_info[mapa[y0][x0]][1][3] == mapa_info[mapa[y0][x0-1]][1][2] == 0:
                    rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)
                else:
                    rectangle(mapa_real, 3*y0+3, 24*(x0+1), 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)
            elif 0 < x0 < 4:                 
                if mapa_info[mapa[y0][x0]][1][2] == mapa_info[mapa[y0][x0+1]][1][3] == 0 and mapa_info[mapa[y0][x0]][1][3] == mapa_info[mapa[y0][x0-1]][1][2] == 1:
                    rectangle(mapa_real, 3*y0+3, 24*(x0+1), 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)
                    
                elif mapa_info[mapa[y0][x0]][1][2] != mapa_info[mapa[y0][x0+1]][1][3] and mapa_info[mapa[y0][x0]][1][3] == mapa_info[mapa[y0][x0-1]][1][2] == 1:
                    rectangle(mapa_real, 3*y0+3, 24*(x0+1), 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)

                elif mapa_info[mapa[y0][x0]][1][2] != mapa_info[mapa[y0][x0+1]][1][3] and mapa_info[mapa[y0][x0]][1][3] == mapa_info[mapa[y0][x0-1]][1][2] == 0:
                    rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)
                    
                elif mapa_info[mapa[y0][x0]][1][2] == mapa_info[mapa[y0][x0+1]][1][3] == 1 and mapa_info[mapa[y0][x0]][1][3] == mapa_info[mapa[y0][x0-1]][1][2] == 0:
                    rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-1)
                    
                elif mapa_info[mapa[y0][x0]][1][2] == mapa_info[mapa[y0][x0+1]][1][3] == 1 and mapa_info[mapa[y0][x0]][1][3] != mapa_info[mapa[y0][x0-1]][1][2]:
                    rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-1)

                elif mapa_info[mapa[y0][x0]][1][2] == mapa_info[mapa[y0][x0+1]][1][3] == 0 and mapa_info[mapa[y0][x0]][1][3] != mapa_info[mapa[y0][x0-1]][1][2]:
                    rectangle(mapa_real, 3*y0+3, 24*(x0+1)+10-len(mapa[y0][x0])//2, 3*y0+5, 24*(x0+2)-9-(len(mapa[y0][x0])+1)%2+len(mapa[y0][x0])//2)
                
                else:
                    rectangle(mapa_real, 3*y0+3, 24*(x0+1), 3*y0+5, 24*(x0+2)-1)
            else:
                rectangle(mapa_real, 3*y0+3, 24*(x0+1), 3*y0+5, 24*(x0+2)-1)
    for y0 in range(5):
        for x0 in range(5):
            if y0 != 0:
                if mapa_info[mapa[y0][x0]][1][0] == 1 == mapa_info[mapa[y0-1][x0]][1][1]:
                    mapa_real.addch(3*y0+2, 24*(x0+1)+9, curses.ACS_URCORNER)
                    mapa_real.addstr(3*y0+2, 24*(x0+1)+10, "     ")
                    mapa_real.addch(3*y0+2, 24*(x0+1)+14, curses.ACS_ULCORNER)
                    mapa_real.addch(3*y0+3, 24*(x0+1)+9, curses.ACS_LRCORNER)
                    mapa_real.addstr(3*y0+3, 24*(x0+1)+10, "     ")
                    mapa_real.addch(3*y0+3, 24*(x0+1)+14, curses.ACS_LLCORNER)
            if x0 != 0:
                if mapa_info[mapa[y0][x0]][1][3] == 1 == mapa_info[mapa[y0][x0-1]][1][2]:
                    mapa_real.addch(3*y0+5, 24*(x0+1)-1, curses.ACS_HLINE)
                    mapa_real.addch(3*y0+5, 24*(x0+1), curses.ACS_HLINE)
                    mapa_real.addstr(3*y0+4, 24*(x0+1)-1, "  ") 
                    mapa_real.addch(3*y0+3, 24*(x0+1)-1, curses.ACS_HLINE)
                    mapa_real.addch(3*y0+3, 24*(x0+1), curses.ACS_HLINE)
                    
            if y0 == coordy and x0 == coordx:
                mapa_real.addstr(3*y0+4, 24*(x0+1)+11-len(mapa[y0][x0])//2, f"> {mapa[y0][x0][:-1]} <", curses.A_BOLD)
            elif mapa_info[mapa[y0][x0]][0] == 1:
                mapa_real.addstr(3*y0+4, 24*(x0+1)+13-len(mapa[y0][x0])//2, mapa[y0][x0][:-1])
    rectangle(mapa_real, 2, 23, 18, 144)

    movimento.addstr(12, x//4-37 if x//2 >= 76 else 1, "MOVIMENTO:", curses.A_BOLD)
    for i in range(4):
        movimento.addstr(13+i, x//4-37 if x//2 >= 76 else 1, f"{i+1} - {direcoes[i]}", curses.A_BOLD)
            
        if (i == 0 and coordy == 0) or (i == 1 and coordy == 4) or (i == 2 and coordx == 4) or (i == 3 and coordx == 0):
            movimento.addstr(" (Fora do mapa)"+" "*4)
           
        elif i == 0 and mapa_info[mapa[coordy][coordx]][1][0] == 0:
            if mapa_info[mapa[coordy-1][coordx]][1][1] == 1:
                movimento.addstr(" (Porta trancada)"+" "*2)
            else:
                movimento.addstr(" (Parede)"+" "*10)
        elif i == 0 and mapa_info[mapa[coordy][coordx]][1][0] == 1:
            if mapa_info[mapa[coordy-1][coordx]][1][1] == 0:
                movimento.addstr(" (Destrancar porta)")
            else:
                movimento.addstr(" "*19)
             
        elif i == 1 and mapa_info[mapa[coordy][coordx]][1][1] == 0:
            if mapa_info[mapa[coordy+1][coordx]][1][0] == 1:
                movimento.addstr(" (Porta trancada)"+" "*2)
            else:
                movimento.addstr(" (Parede)"+" "*10)
        elif i == 1 and mapa_info[mapa[coordy][coordx]][1][1] == 1:
            if mapa_info[mapa[coordy+1][coordx]][1][0] == 0:
                movimento.addstr(" (Destrancar porta)")
            else:
                movimento.addstr(" "*19)
          
        elif i == 2 and mapa_info[mapa[coordy][coordx]][1][2] == 0:
            if mapa_info[mapa[coordy][coordx+1]][1][3] == 1:
                movimento.addstr(" (Porta trancada)"+" "*2)
            else:
                movimento.addstr(" (Parede)"+" "*10)
        elif i == 2 and mapa_info[mapa[coordy][coordx]][1][2] == 1:
            if mapa_info[mapa[coordy][coordx+1]][1][3] == 0:
                movimento.addstr(" (Destrancar porta)")
            else:
                movimento.addstr(" "*19)
       
        elif i == 3 and mapa_info[mapa[coordy][coordx]][1][3] == 0:
            if mapa_info[mapa[coordy][coordx-1]][1][2] == 1:
                movimento.addstr(" (Porta trancada)"+" "*2)
            else:
                movimento.addstr(" (Parede)"+" "*10)
        elif i == 3 and mapa_info[mapa[coordy][coordx]][1][3] == 1:
            if mapa_info[mapa[coordy][coordx-1]][1][2] == 0:
                movimento.addstr(" (Destrancar porta)")
            else:
                movimento.addstr(" "*19)
    movimento.refresh()

    auy = aux = 0
    
    if key in ["1", "NORTE", "N"] and coordy != 0 and mapa_info[mapa[coordy][coordx]][1][0] == 1:
        if mapa[coordy][coordx] == "Sala do trono1":
            mapa_info["Sala de jantar1"][1][1] = 1
        auy = -3
        coordy -= 1
    elif key in ["2", "SUL", "S"] and coordy != 4 and mapa_info[mapa[coordy][coordx]][1][1] == 1:
        if mapa[coordy][coordx] == "Dispensa1":
            mapa_info["Entrada1"][1][0] = 1
        auy = 3
        coordy += 1
    elif key in ["3", "LESTE", "L"] and coordx != 4 and mapa_info[mapa[coordy][coordx]][1][2] == 1:
        if mapa[coordy][coordx] == "Jardim1":
            mapa_info["Guarita2"][1][3] = 1
        aux = 24
        coordx += 1
    elif key in ["4", "OESTE", "O"] and coordx != 0 and mapa_info[mapa[coordy][coordx]][1][3] == 1:
        aux = -24
        coordx -= 1
        
    if aux != 0:
        for i in range(0, aux*25//24, int(aux/(aux**2)**(1/2))):
            mapa_real.refresh(3*coordy, 24*coordx-aux+i, 2, x//4-36 if x//2 >= 76 else 2, 10, x//4+35 if x//2 >= 76 else 73)
            time.sleep(0.01)
    elif auy != 0:
        for i in range(0, auy*4//3, int(auy/(auy**2)**(1/2))):
            mapa_real.refresh(3*coordy-auy+i, 24*coordx, 2, x//4-36 if x//2 >= 76 else 2, 10, x//4+35 if x//2 >= 76 else 73)
            time.sleep(0.05)
    else:
        mapa_real.refresh(3*coordy, 24*coordx, 2, x//4-36 if x//2 >= 76 else 2, 10, x//4+35 if x//2 >= 76 else 73)
        
    mapa_info[mapa[coordy][coordx]][0] = 1
    return coordy, coordx

def jogar(stdscr, y, x, config, mapa, mapa_info, coordy, coordx):
    stdscr.clear()
    curses.echo()
    rectangle(stdscr, y//2, 0, y-1, x//2-1)
    
    stdscr.refresh()

    painel = curses.newwin(y//2-2, x//2-2 if x//2-2 >= 74 else 74, y//2+1, 1)
    painel.box()
    mover(stdscr, y, x, mapa, mapa_info, coordy, coordx)

    while True:
        painel.clear()
        painel.addstr(0, 4, "GERAL:", curses.A_BOLD)
        painel.addstr(1, 4, "5 - VOLTAR PARA O MENU (V)", curses.A_BOLD)
        painel.addstr(3, 4, "ESCOLHA UMA AÇÃO: ", curses.A_BOLD)
        painel.refresh()
        
        key = str(painel.getstr().decode("utf-8")).upper()
        if key in ["1", "2", "3", "4", "NORTE", "SUL", "LESTE", "OESTE", "N", "S", "L", "O"]:
            coordy, coordx = mover(stdscr, y, x, mapa, mapa_info, coordy, coordx, key)
            mover(stdscr, y, x, mapa, mapa_info, coordy, coordx)
        elif key in ["5", "VOLTAR", "V"]:
            return coordy, coordx
        
def opcoes(stdscr, y, x, config):
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

    curses.init_pair(10, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(11, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(12, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(13, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(14, curses.COLOR_BLUE, curses.COLOR_BLACK)

    ops = 0
    while True:
        opcoes_tela.clear()
        desc.clear()
        opcoes_tela.addstr(0, 2, "DIFICULDADE: {}".format(config["diff"][0]))
        opcoes_tela.addstr(1, 2, "PERSONAGEM: {}".format(config["person"]))
        if ops == 0:
            opcoes_tela.addstr(0, 2, "> DIFICULDADE: {} <".format(config["diff"][0]), curses.A_BOLD)
        elif ops == 1:
            opcoes_tela.addstr(1, 2, "> PERSONAGEM: {} <".format(config["person"]), curses.A_BOLD)
        opcoes_tela.refresh()
        desc.refresh()
        try:
            key = opcoes_tela.getkey()
        except:
            continue
        if ord(key) == 27:
            return config
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
                    for i in range(6):
                        desc.addstr(linha[i])
                elif subop == 1:
                    opcoes_tela.addstr(2, 4, "> MÉDIO <", curses.A_BOLD)
                    for i in range(6):
                        desc.addstr(linha[i + 7])
                elif subop == 2:
                    opcoes_tela.addstr(3, 4, "> DIFÍCIL <", curses.A_BOLD)
                    for i in range(6):
                        desc.addstr(linha[i + 14])
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
                        config["diff"] = ["FÁCIL", 0]
                        break
                    elif subop == 1:
                        config["diff"] = ["MÉDIO", 1]
                        break
                    elif subop == 2:
                        config["diff"] = ["DIFÍCIL", 2]
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
                        desc.addstr(linha[i + 21])
                elif subop == 1:
                    opcoes_tela.addstr(2, 4, "> LADINO <", curses.A_BOLD)
                    for i in range(7):
                        desc.addstr(linha[i + 28])
                elif subop == 2:
                    opcoes_tela.addstr(3, 4, "> MAGO <", curses.A_BOLD)
                    for i in range(13):
                        desc.addstr(linha[i + 37])
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
                        config["person"] = "GUERREIRO"
                        break
                    elif subop == 1:
                        config["person"] = "LADINO"
                        break
                    elif subop == 2:
                        config["person"] = "MAGO"
                        break

def main(stdscr):
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
    coordy = 2
    coordx = 0
    config = {"diff": ["FÁCIL", 1], "person": "GUERREIRO"}
    curses.curs_set(0)
    tinta, tinta_fundo = intro(stdscr, y, x, 0)
    while True:
        stdscr.clear()
        intro(stdscr, y, x, 1, tinta, tinta_fundo)
        selec = menu(stdscr, y, x, selec)
        if selec == 0:
            coordy, coordx = jogar(stdscr, y, x, config, mapa, mapa_info, coordy, coordx)
            curses.noecho()
        elif selec == 1:
            config = opcoes(stdscr, y, x, config)
        elif selec == 2:
            break
        
mapa = [["Cozinha1", "Sala de jantar1", "Encruzilhada1", "Guarita1", "Masmorra1"],
            ["Dispensa1", "Sala do trono1", "Salão principal1", "Expurgo1", "Catacumbas1"],
            ["Entrada1", "Corredor lateral1", "Encruzilhada2", "Quartéis1", "Paiol1"],
            ["Corredor vertical1", "Jardim1", "Guarita2", "Quarto do rei1", "Porão1"],
            ["Torre do vigia1", "Grimório1", "Sala do tesouro1", "Quarto secreto1", "Torre vermelha1"]]
        
mapa_info = {
             "Catacumbas1":        [0, [1,0,0,0]],
             "Corredor lateral1":  [0, [0,0,1,1]],
             "Corredor vertical1": [0, [1,1,0,0]],
             "Cozinha1":           [0, [0,1,1,0]],
             "Dispensa1":          [0, [1,1,0,0]],
             "Encruzilhada1":      [0, [0,1,1,1]],
             "Encruzilhada2":      [0, [1,1,1,1]],
             "Entrada1":           [1, [0,1,1,0]],
             "Expurgo1":           [0, [1,0,0,0]],
             "Grimório1":          [0, [1,0,0,1]],
             "Guarita1":           [0, [0,1,1,1]],
             "Guarita2":           [0, [1,1,1,0]],
             "Jardim1":            [0, [0,1,1,0]],
             "Masmorra1":          [0, [0,1,0,1]],
             "Paiol1":             [0, [0,1,0,1]],
             "Porão1":             [0, [1,0,0,0]],
             "Quartéis1":          [0, [0,0,1,1]],
             "Quarto do rei1":     [0, [0,0,0,1]],
             "Quarto secreto1":    [0, [1,0,0,0]],
             "Sala de jantar1":    [0, [0,0,1,1]],
             "Sala do trono1":     [0, [1,0,1,0]],
             "Sala do tesouro1":   [0, [1,0,0,0]],
             "Salão principal1":   [0, [1,1,0,1]],
             "Torre do vigia1":    [0, [1,0,1,0]],
             "Torre vermelha1":    [0, [1,0,0,0]]
             }

curses.wrapper(main)
