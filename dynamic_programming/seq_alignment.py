from utils import readFile

def calcMinTotalPenalty(X, Y, a_gap, a_mm):
    """
    Create an (m+1) x (n+1) matrix
    """
    m = len(X)
    n = len(Y)

    P = [[None for _ in range(n+1)] for _ in range(m+1)]

    # Base case when i = 0
    for c in range(n+1):
        P[0][c] = a_gap*c

    # Base case when j = 0
    for r in range(m+1):
        P[r][0] = a_gap*r

    for r in P:
        print(f"{r}")

    for i in range(1,m+1):
        for j in range(1,n+1):
            mm_pen = a_mm if X[i-1] != Y[j-1] else 0
            P[i][j] = min(P[i-1][j-1] + mm_pen,  
                          P[i-1][j] + a_gap,
                          P[i][j-1] + a_gap)
    for r in P:
        print(f"{r}")

    return P[m][n]

def main():
    X = "intention"
    Y = "execution"
    alpha_gap = 1
    alpha_mm = 2

    minTotalPenalty = calcMinTotalPenalty(X,Y, alpha_gap, alpha_mm)
    print(f"The minimum total penalty between {X} and {Y} is: {minTotalPenalty}")

if __name__=='__main__':
    main()
