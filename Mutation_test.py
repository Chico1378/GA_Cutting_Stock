import random
import time
from tkinter import *
master = Tk()

generations = 100
individuals = []
indv = []
new_coords = []
mutation = []

random.seed(0)

filename = open("pieces.txt", "r")
pieces_size = filename.read()
pieces = pieces_size.rsplit()
print(pieces)
piece_colors = ["gold", "deepskyblue", "green3", "tan1", "orchid1", 
	"purple1", "red2", "palegreen", "goldenrod", "thistle2", "lightblue3",
	"thistle"]

window = Canvas(master, width=int(pieces[0]), height = int(pieces[1]))

window.pack()

x = 3
y = 4

for i in range (int(pieces[2])):
    new_coords.append([])
    x1 = int(pieces[x])
    y1 = int(pieces[y])
    w = random.randint(0,800 - int(pieces[x]))
    h = random.randint(0,800 - int(pieces[y]))
    color = random.choice(piece_colors)
    individuals.append(window.create_rectangle(x1, y1, w, h, fill=color, outline="black" ))
    indv.extend([[x1,y1,w,h]])
    x += 2
    y += 2

mutation = new_coords

for l in range(generations):
    for i in range(int(pieces[2])):
        x = 3
        y = 4
        indv[i][0] = random.randint(0,random.randint(0,800 - int(pieces[x])))
        indv[i][2] = random.randint(0,random.randint(0,800 - int(pieces[x])))
        x += 2
        y += 2
                    
    for z in range(int(pieces[2])):
        window.coords(individuals[z], indv[z])

        
    new_coords.clear()

    for i in range(int(pieces[2])):
        new_coords.append([])
    
    window.update()
    time.sleep(0.02)

    
mainloop()
