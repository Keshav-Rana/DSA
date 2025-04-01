from collections import deque

class Graph:
    def __init__(self, rows, cols, edges, isDirected=False, isWeighted=False):
        self.rows = cols # represent the number of nodes
        self.cols = rows
        self.edges = edges
        self.adjList = {} # dict or hashmap
        self.adjMatrix = [[]] # 2d matrix n * n
        self.isDirected = isDirected
        self.isWeighted = isWeighted

    def createAdjListGraph(self):
        if not self.isDirected:
            if not self.isWeighted:
                # initialise the adjacency list
                for i in range(0, self.rows+1):
                    self.adjList[i] = []

                # populate the adj list
                for edge in self.edges:
                    self.adjList[edge[0]].append(edge[1])
                    self.adjList[edge[1]].append(edge[0])

    def createAdjMatrixGraph(self):
        # initialise matrix
        for i in range(self.rows+1):
            # [0] creates a list of 0s and we multiply it by the number of columns
            self.adjMatrix.append([0] * (self.cols+1))

        if not self.isDirected:
            if not self.isWeighted:
                # populate matrix
                for edge in self.edges:
                    self.adjMatrix[edge[0]][edge[1]] = 1
                    self.adjMatrix[edge[1]][edge[0]] = 1

    def BFSOnList(self, startNode):
        # initialise a visited array
        visited = [False] * (self.rows+1) # size == num of nodes == rows
        q = deque()

        q.append(startNode)
        visited[startNode] = True

        while q:
            frontElem = q.popleft()
            print(frontElem, end = ' ')
            for adjElement in self.adjList[frontElem]:
                if not visited[adjElement]:
                    q.append(adjElement)
                    visited[adjElement] = True

    def DFSOnList(self, startNode, visited, result):
        # mark the node as visited
        visited[startNode] = True
        result.append(startNode)

        for adjElement in self.adjList[startNode]:
            # skip the visited elements
            if not visited[adjElement]:
                # call the DFS method recursively
                self.DFSOnList(adjElement, visited, result)

if __name__ == '__main__':
    pass
    # test out graph and it's methods here
    edges = [(1, 2), (1, 5), (2, 4), (2, 3), (5, 6)]
    g = Graph(7, 7, edges)

    g.createAdjListGraph()
    g.createAdjMatrixGraph()

    print(g.adjList)
    print('\n')

    g.BFSOnList(1)
    print('\n')

    visited = [False] * 7
    result = []
    g.DFSOnList(1, visited, result)
    print(result)