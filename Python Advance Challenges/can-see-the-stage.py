# Write a function to determine if all the concert attendence can see the stage

def can_see_stage(seats):

    for i in range(len(seats[0])):
        for j in range(len(seats) - 1):
            if seats[j][i] >= seats[j + 1][i]:
                return False

    return True

print(can_see_stage([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
]))