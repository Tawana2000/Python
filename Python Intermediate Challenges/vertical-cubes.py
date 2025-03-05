# Write a function to pile up cubes vertically. The cubes are of different sizes and must be piled from largest to smallest. The function should return 'Yes' if the cubes can be pile up and 'No' otherwise

def pile_up_cubes(cubes):

    if not cubes:
        return 'Yes' 
    
    max_cube = max(cubes)
    max_index = cubes.index(max_cube)
    
    for i in range(max_index):
        if cubes[i] < cubes[i + 1]:
            return 'No'
    
    for i in range(max_index, len(cubes) - 1):
        if cubes[i] < cubes[i + 1]:
            return 'No'
    
    return 'Yes'

print(pile_up_cubes([1, 2, 3, 4, 3, 2, 1]))
print(pile_up_cubes([1, 3, 2]))             
print(pile_up_cubes([1, 2, 1, 4]))     
print(pile_up_cubes([]))                   
print(pile_up_cubes([5, 4, 3, 2, 1]))