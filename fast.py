def gen_matrix(n: int) -> list:
    first_row = [0.0] + [1.0] * n + [0.0]
    result = [first_row]
    for i in range(n+1):
        result.append([0.0] * (n + 2))
    return result


def update_row(matrix, row, n, p):
    for col in range(1, n+1):
        matrix[row][col] = p * (1 - (1 - matrix[row + 1][col]) *
                                    (1 - matrix[row - 1][col]) *
                                    (1 - matrix[row][col + 1]) *
                                    (1 - matrix[row][col - 1]))


def print_matrix(matrix):
    for row in matrix:
        print(''.join(f"{item:8.3}" for item in row))
    print("")


def get_prob_fast(p: float, n: int = 1) -> float:
    num_iter = 100
    matrix = gen_matrix(n)

    # print_matrix(matrix)

    for iteration in range(num_iter):
        for row in range(1, n+1):
            update_row(matrix, row, n, p)
            # print_matrix(matrix)
    result_row = matrix[n][1:-1]
    negative_result = 1
    for item in result_row:
        negative_result *= (1-item)
    return 1 - negative_result


for size in range(1, 5):
    print(get_prob_fast(0.5, size))
