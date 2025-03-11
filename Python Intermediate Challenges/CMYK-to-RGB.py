# Write a function to convert a color from CMYK format to RGB format.

"""
R = 255 x (1 - C) x (1 - K)
G = 255 x (1 - M) x (1 - K)
B = 255 x (1 - Y) x (1 - K)
"""

def cmyk_to_rgb(cmyk):
    c, m, y, k = cmyk 

    R = 255 * (1 - c) * (1 - k)
    G = 255 * (1 - m) * (1 - k)
    B = 255 * (1 - y) * (1 - k)

    return (round(R), round(G), round(B)) 

cmyk = [0.4, 0.49, 0.552, 0.36]
print(cmyk_to_rgb(cmyk))