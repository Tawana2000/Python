# Write a function to check if you have hit the jackpot in a slot machine

def check_jackpot(slot_outcome):

    return all(item == slot_outcome[0] for item in slot_outcome)

print(check_jackpot([1, 2, 1, 1]))
        