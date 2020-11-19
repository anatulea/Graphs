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
        if v1 not in self.vertices:  # if vertex 1 (v1) does not exist
            nv = self.add_vertex(v1)  # we create it
        if v2 not in self.vertices:  # if vertex 2 (v2) does not exist
            nv = self.add_vertex(v2)  # we create it
        self.vertices[v1].add(v2)  # we add v2 as an edge to v1

        '''
        if v1 in self.vertices and v2 in self.vertices: # if v1 and v2 exist in the graph
            self.vertices[v1].add(v2) # we add v2 as an edge to v1
        else: # if v1 and v2 do not exist in the graph
            #r raise error
            raise IndexError("All your vertices are mine, or rather, do not exist.")
        '''

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
        return visited

        '''
        # ------- Using DEQUE -----

        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                # print(currNode)
                for neighbor in self.get_neighbors(currNode):
                    queue.append(neighbor)
        return visited

        '''

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
        return visited

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
            # print(vert_id)
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

     # second option of recursive dft

    def dft_recursive2(self, vertex, visited=set()):
        if vertex not in visited:
            visited.add(vertex)

            neighbors = self.get_neighbors(vertex)
            if len(neighbors) == 0:
                return
            else:
                for neighbor in neighbors:
                    self.dft_recursive2(neighbor, visited)

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
        # loop while the queue is not empty
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            lastvertex = path[-1]
            # CHECK IF IT'S THE TARGET
            if lastvertex == destination_vertex:
                # IF SO, RETURN PATH
                return path

            # If that vertex has not been visited
            if lastvertex not in visited:
                # Mark it as visited
                visited.add(lastvertex)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(lastvertex):
                    # COPY THE PATH
                    copied_path = [*path]
                    # APPEND THE NEIGHBOR TO THE BACK
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

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if len(path) == 0:
            path.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return path

        if starting_vertex not in visited:
            visited.add(starting_vertex)

            neighbors = self.get_neighbors(starting_vertex)
            for neighbor in neighbors:
                path_copy = path + [neighbor]

                result = self.dfs_recursive(
                    neighbor, destination_vertex, path_copy, visited)
                if result is not None:
                    return result


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
    print(f'graph.vertices: {graph.vertices}')
    print(f'graph.get_neighbors(4): {graph.get_neighbors(4)}')
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
    print(f'graph.bft(1): {graph.bft(1)}')

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(f'graph.dft(1): {graph.dft(1)}')
    print(f'graph.dft_recursive2(1): {graph.dft_recursive2(1)}')

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(f'graph.bfs(1, 6): {graph.bfs(1, 6)}')

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(f'graph.dfs(1, 6): {graph.dfs(1, 6)}')
    print(f'graph.dfs_recursive(1, 6): {graph.dfs_recursive(1, 6)}')
