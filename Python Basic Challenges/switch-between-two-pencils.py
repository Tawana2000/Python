# Write a function to switch between two pencils based on the lenght of their lead

def switch_pencil(pencil1, pencil2):
    return 'Pencil 2' if pencil2 > pencil1 else 'Pencil 1'

print(switch_pencil(4, 2))
