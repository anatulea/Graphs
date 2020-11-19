"""
Simple graph implementation 
"""
from util import Stack, Queue  # These may come in handy
from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
       
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            nv = self.add_vertex(v1)
        if v2 not in self.vertices:
            nv = self.add_vertex(v2)
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        #  --- Using QUEUE -----
        visited = set()
        queue = Queue()
        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            vertex = queue.dequeue()
            # print(vertex)
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    queue.enqueue(neighbor)
        # return visited

        # ------- Using DEQUE -----

        # visited = set()
        # queue = deque()
        # queue.append(starting_vertex)
        # while len(queue) > 0:
        #     currNode = queue.popleft()
        #     if currNode not in visited:
        #         visited.add(currNode)
        #         # print(currNode)
        #         for neighbor in self.get_neighbors(currNode):
        #             queue.append(neighbor)
        # return visited


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #  --- Using STACk -----
        # visited = []
        visited = set()
        stack = Stack()
        stack.push(starting_vertex)

        while stack.size() > 0:
            vertex = stack.pop()
            # print(vertex)
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    # print(neighbor)
                    stack.push(neighbor)
        # return visited

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = {}
        # init visited hashtable to false for all verts
        for i in self.vertices:
            visited[i] = False

        def recurse(vert_id, visited):
            # traversal operation
            print(vert_id)
            # mark as visited
            visited[vert_id] = True

            # base case = everything has been visited already
            if False not in visited.values():
                return
            else:
                for neighbor in self.get_neighbors(vert_id):
                    # only recurse for unvisited verts
                    if visited[neighbor] == False:
                        recurse(neighbor, visited)

        # initial recursive call
        recurse(starting_vertex, visited)  


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
         # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
		# Create a Set to store visited vertices
        visited = set()
		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first PATH
            path = q.dequeue()
			# Grab the last vertex from the PATH
            lastvertex = path[-1]
			# If that vertex has not been visited...
            if lastvertex not in visited:
				# CHECK IF IT'S THE TARGET
                if lastvertex == destination_vertex:
				  # IF SO, RETURN PATH
                  return path
				# Mark it as visited...
                visited.add(lastvertex)
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(lastvertex):
				  # COPY THE PATH
                  copied_path = [*path]
				  # APPEND THE NEIGHOR TO THE BACK
                  copied_path.append(neighbor)
                  # Add list back inside queue
                  q.enqueue(copied_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            path = s.pop()
            lastvertex = path[-1]

            if lastvertex not in visited:
                if lastvertex == destination_vertex:
                    return path

                visited.add(lastvertex)

                for neighbor in self.get_neighbors(lastvertex):
                    copied_path = [*path]
                    copied_path.append(neighbor)
                    s.push(copied_path)

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
    print(graph.get_neighbors(4))
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
    print(graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(graph.dft(1))
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
