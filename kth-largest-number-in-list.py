#Create a Python program to find the kth largest element in a list.
#we can find it through index as well but we will be using a different method, where we remove kth-1 max elements to the Kth largest.

def kth_largest(num_list, k):

    loop_timer = k - 1

    unique_numbers = list(set(num_list))

    while loop_timer > 0:

        current_max = max(unique_numbers)
        unique_numbers.remove(current_max)


        loop_timer -= 1


    kth_largest = max(unique_numbers)
    print(kth_largest)

num_list = [2, 3, 1, 5, 6, 4]
k = 3

kth_largest(num_list, k)