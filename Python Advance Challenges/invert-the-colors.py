# Write a function to invert the colors of an image

def invert_color(color):

    hex_value = color.lstrip('#')
    rgb = int(hex_value, 16)

    inverted = 0xFFFFFF - rgb
    invert_hex = hex(inverted)[2:].zfill(6)

    return '#' + invert_hex

print(invert_color('#000000'))