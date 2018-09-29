import time
import random
import sys

random.seed(0)  # Initialize internal state of the random number generator.

NUMBER_OF_GENERATIONS = 10 # HARDCODED Number of generations of evolution
POPULATION_SIZE = 10  # HARDCODED Number of individuals in population
mutation_list_coords = [[],[],[],[]]

idealSquareOverlap = 0 #Total square overlap goal to judge best individual by

piece_colors = ["gold", "deepskyblue", "green3", "tan1", "orchid1", 
    "purple1", "red2", "palegreen", "goldenrod", "thistle2", "lightblue3",
    "thistle"]

#Reading File from the command Line
if (len(sys.argv) > 1):
    filename = sys.argv[1]
    
    try:
        with open(filename) as f:
            content = f.readlines()
    except FileNotFoundError:
        sys.exit('Could not find file ' + filename)
        
    for i in range(0, len(content)):
        line = content[i].split()
        for j in range(0, len(line)):
            print(str(line[j]))
            
#Reading a specific File 
else:
    filename = open("pieces.txt", "r")
    pieces_size = filename.read()
    pieces = pieces_size.rsplit()
    print(pieces)            

#Turning values inside the file into INTs
for i in range(int(pieces[2])):
    pieces[i] = int(pieces[i])
    
''' 
Definition of a class Piece that has data members:
    xcoord	X coordinate of the upper left corner
    ycoord	Y coordinate of the upper left corner
    . . . (other values as desired)
    
Create an object of the class Piece using     Piece(x, y, ...)
Place an object of the class Piece into a list   myList.append(myPiece)
'''
class Piece:
    def __init__(self, xcoord, ycoord): # Add other values to this list
        self.x = xcoord
        self.y = ycoord
    def setX(self, xcoord):
        self.x = xcoord
    def setY(self, ycoord):
        self.y = ycoord
    def getX(self):
        return self.x
    def getY(self):
        return self.y

    # As you wish, define other function members of class Piece
    # to return other individual values or a set of several
    # values within a tuple or list.


'''
Create a Piece object in a dictionary data structure, using the parameters
for the piece position.
TBD -- this places the piece within the stock (as opposed to putting
at least the UL corner but not necessarily the LR corner in stock)
'''
# https://www.w3schools.com/python/python_dictionaries.asp
def makeRectObj(w, h, x1, y1, c):
    return { "width": w, "height": h, "color": c,
        "x1": x1, "y1": y1,
        "x2": x1+w, "y2": y1+h}  # Return a dictionary object



# Use tkinter to display stock and pieces
from tkinter import *      
root = Tk()      
canvas = Canvas(root, width = pieces[0], height = pieces[1], bg='khaki')   
canvas.pack()

x = 3
y = 4

population = [0 for i in range(POPULATION_SIZE)]
print("population yoooooo: ", population)
for indiv_count in range(POPULATION_SIZE):
    x = 3
    y = 4
    individual = [0 for j in range(pieces[2])]
    for piece_count in range(pieces[2]):
        w = int(pieces[x])
        h = int(pieces[y])
        c = piece_colors[piece_count]  
        x1 = random.randint(0, pieces[0] - w)
        y1 = random.randint(0, pieces[1] - h)

        # An individual is an array of dictionary objects
        individual[piece_count] = makeRectObj(w, h, x1, y1, c)
        #print(individual[piece_count])
        #print("	Piece ", piece_count, " x1 is ", (individual[piece_count]).get("x1"))



        # TBD  -- display the  first individual
        # in general, display the fittest individual of this generation
        if indiv_count == 0:
            canvas.create_rectangle(x1, y1, x1+w, y1+h, fill=c, outline='black')
            canvas.update()
            time.sleep(0.02) # HARDCODED



        print("individual  is ", individual)
        print()

        x += 2
        y += 2
        
    # The population is an array of individual objects
    population[indiv_count] = individual
    print("population[", indiv_count,"] is ", population[indiv_count])
    print()
    #print("Piece ", piece_count, " x1 is ", (population[piece_count]).get("x1")
    #print("Piece ", piece_count, " x1 is ", (population[piece_count])["x1"]
    #print("Piece ", piece_count, " x1 is ", (population[piece_count])["x1"]
    #print(population[piece_count])["x1"]



    #print()


'''
This is the main GA loop, performing the evolutionary sequence of
operations: Evaluation, Selection, Crossover, Mutation.
Remember:
    A POPULATION is a set of POPULATION_SIZE individuals.
    An INDIVIDUAL is a set of PIECE_COUNT pieces.
'''

