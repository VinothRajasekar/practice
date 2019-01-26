QUEEN = 'q'
NO_QUEEN = '-'

def find_all_arrangements(n):
    output = []

    # n columns for n rows
    col_occupied = [False] * n

    # for n * n board there are 2*n - 1 diagonals (slash and back slash diagonals)
    slash_diag_occupied = [False] * (2*n-1)
    back_slash_diag_occupied = [False] * (2*n-1)

    # by using auxilary space for col occupied and diags occupied and updating then accordingly this function will run in O(1)
    def is_safe(row, col):
        return not (col_occupied[col] or slash_diag_occupied[row+col] or back_slash_diag_occupied[row-col+n-1])

    def _generate_n_queens(curr_arrangement, row):
        if row == n:
            # make deep copy and append to output
            output.append([''.join(x) for x in curr_arrangement])
            return

        for col in range(0, n):
            if is_safe(row, col):
                # mark this col and both diagonals as being occupied
                curr_arrangement[row][col] = QUEEN
                print(row,col)
                col_occupied[col] = True
                slash_diag_occupied[row+col] = True
                back_slash_diag_occupied[row-col+n-1] = True
                print(col_occupied)
                print(slash_diag_occupied)
                print(back_slash_diag_occupied)

                # try to place queen in the next row
                _generate_n_queens(curr_arrangement, row+1)

                # set back as not occupied
                curr_arrangement[row][col] = NO_QUEEN
                col_occupied[col] = False
                slash_diag_occupied[row+col] = False
                back_slash_diag_occupied[row-col+n-1] = False

    # start recursive function with empty current arrangement and 0 row
    curr_board = [[NO_QUEEN] * n for _ in range(n)]
    _generate_n_queens(curr_board, 0)
    return output

n=4
print(find_all_arrangements(n))
