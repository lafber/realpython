''' Real Python

    Assignment: Track your investments
    
'''

def invest(amount, rate, time):
    year = 1
    print('principal amount: €{} \nannual rate of return: {}'.format(amount, rate))
    
    while(year <= time):
        amount = amount * ( 1 + rate)
        print('year {}: €{}'.format(year, amount))
        year = year + 1


# main

invest(100, .05, 8)
print('\n')
invest(2000, .025, 5)