for looper in range(NUMBER_OF_GENERATIONS):
    for x in range(POPULATION_SIZE):
        for i in range(pieces[2]):
            mutating_individual = population[x]
            print()
            print("mutating indiv is ", mutating_individual)
            print()
            mutating_characteristic = mutating_individual[i]
            print(" mutating_characteristic is ", mutating_characteristic)
            print()
            
            '''
            Mutation is working by changingin the first individual of the first population with random coords
            
            The first if is setting the bondering between population. The first population will work differently than
            the other.
            
            Inside the first population, the first individual will mutate by random. The random value will be added to
            a list of lists. The first list inside the list contains the X1 values, the second, X2 values, the third.
            Y1 value, the forth, Y2 values. This is being made at the at of the first loop.

            After the first individuals of the first population. The mutations is made by a random choice inside the list
            for the specific coordinate. Still random but this random is made by choosing from previous values.

            For the other populations, it uses the same concept explained in the paragraph above.
            '''
            
            if population[0]:
                if mutating_individual[0]:
                    prev_value = mutating_characteristic.get("x1")
                    new_valuex1 = random.randint(0,random.randint(0,800))  # Random value
                    mutating_characteristic["x1"] = new_valuex1
                    
                    prev_value = mutating_characteristic.get("x2")
                    new_valuex2 = random.randint(0,random.randint(0,800))  # Random value
                    mutating_characteristic["x2"] = new_valuex2
                    
                    prev_value = mutating_characteristic.get("y1")
                    new_valuey1 = random.randint(0,random.randint(0,800))  # Random value
                    mutating_characteristic["y1"] = new_valuey1
                    
                    prev_value = mutating_characteristic.get("y2")
                    new_valuey2 = random.randint(0,random.randint(0,800))  # Random value
                    mutating_characteristic["y2"] = new_valuey2

                else:
                    prev_value = mutating_characteristic.get("x1")
                    new_valuex1 = random.choice(mutation_list_coords[0])  # Random choice from the list of X1 coords
                    mutating_characteristic["x1"] = new_valuex1
                    
                    prev_value = mutating_characteristic.get("x2")
                    new_valuex2 = random.choice(mutation_list_coords[1])  # Random choice from the list of X2 coords
                    mutating_characteristic["x2"] = new_valuex2
                
                    prev_value = mutating_characteristic.get("y1")
                    new_valuey1 = random.choice(mutation_list_coords[2])  # Random choice from the list of Y1 coords
                    mutating_characteristic["y1"] = new_valuey1
                
                    prev_value = mutating_characteristic.get("y2")
                    new_valuey2 = random.choice(mutation_list_coords[3])  # Random choice from the list of Y2 coords
                    mutating_characteristic["y2"] = new_valuey2
                        

            else:
                prev_value = mutating_characteristic.get("x1")
                new_valuex1 = random.choice(mutation_list_coords[0])  # Random choice from the list of X1 coords
                mutating_characteristic["x1"] = new_valuex1
                
                prev_value = mutating_characteristic.get("x2")
                new_valuex2 = random.choice(mutation_list_coords[1])  # Random choice from the list of X2 coords
                mutating_characteristic["x2"] = new_valuex2
                
                prev_value = mutating_characteristic.get("y1")
                new_valuey1 = random.choice(mutation_list_coords[2])  # Random choice from the list of Y1 coords
                mutating_characteristic["y1"] = new_valuey1
                
                prev_value = mutating_characteristic.get("y2")
                new_valuey2 = random.choice(mutation_list_coords[3])  # Random choice from the list of Y2 coords
                mutating_characteristic["y2"] = new_valuey2
                

            #Adding the values to the coords list used for the crossover mutation
            mutation_list_coords[0].append(new_valuex1)
            mutation_list_coords[1].append(new_valuex2)
            mutation_list_coords[2].append(new_valuey1)
            mutation_list_coords[3].append(new_valuey2)

            # Display all pieces in their new position.
            # In general, display the fittest individual of this generation.
            # In this demo, display only the first individual.
            # Clear the display by re-drawing the background with no elements
            canvas.create_rectangle(0, 0, pieces[0], pieces[1], fill='khaki')
            display_individual = population[x] # display this individual, which is a list of dictionary


        totalXOverlap = 0
        totalYOverlap = 0
        totalSquareOverlap = 0

        for piece_count in range(pieces[2]):
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

            for pieceToCompare in range(pieces[2]):

                yOverlap = 0
                xOverlap = 0

                if pieceToCompare != piece_count:
                    if display_individual[piece_count].get("x2") > display_individual[pieceToCompare].get("x1") and (display_individual[piece_count].get("x1") < display_individual[pieceToCompare].get("x1")):
                        xOverlap = abs(display_individual[piece_count].get("x2") - display_individual[pieceToCompare].get("x1"))
                        totalXOverlap = totalXOverlap + xOverlap
                        print("xOverlap for ", piece_count, "with", pieceToCompare, "is ", xOverlap)
                    elif display_individual[piece_count].get("x2") == display_individual[pieceToCompare].get("x2"):
                        xOverlap = 200
                        totalXOverlap = totalXOverlap + xOverlap
                        print("COMPLETE OVERLAP xOverlap for ", piece_count, "with", pieceToCompare, "is ", xOverlap)

                if pieceToCompare != piece_count:
                    if display_individual[piece_count].get("y2") > display_individual[pieceToCompare].get("y1") and (display_individual[piece_count].get("y1") < display_individual[pieceToCompare].get("y1")):
                        yOverlap = abs(display_individual[piece_count].get("y2") - display_individual[pieceToCompare].get("y1"))
                        totalYOverlap = totalYOverlap + yOverlap
                        print("yOverlap for ", piece_count, "with", pieceToCompare, "is ", yOverlap)
                    elif display_individual[piece_count].get("y2") == display_individual[pieceToCompare].get("y2"):
                        yOverlap = 200
                        totalYOverlap = totalYOverlap + yOverlap
                        print("COMPLETE OVERLAP yOverlap for ", piece_count, "with", pieceToCompare, "is ", yOverlap)

        totalSquareOverlap = totalXOverlap * totalYOverlap

        print("Total x overlap for individual: ", totalXOverlap)
        print("Total y overlap for individual: ", totalYOverlap)
        print("Total square overlap for individual: ", totalSquareOverlap)

        canvas.update()
        time.sleep(1) # HARDCODED TIME -- pause briefly between generations





mainloop()   # Graphics loop -- This statement follows all other statements
