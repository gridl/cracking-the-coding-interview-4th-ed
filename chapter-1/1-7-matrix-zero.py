# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0

# What is the minimum m and n?
#   1 and 1
# What object is stored in the matrices?
#   Integer
# Is there a time complexity limit?
#   Yes
# Is there a space complexity limit?
#   No

def matrix_zero(mat):
    m = len(mat)
    n = len(mat[0])

    done_cols = set()
    done_rows = set()

    for i in range(m):
        print(mat)

        if i in done_cols:
            continue

        for j in range(n):

            if j in done_rows:
                continue

            if mat[i][j] == 0:

                done_cols.add(i)
                done_rows.add(j)
                print(i, j)

                for xi in range(m):
                    mat[xi][j] = 0

                for xj in range(n):
                    mat[i][xj] = 0

    return mat

if __name__ == "__main__":
    m1 = [[1,2,3,4],[5,6,0,8],[9,10,11,12],[13,14,15,16]]
    print(m1)
    print(matrix_zero(m1))

