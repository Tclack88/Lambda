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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if all([v1,v2]) in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("can't")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else: 
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            vertex = q.dequeue()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            vertex = s.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    s.push(neighbor)
                     

    def dft_recursive(self, starting_vertex, visited = []):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex in visited:
            return # Don't continue to recurse if the vertex already exists
        print(starting_vertex)
        visited.append(starting_vertex)
        # recurse on neighbors, passing in higher "visited" list
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # perform Breadth first traversal again, but keep track of each
        # neighbor's "parent node" as it pertains to the breadth traversal
        visited = set()
        parent = {}
        q = Queue()
        q.enqueue(starting_vertex)
        while q.size() > 0:
            vertex = q.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    q.enqueue(neighbor)
                    parent[neighbor] = vertex
                    if neighbor == destination_vertex:
                        break # end the BFT early
        # with the tracked parent hash table, we can move backwards 
        # from destination vertex -> starting vertex
        reversed_traversal = []
        prev_vertex = destination_vertex
        while prev_vertex != starting_vertex:
            reversed_traversal.append(prev_vertex)
            prev_vertex = parent[prev_vertex]
        
        forward_path = [starting_vertex] + reversed_traversal[::-1]
        return forward_path
        #def flatten(lst):
        #    outlist = sum( ([x] if not isinstance(x, list) else flatten(x) for x in lst), [] )
        #    return outlist
        #print('\nbreadth first search')
        #search_list = []
        #search_list.append([starting_vertex])
        #last = search_list[-1]
        #print(last)
        #i = 0
        #while destination_vertex not in last:
        #    print('in loop')
        #    search_list.append([list(self.get_neighbors(v)) for v in flatten(last)])
        #    last = search_list[-1]
        #    i += 1
        #    if i > 5:
        #        break

    
        #    print(search_list)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # as with BFS, perform a DFT keeping track of "parent nodes"
        visited = set()
        parent = {}
        print('dfs')
        s = Stack()
        s.push(starting_vertex)
        while s.size() > 0 :
            vertex = s.pop()
            if vertex not in visited:
                visited.add(vertex)
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    s.push(neighbor)
                    parent[neighbor] = vertex
                    if neighbor == destination_vertex:
                        break # break early from DFT
        # with parent dictionary known, trace backwards
        # from destination vertex -> starting vertex
        reversed_traversal = []
        prev_vertex = destination_vertex
        while prev_vertex != starting_vertex:
            reversed_traversal.append(prev_vertex)
            prev_vertex = parent[prev_vertex]
        
        forward_path = [starting_vertex] + reversed_traversal[::-1]
        return forward_path
        

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=[], path = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited and visited[-1] == destination_vertex:
            path.append(destination_vertex)
            return path
        if starting_vertex in visited:
            return path
        path.append(starting_vertex)
        print(starting_vertex)
        visited.append(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)
        if not neighbors:
            path.pop(-1)
            return path
        for neighbor in neighbors:
            self.dfs_recursive(neighbor, destination_vertex, visited)
        return path


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
