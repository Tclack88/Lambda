islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


visited = {}
island_count = 0
width = len(islands[0])
height = len(islands)

def find_neighbors(islands, visited, i, j):
    if (j,i) not in visited:
        visited.add((j,i))
        if islands[j][i] == 1:
            if j < width:
                j += 1
                find_neighbors(islands, visited, i, j)
            if i < height:
                i += 1
                find_neighbors(islands, visited, i, j)


def count_islands(islands):
    for j in range(height):
        for i in range(width):
            position = islands[j][i]
            if position == 1:
                island_count += 1
                find_neighbors(islands, visited, i, j)


count_islands(islands)
print(island_count)
