from graph import Graph

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

starting_node = 6

def earliest_ancestor(ancestors, starting_node):
    # initialize and populate graph
    g = Graph()
    for a in ancestors:
        g.add_vertex(a[1])
    for a, c in ancestors:
        g.add_edge(c, a) # a, c: ancestor, child
    # use graph to find ancestors with recursive finction
    level_children_map = {} # dictionary  -- {level: set of nodes}
    level = 0               # initialize to level 0
    node = starting_node    # initialize to starting_node
    def go_deep(g, node, level):
        if level_children_map.get(level): # if the key already exists
            level_children_map[level].add(node) # append to key's set
        else: 
            level_children_map[level] = {node} # otherwise add the node
        children = g.get_neighbors(node)
        level += 1                          # increment level
        if children:                        # and recurse on children
            for child in children:
                go_deep(g, child, level)

    go_deep(g, node, level)
    print(level_children_map)
    deepest = max(level_children_map.keys()) # largest key = deepest level
    if deepest == 0:
        return -1
    return min(level_children_map[deepest]) # return smallest ancestor node

    


earliest_ancestor(ancestors, starting_node)
        

