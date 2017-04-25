import constants
import graph
import astar

def translate(pathway, startingDirection=constants.NORTH):
    directions = []
    facing = startingDirection
    forwardLength = 0

    for i in range(len(pathway) - 1):
        (x1, y1) = pathway[i]
        (x2, y2) = pathway[i+1]

        if (x2 == x1+1):
            #go right
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
            #go left
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
            #forward
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
            #backward
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