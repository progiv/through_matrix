import numpy as np
from simple_and_correct import passable, bisect_f
from itertools import product

def gen_matrix(n: int, p:float) -> list:
    return np.random.binomial(1, p, (n, n))


def get_prob_fast(p: float, n: int = 1) -> float:
    num_iter = 100
    result_arr = []
    for i in range(num_iter):
        result_arr.append(passable(gen_matrix(n, p)))
    return np.mean(result_arr)


for i in range(1, 6):
    print(i, bisect_f(partial(get_prob_fast, n=i)))
