#Date of last revision: 4/17/2017
#Authored by Love Bennett, Josh Burks, Greeta Joshi, Ayca Kucukdurmaz, Jacob Morgan,

import astar 

NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3

ourMap = astar.graph(10, 10)
ourMap.walls = [(0, 2),(1, 2),(2, 2),(3, 2), (4, 2), (5, 2)]
ourStart = (0, 0)
ourGoal = (3, 4)

finalNode = astar.aStarSearch(ourMap, ourStart, ourGoal)
pathway = astar.reconstructPath(finalNode, ourStart, ourGoal)

directions = []
facing = NORTH
forwardLength = 0

for i in range(len(pathway) - 1):
    (x1, y1) = pathway[i]
    (x2, y2) = pathway[i+1]

    if (x2 == x1+1):
        #go right
        if (facing == EAST):
            forwardLength += 1
            
        elif (facing == NORTH):
            directions.append("FWD " + str(forwardLength))
            directions.append("RGT")
            facing = EAST
            forwardLength = 1
            
        elif (facing == SOUTH):
            directions.append("FWD " + str(forwardLength))
            directions.append("LFT")
            forwardLength = 1
            facing = EAST

    elif (x2 == x1-1):
        #go left
        if (facing == WEST):
            forwardLength += 1
            
        elif (facing == NORTH):
            directions.append("FWD " + str(forwardLength))
            directions.append("LFT")
            forwardLength = 1
            facing = WEST
            
        elif (facing == SOUTH):
            directions.append("FWD " + str(forwardLength))
            directions.append("RGT")
            forwardLength = 1
            facing = WEST
        
    elif (y2 == y1+1):
        #forward
        if (facing == NORTH):
            forwardLength += 1
            
        elif (facing == EAST):
            directions.append("FWD "  + str(forwardLength))
            directions.append("LFT")
            forwardLength = 1
            facing = NORTH
            
        elif (facing == WEST):
            directions.append("FWD " + str(forwardLength))
            directions.append("RGT")
            forwardLength = 1
            facing = NORTH

    elif (y2 == y1-1):
        #backward
        if (facing == SOUTH):
            forwardLength += 1
            
        elif (facing == EAST):
            directions.append("FWD "  + str(forwardLength))
            directions.append("RGT")
            forwardLength = 1
            facing = SOUTH
            
        elif (facing == WEST):
            directions.append("FWD " + str(forwardLength))
            directions.append("LFT")
            forwardLength = 1
            facing = SOUTH
            
directions.append("FWD " + str(forwardLength))

print(pathway)
for d in directions:
    print(d)
