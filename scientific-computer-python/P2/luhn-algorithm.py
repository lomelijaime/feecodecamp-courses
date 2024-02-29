# Verify a credit card number using the Luhn algorithm
# 1.- From right to left, sum the digits of the card number in odd positions
# 2.- From right to left, double the digits of the card number in even positions
# 3.- If the result of the previous step is greater than 9, sum the digits of the result
# 4.- If the sum of the digits is divisible by 10, the card number is valid

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    #1
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    
    #2
    for digit in even_digits:
        number = int(digit) * 2
        #3
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    #4
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1191'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('Valid card number!')
    else:
        print('Invalid card number!')

main()