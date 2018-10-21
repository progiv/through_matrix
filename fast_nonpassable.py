def gen_matrix(n:int) -> list:
    first_row = [1.0] + [0.0] * n + [1.0]
    result = [first_row]
    for i in range(n+1):
        result.append([1.0] * (n + 2))
    return result


def update_row(matrix, row, n, p):
    for col in range(1, n+1):
        matrix[row][col] = 1 - (1- (1 - p)) * (1 - (matrix[row + 1][col] *
                                      matrix[row - 1][col] *
                                      matrix[row][col + 1] *
                                      matrix[row][col - 1]))


def print_matrix(matrix):
    for row in matrix:
        print(''.join(f"{item:8.3}" for item in row))
    print("")


def get_prob_fast(p: float, n:int = 1) -> float:
    num_iter = 100
    matrix = gen_matrix(n)

    print_matrix(matrix)

    for iter in range(num_iter):
        for row in range(1, n+1):
            update_row(matrix, row, n, p)
            #print_matrix(matrix)

    return n - sum(matrix[n][1:-1])

for n in range(1, 3):
    print(get_prob_fast(0.9, n))