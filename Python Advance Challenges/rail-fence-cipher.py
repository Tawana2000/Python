# Write a function to implement the Rail Fence Cipher

def rail_fence_cipher(text, num_rails):
    if num_rails <= 0:
        return ""
    
    fence = [''] * num_rails
    rail = 0
    step = 1
    
    for char in text:
        fence[rail] += char
        rail += step

        if rail == num_rails - 1:
            step = -1
        elif rail == 0:
            step = 1
 
    return ''.join(fence)


print(rail_fence_cipher("Hello World", 3))