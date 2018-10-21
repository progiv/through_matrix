from collections import deque
from itertools import product
from functools import partial
import numpy as np


dxdy = ((0, 1), (-1, 0), (0, -1), (1, 0))


def passable(a: tuple) -> bool:
    """
    We always have matrix a: NxN
    :param a: Matrix of block each one is passable or not
    :return: True if matrix is passable
    """
    n = len(a)
    visited = [[False] * n for _ in range(n)]

    queue = deque()
    for j in range(n):
        if a[0][j] and not visited[0][j]:
            queue.append((0, j))
            while queue:
                ii, jj = queue.popleft()
                visited[ii][jj] = True
                for di, dj in dxdy:
                    ii_next = ii + di
                    if ii_next == n:
                        return True
                    jj_next = jj + dj
                    if 0 <= ii_next and 0 <= jj_next < n and a[ii_next][jj_next] and not visited[ii_next][jj_next]:
                        queue.append((ii_next, jj_next))
    return False


def get_probability(sequence: tuple, p: float) -> float:
    """
    :param sequence: sequance ot True or False values meaning if a cell is passable
    :param p: probability to cell to be open (True value)
    :return: probability of this sequence to occure
    """
    prob = 1
    for item in sequence:
        prob *= p if item else (1 - p)
    return prob


def make_matrix(sequence: tuple, n: int) -> tuple:
    return np.array(sequence).reshape((n, n))
    # return tuple(sequence[index * n: (index + 1) * n] for index in range(n))


def get_prob_simple(p: float, n: int = 1) -> float:
    """
    :param p: probability of cell to become open
    :param n: matrix (n x n) size
    :return: probability of graph to be passable
    """
    result: float = 0.0
    for sequence in product((0, 1), repeat=n * n):
        result += get_probability(sequence, p) if passable(make_matrix(sequence, n)) else 0
    return result


def bisect_f(func, value=0.5, left=0.0, right=1.0, eps=1e-9):
    le = left
    ri = right
    while abs(ri - le) > eps:
        m = (ri + le) / 2
        if func(m) < value:
            le = m
        else:
            ri = m
    return le


for i in range(1, 6):
    print(i, bisect_f(partial(get_prob_simple, n=i)))
