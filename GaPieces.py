import random
from tkinter import *
from heapq import nsmallest
import time
import sys

population_size = 10
generations = 10

piece_colors = ["gold", "deepskyblue", "green3", "tan1", "orchid1", 
    "purple1", "red2", "palegreen", "goldenrod", "thistle2", "lightblue3",
    "thistle"]

random.seed(0)

if (len(sys.argv) > 1):
    filename = sys.argv[1]

    try:
        with open(filename) as f:
            content = f.readline()
    except FileNotFoundError:
        sys.exit('Could not find file' + filename)
        
else:
    filename = input("Type filename: ")
    content = open(filename, "r")
    l = content.read()
    line = l.rsplit()

for x in range(len(line)):
    line[x] = int(line[x])

width = line[0]
height = line[1]
individuals = line[2]

def MakeRectObj(w,h,x1,y1,c):
    return {"width" : w, "height" : h, "color": c, "x1" : x1, "y1" : y1, "x2": x1+w, "y2": y1+h}

def PopulationCount(x, population, totalSquareOverlap):
    return {"index" : x, "Population": population[x], "Overlap" : totalSquareOverlap}

root = Tk()      
canvas = Canvas(root, width = width, height = height, bg='khaki')   
canvas.pack()

totalPopulation = [0 for j in range(population_size)]

for population_count in range(population_size):
    size_countw = 3
    size_counth = 4
    totalIndividuals = [0 for x in range(individuals)]
    for indv_count in range(individuals):
        w = line[size_countw]
        h = line[size_counth]
        c = piece_colors[indv_count]
        x1 = random.randint(0, width - w)
        y1 = random.randint(0, height - h)

        size_countw += 2
        size_counth += 2
    
        totalIndividuals[indv_count] = MakeRectObj(w,h,x1,y1,c)
      

    totalPopulation[population_count] = totalIndividuals


def Crossover(crossover_indv, i):
    new_valuex1_0 = crossover_indv[0][i].get("x1")
    new_valuex1_1 = crossover_indv[1][i].get("x1")
    new_valuey1_0 = crossover_indv[0][i].get("y1")
    new_valuey1_1 = crossover_indv[1][i].get("y1")
   
    crossover_indv[0][i]["x1"] = new_valuex1_1
    crossover_indv[1][i]["x1"] = new_valuex1_0
    crossover_indv[0][i]["y1"] = new_valuey1_1
    crossover_indv[1][i]["y1"] = new_valuey1_0

    prev_valuex2_0 = crossover_indv[0][i].get("x2")
    prev_valuex2_1 = crossover_indv[1][i].get("x2")
    prev_valuey2_0 = crossover_indv[0][i].get("y2")
    prev_valuey2_1 = crossover_indv[1][i].get("y2")

    new_valuex2_0 = crossover_indv[0][i]["x1"] + (prev_valuex2_0 - new_valuex1_0)
    new_valuex2_1 = crossover_indv[1][i]["x1"] + (prev_valuex2_1 - new_valuex1_1)
    new_valuey2_0 = crossover_indv[0][i]["y1"] + (prev_valuey2_0 - new_valuey1_0)
    new_valuey2_1 = crossover_indv[1][i]["y1"] + (prev_valuey2_1 - new_valuey1_1)

    crossover_indv[0][i]["x2"] = new_valuex2_0
    crossover_indv[0][i]["y2"] = new_valuey2_0
    crossover_indv[1][i]["x2"] = new_valuex2_1
    crossover_indv[1][i]["y2"] = new_valuey2_1    

    return crossover_indv[0], crossover_indv[1]
     
def Mutation(indiv):
    new_valuex1 = indiv.get("x1")
    new_valuex2 = indiv.get("x2")
    new_valuey1 = indiv.get("y1")
    new_valuey2 = indiv.get("y2")

    random_valuex = random.randint(-20,20)
    random_valuey = random.randint(-20,20)
    
    indiv["x1"] = new_valuex1 + random_valuex 
    indiv["x2"] = new_valuex2 + random_valuex
    indiv["y1"] = new_valuey1 + random_valuey
    indiv["y2"] = new_valuey2 + random_valuey

    return indiv

