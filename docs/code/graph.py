#Defines aspects of the map such as its size and any obstacles.

class graph:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.weights = {}

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse()
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

#Creates a visual representation of the map used by the GoPiGo.

def drawGraph(graph, start, goal, path):
	for j in range(graph.height):
		for i in range(graph.width):
			if (i, graph.height - j - 1) == start:
				print('S', end = "")

			elif (i, graph.height - j - 1) == goal:
				print('G', end = "")

			elif (i, graph.height - j - 1) in path:
				print('p', end = "")

			elif (i, graph.height - j - 1) in graph.walls:
				print('#', end = "")

			else:
				print(".", end = "")

		print()
