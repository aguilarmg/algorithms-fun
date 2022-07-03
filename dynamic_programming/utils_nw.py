class Alignment():
    def __init__(self, X, Y, a_gap, a_mm):
        self.m = len(X)
        self.n = len(Y)
        self.X = X
        self.Y = Y
        self.a_gap = a_gap
        self.a_mm = a_mm
        self.nwGrid = [[None for c in range(self.n+1)] for r in range(self.m+1)]
        self.aX = ""
        self.aY = ""

    def fillGrid(self):
        """
        Base case when i=0
        """
        for c in range(self.n+1):
            self.nwGrid[0][c] = c*self.a_gap

        """
        Base case when j=0
        """
        for r in range(self.m+1):
            self.nwGrid[r][0] = r*self.a_gap


        """
        Fill Grid
        """
        for i in range(1,self.m+1):
            for j in range(1,self.n+1):
                mismatch_cost = 0 if self.X[i-1] == self.Y[j-1] else self.a_mm
                self.nwGrid[i][j] = min(self.nwGrid[i-1][j-1] + mismatch_cost,
                                        self.nwGrid[i-1][j] + self.a_gap,
                                        self.nwGrid[i][j-1] + self.a_gap)
    
    def getNWScore(self, m, n):
        return self.nwGrid[m][n]

    def constructAlignment(self) -> tuple[str,str]:
        i = self.m
        j = self.n

        while i >= 1 and j >= 1:
            mismatch_cost = 0 if self.X[i-1] == self.Y[j-1] else self.a_mm
            if self.nwGrid[i][j] == self.nwGrid[i-1][j-1] + mismatch_cost:
                self.aX += self.X[i-1]
                self.aY += self.Y[j-1]
                i -= 1
                j -= 1
            elif self.nwGrid[i][j] == self.nwGrid[i-1][j] + self.a_gap:
                self.aX += self.X[i-1]
                self.aY += "-"
                i -= 1
            else:
                self.aX += "-"
                self.aY += self.Y[j-1]
                j -=1
        print(f"Final i and j values: i={i}, j={j}")

        self.aX = self.aX[::-1]
        self.aY = self.aY[::-1]
        return (self.aX, self.aY)

def extractData(data) -> tuple[str, str, int, int]:
    """
    Data is formatted as such:
        - Line 0: length of X and length of Y
        - Line 1: gap cost and mismatch cost (where mismatch cost is the same
          for every pair of distinct symbols)
        - Line 2: X sequence
        - Line 3: Y sequence
    """
    l_2 = data[1].split()    
    a_gap = int(l_2[0])
    a_mm = int(l_2[1])

    X = data[2].strip()
    Y = data[3].strip()

    return (X, Y, a_gap, a_mm)