for looper in range(generations):
    for indv_count in range(population_size):
        crossing_indiv = totalPopulation
        for i in range(individuals):
            mutating_individual =  totalPopulation[indv_count]
            indiv = mutating_individual[i]
            
            
                
            crossover_indv = random.sample(crossing_indiv, 2)   

            #print("Crossover x: ", crossover_indv[0])
            #print("Crossover y: ", crossover_indv[1])
            
            index1 = crossing_indiv.index(crossover_indv[0])
            index2 = crossing_indiv.index(crossover_indv[1])     


            cross_indvx, cross_indvy = Crossover(crossover_indv, i)

            #print("Results x: ", cross_indvx)
            #print("Results y: ", cross_indvy)
            
            totalPopulation[index1] = cross_indvx
            totalPopulation[index2] = cross_indvy

            mutating_characteristic = Mutation(indiv)
            totalPopulation[indv_count][i] = mutating_characteristic
            
        canvas.create_rectangle(0, 0, width, height, fill='khaki')   
        display_individual = totalPopulation[indv_count]

        totalXOverlap = 0
        totalYOverlap = 0
        totalSquareOverlap = 0

        for piece_count in range(individuals):
            canvas.create_rectangle(display_individual[piece_count].get("x1"),
                display_individual[piece_count].get("y1"),
                display_individual[piece_count].get("x2"),
                display_individual[piece_count].get("y2"),
                fill = display_individual[piece_count].get("color"),
                outline = "black")
                #tkFont.Font(family='Helvetica',size=36, weight='bold') # http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/fonts.html
            canvas.create_text(display_individual[piece_count].get("x1") + 20,
                display_individual[piece_count].get("y1") + 20,
                text=str(piece_count))

                    #for each second piece in this individual (the for loop this is contained in runs through the 'first' pieces)
                        #if the second and first piece are not the same piece
                            #if the first piece's right side x value is greater than the second piece's left side x value,
                            #AND the first piece's left side x value is less than the second piece's left side x value
                                #get the x overlap for that piece pair, and add it to the total x overlap
                            #elif the pieces' right side x values are the same, the x overlap is 200. This only works
                            #with the current squares of side lengths 200 obviously, I'll change it later

                    #checking for y overlap is the same as x but with y values

            for pieceToCompare in range(individuals):

                yOverlap = 0
                xOverlap = 0

                if pieceToCompare != piece_count:
                    if display_individual[piece_count].get("x2") > display_individual[pieceToCompare].get("x1") and (display_individual[piece_count].get("x1") < display_individual[pieceToCompare].get("x1")):
                        xOverlap = abs(display_individual[piece_count].get("x2") - display_individual[pieceToCompare].get("x1"))
                        totalXOverlap = totalXOverlap + xOverlap
                        #print("xOverlap for ", piece_count, "with", pieceToCompare, "is ", xOverlap)
                    elif display_individual[piece_count].get("x2") == display_individual[pieceToCompare].get("x2"):
                        xOverlap = 200
                        totalXOverlap = totalXOverlap + xOverlap
                        #print("COMPLETE OVERLAP xOverlap for ", piece_count, "with", pieceToCompare, "is ", xOverlap)

                if pieceToCompare != piece_count:
                    if display_individual[piece_count].get("y2") > display_individual[pieceToCompare].get("y1") and (display_individual[piece_count].get("y1") < display_individual[pieceToCompare].get("y1")):
                        yOverlap = abs(display_individual[piece_count].get("y2") - display_individual[pieceToCompare].get("y1"))
                        totalYOverlap = totalYOverlap + yOverlap
                        #print("yOverlap for ", piece_count, "with", pieceToCompare, "is ", yOverlap)
                    elif display_individual[piece_count].get("y2") == display_individual[pieceToCompare].get("y2"):
                        yOverlap = 200
                        totalYOverlap = totalYOverlap + yOverlap
                        #print("COMPLETE OVERLAP yOverlap for ", piece_count, "with", pieceToCompare, "is ", yOverlap)

        totalSquareOverlap = totalXOverlap * totalYOverlap

        #print("Total x overlap for individual: ", totalXOverlap)
        #print("Total y overlap for individual: ", totalYOverlap)
        #print("Total square overlap for individual: ", totalSquareOverlap)

        canvas.update()
        time.sleep(1) # HARDCODED TIME -- pause briefly between generations

            
        #selection_list[POPULATION_SIZE]= PopulationCount(x ,population[x], totalSquareOverlap)
        #print(selection_list)
        

mainloop()   # Graphics loop -- This statement follows all other statements
