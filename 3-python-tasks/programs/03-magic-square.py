from collections import defaultdict, deque
from copy import deepcopy

def is_magic_square(s3):
    """
        This function will check whether input square is magic or not
        -- input:
            s3 - 3 x 3 square matrix as a input (in the form of list of list)
        -- function:
            Count the sum of rows 
            count the sum of columns
            count the sum of diagonals
            if all the count are same the it's magic

        -- Output
            result as boolean 
    """
    size = len(s3[0])
    list_of_sum = []
    
    #count sum of rows:
    for i in s3:
        list_of_sum.extend([sum(i)]) 

    # count sum of colums
    for col in range(size):
        list_of_sum.append(sum(row[col] for row in s3))
    
    # Count sum of diagonals
    diagonal_1 = 0
    for i in range(0,size):
        diagonal_1 +=s3[i][i]
    list_of_sum.append(diagonal_1)  
    
    diagonal_2 = 0
    for i in range(size-1,-1,-1):
        diagonal_2 +=s3[i][i]
    list_of_sum.append(diagonal_2)

    if len(set(list_of_sum))>1:
        return False

    return True

# Helper function -1 
def magicSum(n):
    return int((n*n * (n*n + 1)) / 6)

# Helper function - 2
def validate(sumDict, n):
    for k, v in sumDict.items():
        if v > magicSum(n):
            return False
    return True

# Helper function -3
def check(sumDict, n):
    for k, v in sumDict.items():
        if v != magicSum(n):
            return False
    return True

# Helper function - 4
def isValid(m, n):
    rowSum = defaultdict(int)
    colSum = defaultdict(int)
    diagSum = defaultdict(int)

    isLeft = False

    for i in range(n):
        for j in range(n):
            if m[i][j] == 0: isLeft = True
            rowSum[i] += m[i][j]
            colSum[j] += m[i][j]
            if i == j: diagSum[0] += m[i][j]
            if i + j == n - 1: diagSum[n - 1] += m[i][j]

    if isLeft:
        return (validate(rowSum, n) and validate(colSum, n) and validate(diagSum, n))       
    return (check(rowSum, n) and check(colSum, n) and check(diagSum, n))        

# Helper function 5
def next(cur, m, n):
    possible = []
    for i in range(n): 
        for j in range(n):
            if m[i][j] == 0:
                nextM = deepcopy(m)
                nextM[i][j] = cur
                if isValid(nextM, n):
                    possible.append(nextM)
    return possible

def generate_3_square():
    """
        This function will generate all the magic square for 3 X 3

    """
    n = 3 # Square size
    startM = [[0 for x in range(n)] for y in range(n)]
    magic = []
    Q = deque([(1, startM)])
    while len(Q):
        state = Q.popleft()
        cur = state[0]
        m = state[1]
        if cur == n * n + 1:
            magic.append(m)
            continue
        for w in next(cur, m, n):
            Q.append((cur + 1, w))
    return magic
        

if __name__ == "__main__":
    s3 =  [ [ 2 , 7 , 6 ] , [ 9 , 5 , 1 ] , [ 4 , 3 , 8 ] ]
    print(is_magic_square(s3))
    print(generate_3_square())