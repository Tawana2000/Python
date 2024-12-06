# Write a function to hide a credit card number

def mask_credit_card(card_number):

    card_nunmber = card_number.replace(" ", "").replace("-", "")       #Ensure the input is string and remove any spaces or dashes

    if len(card_nunmber) < 4:
        return 'Invalid card number'
    
    masked_number = '*' * (len(card_nunmber) - 4) + card_nunmber[-4:]      #Mask all except the last four
    return masked_number

card_number = input('Enter your credit card number: ')
print("Masked Credit Card: ", mask_credit_card(card_number))