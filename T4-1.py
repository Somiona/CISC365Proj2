"""
Enter names and Stu# here!
Name: Somion Tian
Stu#: 20093560
Name:
Stu#:
Name:
Stu#:
"""

"""
Enter your pseudo code here!
- To jump to island i, we either go through i-1 or i-2, so the state transformation would be:
f(0) = 0
f(1) = cost(0)
f(2) = min(f(1) + cost(1), f(0) + cost(0))
f(i) = min{f(i-1)+cost(i-1), f(i-2)+cost(i-2) }
So the pseudo code would be:

FUNCTION island_hopping {
    INPUT: (Cost: cost of leaving island i)
    OUTPUT: The string containing hop path and cost

    ASSERT Length(Cost) >= 1 // otherwise theres's only one way to jump.
    Integer size = Length(Cost)

    Set Choice := {One, Two}
    List<Choice> minHop := [None repeated (size + 1) times]
    minHop_1 <- One
    List<Integer> minPath := [-1 repeated (size + 1) times]
    minPath_{0, 1} <- [0, Cost[0]]

    LOOP i ∈ [2, size] {
        costFromTwo := minPath[i-2] + Cost[i-2]
        costFromOne := minPath[i-1] + Cost[i-1]
        IF costFromOne < costFromTwo {
            We decide to take one hop, update minPath_i and minHop_i with costFromOne
        } ELSE {
            We decide to take two hops, update minPath_i and minHop_i with costFromTwo
        }
    }

    String hopPath := size

    REPEAT {
        Trace minHop backward to decide jump 2 or 1 for each hop.
        Append island# after current hop to hopPath
    } UNTIL We reach the first island

    RETURN (Last number in minPath List, Reverse(hopPath))
}

This code loops through input only once so it must be O(n)
"""


def island_hopping(c):
    """
    Enter your code here!
    """
    size = len(c)
    assert size > 1

    minHop = [0 for _ in range(size + 1)]
    # 1 denoting jump back 1, 2 denoting jump back 2
    minHop[1] = 1
    # i-th place stores the min cost jumping to island# i
    minPath = [-1 for _ in range(size + 1)]
    minPath[0], minPath[1] = 0, c[0]

    for i in range(2, size+1):
        # Make the table. In order to arrive island i, we need to hop from either island i-1 or island i-2
        costFromTwo = minPath[i-2] + c[i-2]
        costFromOne = minPath[i-1] + c[i-1]
        if costFromOne < costFromTwo:
            # Choose from lower cost path
            minPath[i] = costFromOne
            minHop[i] = 1
        else:
            # For the case when i-1 and i-2 have the same cost, prefer the one with shorter path.
            minPath[i] = costFromTwo
            minHop[i] = 2

    # Notice that i = size now, so we does not need another index variable
    path = str(size)

    while i > 0:
        # Traverse backward to build the hopping path
        if minHop[i] == 2:
            i -= 2
        elif minHop[i] == 1:
            i -= 1

        path += f"-{i}"

    return (minPath[size], path[::-1])  # path[::-1] reverses the string.


"""
Testing code
"""

c = (2,15,32,3)
print(c)
print("Answer (20, '0-1-3-4')")
print(island_hopping(c),"\n")

c = (10,10,40,33,15,1)
print(c)
print("Answer (54, '0-1-3-5-6')")
print(island_hopping(c),"\n")

c = (15,3,11,36)
print(c)
print("Answer (26, '0-2-4')")
print(island_hopping(c),"\n")

c = (15,3,11,36,2,18)
print(c)
print("Answer (28, '0-2-4-6')")
print(island_hopping(c),"\n")

c = (15,3,11,17,36,2,18)
print(c)
print("Answer (37, '0-1-3-5-7')")
print(island_hopping(c),"\n")

c = (5,3,17,6,2,16,1)
print(c)
print("Answer (17, '0-1-3-4-6-7')")
print(island_hopping(c),"\n")

# Complexity Explanation:
# THe complexity of the program would be: O(n)
# - Assignment of size -                     O(1)
# - Assert function -                        O(1)
# - Assignment for minHop -                  O(n)
# - Assignment for minHop[1] -               O(1)
# - Assignment for minPath -                 O(n)
# - Assignment for minPath[0], minPath[1] -  O(1)
# - For Loop & if-else Statement -           O(n)
# - Aissgnment for path  -                   O(1)
# - While Loop & if-else Statement -         O(n)     
# Therefore, the complexity of the program would be O(n).
