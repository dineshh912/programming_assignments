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


def generate_3_square():
    """
        This function will generate all the magic square for 3 X 3

    """
    n = 3 # Square size
    square=[]
    for i in range(n):
            l=[]
            for v in range(n):
                l.append(0)
            square.append(l)
    count=1
    i=n//2
    j=n-1
    while count<=n*n:
        if i==-1 and j==n:
            j=n-2
            i=0
        else:
            if i<0:
                i=n-1
            if j==n:
                j=0
        if square[i][j]!=0:
            j=j-2
            i=i+1
            continue
        else:
            square[i][j]=count
            count+=1
        i=i-1
        j=j+1
    for i in range(n):
            for j in range(n):
                print(square[i][j],end=" ")
            print()

if __name__ == "__main__":
    s3 =  [ [ 2 , 7 , 6 ] , [ 9 , 5 , 1 ] , [ 4 , 3 , 8 ] ]
    print(is_magic_square(s3))
    generate_3_square()