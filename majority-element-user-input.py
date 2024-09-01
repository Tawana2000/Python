
def majority_elemnt(num_list):

    for num in num_list:

        count = num_list.count(num)
        #print(f'The number of occurence for {num} is: ',count), gives extra outputs sometimes (needs to be worked on)

        if count > len(num_list) // 2:
            return num
        
index = int(input('Enter the number of elements: '))
li = []

for i in range(0,index):
    number = int(input())
    li.append(number)

print('The majority element in the given list is: ',majority_elemnt(li))
