#Create a Python program to add 1 to the number represented by the given list, for the input [8,9,9] the output should be [9,0,0], similarly for the input [1,2,4,4] the output should be [1,2,4,5]

def increase(list_numbers):
    
    list_numbers[-1] += 1
    carry = list_numbers[-1] // 10             #gertting the carry
    list_numbers[-1] = list_numbers[-1] % 10    #replacing the last digit with the reminder
    
    #continue adding carry to each digit from second last element
    for i in range(len(list_numbers) -2, -1, -1):
        if carry:
            list_numbers[i] += carry
            carry = list_numbers[i] // 10
            list_numbers[i] = list_numbers[i] % 10
 
    #even after adding all the carries, if one carry is still remaining , we need to add that at the beginning
    if carry:
            list_numbers.insert(0,carry)

    return list_numbers
    
list_numbers = [8,9,9]
print(increase(list_numbers))