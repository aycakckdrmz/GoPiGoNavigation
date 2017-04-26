#Date of last revision: 4/26/2017
#Authored by Love Bennett, Josh Burks, Greeta Joshi, Ayca Kucukdurmaz, Jacob Morgan,

from gopigo import *
import astar
import constants
import graph
import sys
import translator

#Establish starting position, goal position, and locations of obstacles.

ourMap = graph.graph(80, 80)
ourMap.walls = [(0,18),(1,18),(2,18),(3,18),(4,18),(5,18),(6,18),(7,18),
                (8,18),(9,18),(10,18),(11,18),(12,18),(13,18),(14,18),
                (15,18),(16,18),(17,18),(18,18)]
ourStart = (0, 0)
ourGoal = (3, 75)

'''
Perform astar to derive shortest path, then translate directions into
GoPiGo instructions.
'''

pathway = astar.aStarSearch(ourMap, ourStart, ourGoal) 

directions = translator.translate(pathway)

#Prints visual representation of our map and labels important points.

print("our example graph: ")
graph.drawGraph(ourMap, ourStart, ourGoal, pathway)
print()

print("Start node: %s" % str(ourStart))
print("Goal node: %s" % str(ourGoal))
print("A* Results: %s" % str(pathway))
print()

#Prints directions in the form of directions, then executes GoPiGo instructions.

print("Translated directions to get from start node to goal node:")
for d in directions:
    print(d)

for d in directions:
    enable_encoders()
    instruction = d[:3]
    if (instruction == 'FWD'):
        units = d[4]
        enc_tgt(1, 1, int(units)*18)
        fwd()
        time.sleep(3)
    elif (instruction == 'RGT'):
        right()
        time.sleep(.5)
    elif (instruction == 'LFT'):
        left()
        time.sleep(.5)
    else:
        stop()
        sys.exit()
