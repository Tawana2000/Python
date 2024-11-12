# Write a fucntion to find the equations that are true from the given list

def find_true(equations):

    new_lst = [] 

    for i in equations:
        if eval(i.replace('=', '==')):
            new_lst.append(i)

    return new_lst

equations = ['2+2=4', '3*3=6', '1+1=3', '5/5=1']
print(find_true(equations))