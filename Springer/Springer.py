from tkinter import *
from farben import *
import threading
import funkt
root = Tk()


# ### Zeit nehmen (zwischen einzelnen Lösungen? oder Gesamt?) -> Klasse Lösungen
# ### Lösungen anzeigen lassen (2 Stück) mit vor und zurück Schaltflächen (eigenes Fenster oder eigener Frame?) -> Klasse Lösungen
# ### Schleife um alle Startoptionen durchzugehen ⇦ Zugmöglichkeiten in Schleife und 0 bis 7 mit Random auswählen
# ### Geschwindigkeitsregler -- incl. manueller Schritteingabe ⇒ bei Klick in Funktion mit While(klick==1) if klick == 1 bei klick -> klick =0 // klick auf schieber -> normale pausen()
# ### Nach Start Buttons in Labels umwandeln

# #----## Geschwindigkeitsregler
# #----## Lösungen gesammelt unterhalb anzeigen
# #----## 2. Lösungen auf Unterschiedlichkeit prüfen -> Klasse Lösungen -> eigener Thread
# #----## 1. Lösungen speichern -> Liste mit Arrays -> Klasse Lösungen (alle Felder speichern und vergleichen)
# #----## 0. Modularisieren -> UI / Klassen / Funktionen / Farben
# #----## Anzahl Lösungen anzeigen -> Klasse Lösungen
# #----## min in Klasse Feld anzeigen
# #----## c in 'frei' umbenennen


zug = 1
brett = [[0] * 8 for i in range(8)]
erg_list = []


class Feld:
    def __init__(self, x, y):
        self.besucht = 0
        self.max = 0
        self.min = 65
        self.vs = 0              # vs ⇨ Vier und Sechzig
        self.frei = 0
        self.b = Button(root, height=5, width=10, command=lambda: extstart(x, y))
        self.b.grid(row=x, column=y)
        if (x+y) % 2 == 1:
            self.b["bg"] = weiss
        else:
            self.b["bg"] = schwarz
        
    def ausgabe(self, zug, x, y):
        if self.besucht == 0:
            if self.vs > 0:
                self.b["text"] = "Lösungen: " + str(self.vs) + "\n\n" + "frei = " + str(self.frei)
            else:
                self.b["text"] = "frei = " + str(self.frei)
        else:
            if self.vs > 0:
                self.b["text"] = "Lösungen: " + str(self.vs) + "\n\n" + "zug: " + str(self.besucht)
            else:
                self.b["text"] = "zug: " + str(self.besucht)
        if self.besucht == zug:
            self.b["bg"] = rot
        elif self.besucht == 1:
            self.b["bg"] = magenta
        elif self.besucht == 0:
            if (x+y) % 2 == 1:
                self.b["bg"] = weiss
            else:
                self.b["bg"] = schwarz
                self.b["fg"] = weiss
        elif self.besucht == zug-1:
            self.b["bg"] = orangeRed
        elif self.besucht == zug-2:
            self.b["bg"] = gold
        elif self.besucht > 0:
            if self.min == self.max:
                if (x+y) % 2 == 1:
                    self.b["bg"] = cyan
                else:
                    self.b["bg"] = blue
            else:
                if (x+y) % 2 == 1:
                    self.b["bg"] = gruen
                else:
                    self.b["bg"] = gruen4


for i in range(8):
    for j in range(8):
        brett[i][j] = Feld(i, j)


la = Label(root, height=5, width=80)
la.grid(row=8, column=0, columnspan=8)
la["text"] = "Lösungen gesamt: 0"

schieber = Label(root, height=45, width=30)
schieber.grid(row=0, column=8, rowspan=9)


def sch_anzeigen():
    lb["text"] = "Pause " + str(scvwert.get()) + " Sekunden"


lb = Label(schieber, text="Pause 3 Sekunden", width=30)
lb.pack()

scvwert = DoubleVar()
scvwert.set(3)

scv = Scale(schieber, width=30, length=450, orient="vertical", from_=0, to=3, resolution=0.1, tickinterval=0.5, label="Sek", command=sch_anzeigen, variable=scvwert)
scv.pack()


def extstart(x, y):
    t = threading.Thread(target=funkt.move, args=(brett, zug, x, y, erg_list, la, scvwert))
    t.start()


root.mainloop()
