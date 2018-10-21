# The problem
There is a NxN matrix. Each cell of matrix can be blocked or opened. At the beginning each cell is blocked and each field is independently set to be opened with a probability of p.

The NxN matrix is passable if there is a route through the open fields from the top row to the bottom one via chain of neighboring open fields (up, down, left, right [diagonal step on the matrix is not allowed]).

Task: Find p probability where 10000x10000 matrix is passable with ½ probability. There are different ways to get out of a labyrinth, this one is tough because you have to find the best algorithm, otherwise you will need to compute for 100 years. If you prefer bruteforce, we’d like to inform you that we think of solutions that require several hundreds of years to crack for a super computer.
# Solution approach
## 1x1 and 2x2 manual
For small sizes we can calculate probabilities easilly by hands. This approach is not scalable
## Slow and simple
The bruteforce [slow solution](simple_and_correct.py) was written to test others. For each matrix it uses Brad First Search to test if it is passable. And get the answer it uses bisect on answer algorithm. For now it works only with 5x5 matrices. This solution is not scalable beacause it has exponential complexity.
## Fast and incorrect
I [tried](fast.py) use dinamical programming approach to solve this problem, but the dependencies between random events are too complicated, so this one gives wrong answer.