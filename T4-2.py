"""
Enter names and Stu# here!

Kyle Verma, 20155370
"""

"""
Enter your pseudo code here!

total paths = 2d list starting at 0. List will return total paths for speciied cherry location

if at 0,0 there are no ghosts 
    set total paths at 0,0 to 1

else
    set total paths at 0,0 to 0

initialize row for the 2d list
    set totalPaths at 0,i to 0,i-1 if there is no ghost at the first row

initialize column for the 2d list
    set totalPaths at j,0 to j-1,0 if ther is no ghost at the first column

process 2d list
    if the index in question has no ghost
        sum the paths

return total paths
"""


def pacman(ghost):
    """
    Enter your code here!
    """
    # creating 2-d list for ghost location matrix that will return the total paths to cherries
    totalPaths = [[0] * len(ghost[0]) for i in ghost]

    # Pacman starts at 0,0
    # set totalPaths at 0,0 to 1 if there is a ghost
    if ghost[0][0] == 0:
        totalPaths[0][0] = 1
    
    # otherwise set totalPaths at 0,0 to 0
    else:
        totalPaths[0][0] = 0
    
    # row, set totalPaths at 0,i to 0,i-1 if there is no ghost at the first row
    for i in range(1, len(ghost)):
        if ghost[0][i] == 0:
            totalPaths[0][i] = totalPaths[0][i-1]
    
    # column, set totalPaths at j,0 to j-1,0 if ther is no ghost at the first column
    for j in range(1, len(ghost)):
        if ghost[j][0] == 0:
            totalPaths[j][0] = totalPaths[j-1][0]
    
    # process the 2d list
    # first go through each row
    for i in range(1, len(ghost)):
        # then go through each column in every row
        for j in range(1, len(ghost)):
            # if no ghost is blocking the corresponding location, return sum of the paths
            if ghost[i][j] == 0:
                totalPaths[i][j] = totalPaths[i-1][j] + totalPaths[i][j-1]
    
    # return location at (n-1, n-1), the location of the cherries
    return totalPaths[-1][-1]

    
    
                    

"""
Testing code
"""

ghost=[[0,1],
       [0,0]]
print("for input:", ghost)
print("Answer: 1")
print(pacman(ghost),"\n")


ghost=[[0,1],
       [0,0]]
print("for input:", ghost)
print("Answer: 0")
print(pacman(ghost),"\n")


ghost=[[0,0,0,1],
       [0,1,0,0],
       [0,0,0,0],
       [0,0,0,0]]
print("for input:", ghost)
print("Answer: 7")
print(pacman(ghost),"\n") 


















