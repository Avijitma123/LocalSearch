import search
#I have a 8-queens problem and I want to use hill climbing algorithm to solve it.
state = (1, 2, 3, 4, 5, 6, 7, 0)
N =len(state)

#display the  state in matrix form
def display(state,s):
    mat = [[0 for i in range(N)] for j in range(N)]
    for i in range(0, N):
        mat[state[i]][i] = "Q"
    print(s)
    for i in range(0, N):
        print(mat[i])
        print()


p1 = search.Problem(state)
display(p1.initial,"Initial State:")
display(search.hill_climbing(p1),"Final State:")



