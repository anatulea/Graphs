''' BFS - use queue'''
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    
    q = Queue()
    # add first vertex to path list
    path = [starting_node]
    q.enqueue(path)
    # print(f'path: {path}')
    # loop while we have vertices in the q
    while q.size() > 0:
        
        current_path = q.dequeue()
        new_path = []
        changed = False
        # print( f'current_path: {current_path}')
        # get begin vertexId/vertex of path        
        for vertexId in current_path:
            # loop through ancestors for parents            
            for ancestor in ancestors:
                # look into each ancestor parent 
                # with start_node as child
                # parent is 0, child is 1
                # flip the arrows up
                if ancestor[1] == vertexId: 
                    new_path.append(ancestor[0])
                    changed = True
                    q.enqueue(new_path)

        # loop through final path for largest value
        if changed is False:
            # If the input individual has no parents, 
            # the function should return -1
            if current_path[0] == starting_node:
                return -1
            else:
                return min(current_path)
