# write a getNeighbors function
# iterate over the pairs of nodes
# find those that are direct parents of this node
​
# run a standard DFT, but recurse with distance to track the earliest ancestor found
def dft(ancestors, node, distance)
​
    parents = getNeighbors(node)
​
    if len(parents) == 0:
        return (node, distance)
​
    ancient_one = (node, distance)
    for parent in parents:
        node_pair = dft(ancestors, parent, distance + 1)
​
        if node_pair[1] > distance:
            ancient_one = node_pair
		if node_pair[1] == ancient_one[1] and node_pair[0] < ancient_one[0]:
			ancient_one = node_pair
​
    return ancient_one
​
def earliest_ancestor(ancestors, starting_node):
    # call BFT or DFT
    ancient_one = dft(ancestors, starting_node, 0)
​
    # if the earliest ancestor returned is the same as the starting node, return -1