# Write a function to determine if a cargo fits in a box

def cargo_fit(box_dimensions, cargo_volume):
     
    total_dimensions = 1
    for num in box_dimensions:
        total_dimensions *= num
    
    return True if total_dimensions == cargo_volume else False

box_dimensions = [3, 4, 5]
cargo_volume = 60

print(cargo_fit(box_dimensions, cargo_volume))