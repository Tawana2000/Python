# Write a function to simulate a robot's path based on commands
# The robot starts at position (0,0). It can move up, down, left or right based on the commands 'U','D','L' and 'R' respectively.

def robot_path(commands):

    x, y = 0, 0

    for cmd in commands:
        if cmd == 'U':
            y += 1
        elif cmd == 'D':
            y -= 1
        elif cmd == 'R':
            x += 1
        elif cmd == 'L':
            x -= 1

    return (x, y)

print(robot_path("URDL")) 
print(robot_path("UURR"))  
print(robot_path("LLDD"))
