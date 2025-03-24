# Write a function to return the skyline formed by a set of buildings collectively

def get_skyline(buildings):
    
    pts = sorted([(l, -h) for l, r, h in buildings] + [(r, h) for l, r, h in buildings])
    res, h = [[0, 0]], [0]
    for x, y in pts:
        if y < 0: h.append(-y)
        else: h.remove(y)
        if res[-1][1] != max(h): res += [[x, max(h)]]
    return res[1:]

print(get_skyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
