print('Please, rating from 1–10 on the following questions: ')
loan_size = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income_size = int(input('How high is your income? '))
down_payment_size = int(input('How large is your down payment? '))

if loan_size >= 5:
    if credit_history >= 7 and income_size >= 7:
        decision = 'YES'
    elif credit_history >= 7 or income_size >= 7:
        if down_payment_size >= 5:
            decision = 'YES'
        else:
            decision = 'NO'
    else:
        decision = 'NO'
else:
    if credit_history < 4:
        decision = 'NO'
    else:
        if income_size >= 7 or down_payment_size >= 7:
            decision = 'YES'
        elif income_size >= 4 and down_payment_size >= 4:
            decision = 'YES'
        else:
            decision = 'NO'

print(f'the decision is {decision}')