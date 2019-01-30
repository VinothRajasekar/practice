from collections import deque

DIRECTIONS = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):

    def get_neighbors(lcoation):
        neighbors =[]
        for i, j in DIRECTIONS:
            new_r, new_c = location[0] + i , location[1] + j
            if 0 <= new_r < rows and 0 <= new_c < cols:
                neighbors.append((new_r, new_c))

        return neighbors

    start_cell = start_row, start_col

    visited = {start_row, start_col}

    q = deque([((start_row,start_col), 0)])

    while q:
        location, count = q.popleft()
        if location == (end_row,end_col):
            return count

        for n in get_neighbors(location):
            if n not in visited:
                visited.add(n)
                q.append((n, count + 1))
    return -1











rows = 5
cols = 5
start_row = 0
start_col = 0
end_row = 4
end_col = 4

print(find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col))
