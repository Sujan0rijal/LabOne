'''price of house os $1M. if buyer has good credit,they need to put down 10% 0therwise
 they need to put down 20%
print the down payment   '''

price_house=1000
good_credit= True
if good_credit:
    down_payment=0.1*price_house
else:
    down_payment= 0.2*price_house
print(f'the down payment is ${down_payment}')