# Write a function to calculate the simple interest and the final amount
# simple interest = (principal * rate * time) / 100
# Final amount = simple interest + principle

def simple_interest(principal, rate, time):

    si = (principal * rate * time) / 100
    final_amount = si + principal
    result = (si, final_amount)
    return result

principal = int(input("Enter the principle amount: "))
rate = int(input("Enter the rate: "))
time = int(input("Enter the duration in month: "))

print(simple_interest(principal, rate, time))