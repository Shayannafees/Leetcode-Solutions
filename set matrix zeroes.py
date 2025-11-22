arr = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]
def findRowCol(arr):
    zero_rows = set()
    zero_cols = set()
    for row_index, row in enumerate(arr):
        for col_index, value in enumerate(row):
            if arr[row_index][col_index] == 0: # type: ignore
                zero_rows.add(row_index)
                zero_cols.add(col_index)

    return zero_rows, zero_cols


def setZeroes(zero_rows, zero_cols):
    #now get row and col from prev function and set those to zeroes
    for row_index in range(len(arr)):
        if row_index in zero_rows:
            for col_index in range(len(arr[0])):
                arr[row_index][col_index] = 0

            
    for col_index in range(len(arr[0])):
        if col_index in zero_cols:
            for row_index in range(len(arr)):
                arr[row_index][col_index] = 0

    print(arr)

a, b = findRowCol(arr)

setZeroes(a, b) # type: ignore







