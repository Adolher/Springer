import time, threading

def pause(scvwert):
    time.sleep(scvwert.get())

def frei_rechnung(brett, zug):
    for i in range(8):
        for j in range(8):
            if brett[i][j].besucht == 0 or brett[i][j].besucht == 1:
                frei=0
                if i+2 < 8 and j+1 < 8 and (brett[i+2][j+1].besucht == 0 or brett[i+2][j+1].besucht == zug or brett[i+2][j+1].besucht == 1):
                    frei +=1
                if i+1 < 8 and j+2 < 8 and (brett[i+1][j+2].besucht == 0 or brett[i+1][j+2].besucht == zug or brett[i+1][j+2].besucht == 1):
                    frei +=1
                if i-1 >= 0 and j+2 < 8 and (brett[i-1][j+2].besucht == 0 or brett[i-1][j+2].besucht == zug or brett[i-1][j+2].besucht == 1):
                    frei +=1
                if i-2 >= 0 and j+1 < 8 and (brett[i-2][j+1].besucht == 0 or brett[i-2][j+1].besucht == zug or brett[i-2][j+1].besucht == 1):
                    frei +=1
                if i-2 >= 0 and j-1 >= 0 and (brett[i-2][j-1].besucht == 0 or brett[i-2][j-1].besucht == zug or brett[i-2][j-1].besucht == 1):
                    frei +=1
                if i-1 >= 0 and j-2 >= 0 and (brett[i-1][j-2].besucht == 0 or brett[i-1][j-2].besucht == zug or brett[i-1][j-2].besucht == 1):
                    frei +=1
                if i+1 < 8 and j-2 >= 0 and (brett[i+1][j-2].besucht == 0 or brett[i+1][j-2].besucht == zug or brett[i+1][j-2].besucht == 1):
                    frei +=1
                if i+2 < 8 and j-1 >= 0 and (brett[i+2][j-1].besucht == 0 or brett[i+2][j-1].besucht == zug or brett[i+2][j-1].besucht == 1):
                    frei +=1
                if brett[i][j].besucht == 0:
                    if frei<2:
                        return True
                    brett[i][j].frei = frei
                if brett[i][j].besucht == 1 and frei<1:
                    return True
    return False

def ausgabe(brett, zug, scvwert):
    for i in range(8):
        for j in range(8):
            brett[i][j].ausgabe(zug, i, j)
    pause(scvwert)

def move(brett, zug, x, y, erg_list, l, scvwert):
    if zug < brett[x][y].min:
        brett[x][y].min = zug
    if zug > brett[x][y].max:
        brett[x][y].max = zug
    brett[x][y].besucht = zug

    if frei_rechnung(brett, zug):
        return True
    ausgabe(brett, zug, scvwert)

    if x+2 < 8 and y+1 < 8 and brett[x+2][y+1].besucht == 0:            # 0
        zug += 1
        x += 2
        y += 1
#        pause(scv)
        if move(brett, zug, x, y, erg_list, l, scvwert):
            brett[x][y].besucht = 0
            x -= 2
            y -= 1
            zug -= 1
    if x+1 < 8 and y+2 < 8 and brett[x+1][y+2].besucht == 0:            # 1
        zug += 1
        x += 1
        y += 2
#        pause(scv)
        if move(brett, zug, x, y, erg_list, l, scvwert):
            brett[x][y].besucht = 0
            x -= 1
            y -= 2
            zug -= 1
    if x-1 >= 0 and y+2 < 8 and brett[x-1][y+2].besucht == 0:            # 2
        zug += 1
        x -= 1
        y += 2
#        pause(scv)
        if move(brett, zug, x, y, erg_list, l, scvwert):
            brett[x][y].besucht = 0
            x += 1
            y -= 2
            zug -= 1
    if x-2 >= 0 and y+1 < 8 and brett[x-2][y+1].besucht == 0:            # 3
        zug += 1
        x -= 2
        y += 1
#        pause(scv)
        if move(brett, zug, x, y, erg_list, l, scvwert):
            brett[x][y].besucht = 0
            x += 2
            y -= 1
            zug -= 1
    if x-2 >= 0 and y-1 >= 0 and brett[x-2][y-1].besucht == 0:            # 4
        zug += 1
        x -= 2
        y -= 1
#        pause(scv)
        if move(brett, zug, x, y, erg_list, l, scvwert):
            brett[x][y].besucht = 0
            x += 2
            y += 1
            zug -= 1
    if x-1 >= 0 and y-2 >= 0 and brett[x-1][y-2].besucht == 0:            # 5
        zug += 1
        x -= 1
        y -= 2
#        pause(scv)
        if move(brett, zug, x, y, erg_list, l, scvwert):
            brett[x][y].besucht = 0
            x += 1
            y += 2
            zug -= 1
    if x+1 < 8 and y-2 >= 0 and brett[x+1][y-2].besucht == 0:            # 6
        zug += 1
        x += 1
        y -= 2
#        pause(scv)
        if move(brett, zug, x, y, erg_list, l, scvwert):
            brett[x][y].besucht = 0
            x -= 1
            y += 2
            zug -= 1
    if x+2 < 8 and y-1 >= 0 and brett[x+2][y-1].besucht == 0:            # 7
        zug += 1
        x += 2
        y -= 1
#        pause(scv)
        if move(brett, zug, x, y, erg_list, l, scvwert):
            brett[x][y].besucht = 0
            x -= 2
            y += 1
            zug -= 1

    if zug == 64:
        if vergl_erg(erg_list, brett):
            brett[x][y].vs += 1
            brett[x][y].b["text"] = "Lösungen: " + str(brett[x][y].vs) + "\n\n" + "zug: " + str(brett[x][y].besucht)
            save_erg(erg_list, brett)
        lsg(brett, l)
        #time.sleep(2)

    return True

def save_erg(erg_list, brett):
    kopie=[[0] * 8 for i in range(8)]
    for i in range(8):
        for j in range(8):
            kopie[i][j] = brett[i][j].besucht
    erg_list.append(kopie)

def vergl_erg(erg_list, brett):
    ungleich=0
    if len(erg_list) > 0:
        for e in range(len(erg_list)):
            for i in range(8):
                u = 0
                for j in range(8):
                    if erg_list[e][i][j] != brett[i][j].besucht:
                        ungleich += 1
                        u = 1
                        break
                if u == 1:
                    break
        if ungleich == len(erg_list):
            return True
        return False
    else:
        return True

def lsg(brett, l):
    loesungen = 0
    for i in range(8):
        for j in range(8):
            loesungen += brett[i][j].vs
    l["text"] = "Lösungen gesamt: " + str(loesungen)
