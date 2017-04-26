import astar
import constants
import graph

'''
Takes the graph and astar algorithim and determines the
directions to follow. These directions are passed to the
main to be translated into GoPiGo commands.
'''

def translate(pathway, startingDirection = constants.NORTH):
    directions = []
    facing = startingDirection
    forwardLength = 0

    for i in range(len(pathway) - 1):
        (x1, y1) = pathway[i]
        (x2, y2) = pathway[i+1]

        if (x2 == x1+1):
            #Right turn logic.
            if (facing == constants.EAST):
                forwardLength += 1
                
            elif (facing == constants.NORTH):
                directions.append("FWD " + str(forwardLength))
                directions.append("RGT")
                facing = constants.EAST
                forwardLength = 1
                
            elif (facing == constants.SOUTH):
                directions.append("FWD " + str(forwardLength))
                directions.append("LFT")
                forwardLength = 1
                facing = constants.EAST

        elif (x2 == x1-1):
            #Left turn logic.
            if (facing == constants.WEST):
                forwardLength += 1
                
            elif (facing == constants.NORTH):
                directions.append("FWD " + str(forwardLength))
                directions.append("LFT")
                forwardLength = 1
                facing = constants.WEST
                
            elif (facing == constants.SOUTH):
                directions.append("FWD " + str(forwardLength))
                directions.append("RGT")
                forwardLength = 1
                facing = constants.WEST
            
        elif (y2 == y1+1):
            #Forward logic.
            if (facing == constants.NORTH):
                forwardLength += 1
                
            elif (facing == constants.EAST):
                directions.append("FWD "  + str(forwardLength))
                directions.append("LFT")
                forwardLength = 1
                facing = constants.NORTH
                
            elif (facing == constants.WEST):
                directions.append("FWD " + str(forwardLength))
                directions.append("RGT")
                forwardLength = 1
                facing = constants.NORTH

        elif (y2 == y1-1):
            #Backward logic. Note this should never happen(?)
            if (facing == constants.SOUTH):
                forwardLength += 1
                
            elif (facing == constants.EAST):
                directions.append("FWD "  + str(forwardLength))
                directions.append("RGT")
                forwardLength = 1
                facing = constants.SOUTH
                
            elif (facing == constants.WEST):
                directions.append("FWD " + str(forwardLength))
                directions.append("LFT")
                forwardLength = 1
                facing = constants.SOUTH
                
    directions.append("FWD " + str(forwardLength))

    return directions;
