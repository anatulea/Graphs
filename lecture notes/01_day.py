# Singly Linked List
class ListNode:
    def __init__(self, value):
        self.value = value

        self.next = None 

       # self.prev if DLL

## LL Traversal
current = node
while current is not None:
    current = current.next

class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value

        self.left = None
        self.right = None
        
# BST Traversal
## DFT, BFT
### Stack, Queue

while node is not None:
    recurse(self.left)
    recurse(self.right)

class GraphNode:
    def __init__(self, value):
        self.value = 'B'

        # options: dictionary, array, set
        # B's connections
        self.connections = set('a', 'c', 'd')

        # A's connections
        self.connections = set('B')

        # D's connections - Billy no mates
        self.connections = set()

     
# outbound vs inbound connections?

# Graph terminology for 2-way vs 1-way connections
## undirected graph vs directed graph
## (FB, LinkedIn) vs (Instagram, Twitter, TikTok)

## Graph Traversals

## DFT, stack
### Check every node once, check every connection once

# make a stack
stack = Stack(3, 6, 8, 9)
# make a set to track visited
visited = set(1, 2, 4)

# put the start node into the stack

# while the stack isn't empty

## pop off the top of the stack, this is our current node
current_node = 7

## check if we have visited this node yet
### if not, add it our visited set
### and add each of its neighbors to our stack

## Time complexity?
### How many times did we visit each node? once
### How many times did we check each connection? once

## O(number of nodes + number of connections)
### O(n + m)
## so linear!

# BFT, queue
#        --->>>>>
q = Queue()

# make a set to track visited
visited = set('A', "B", "C", "D", 'E', "F", "G")

# enqueue the start node

# while our queue isn't empty

## dequeue from front of line, this is our current node
current_node = "A"

## check if we've visited here yet
### if not, add to visited
### get its neighbors, for each, add to queue
neighbors = set("A", "F")

# Time complexity?
## visit every vertex once, visit every edge once
## O(n + m)
## O(node + edge)


# DFT vs. BFT
## same time complexity, each just as fast
## DFT can be done recursively
## BFT can find shortest path





"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        pass  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        pass  # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
​
        # make a set to track which nodes we have visited
        visited = set()
​
        # enqueue the starting node
        q.enqueue(starting_vertex)
​
        # loop while the queue isn't empty
        while q.size() > 0:
            # dequeue, this is our current node
            current_node = q.dequeue()
​
            # check if we've yet visited
            if current_node not in visited:
                print(current_node)
            ## if not, we go to the node
            ### mark as visited == add to visited set
                visited.add(current_node)
​
            ### get the neighbors
                neighbors = self.get_neighbors()
            ### iterate over the neighbors, enqueue them
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        pass  # TODO

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
​
        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        Enqueue a PATH TO the starting node, instead of just the starting node
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))