#Date of last revision: 4/17/2017
#Authored by Love Bennett, Josh Burks, Greeta Joshi, Ayca Kucukdurmaz, Jacob Morgan,

import constants
import graph
import astar
import translator

ourMap = graph.graph(10, 10)
ourMap.walls = [(0, 2),(1, 2),(2, 2),(3, 2), (4, 2), (5, 2)]
ourStart = (0, 0)
ourGoal = (3, 4)

pathway = astar.aStarSearch(ourMap, ourStart, ourGoal) 

directions = translator.translate(pathway)

print("our example graph: ")

graph.drawGraph(ourMap, ourStart, ourGoal, pathway)
print()

print("Start node: %s" % str(ourStart))
print("Goal node: %s" % str(ourGoal))
print("A* Results: %s" % str(pathway))
print()

print("Translated directions to get from start node to goal node:")
for d in directions:
    print(d)
