def profitCounter():
    howMuchWillYouSelling = float(input('How Much Will You Sell: '))
    priceWhenBought = float(input('Price When Bought: '))
    priceWhenSold = float(input('Price When Sold: '))

    if howMuchWillYouSelling == None or priceWhenBought == None or priceWhenSold == None: return 'There is a None'
    percentProfit = priceWhenSold / priceWhenBought * 100 - 100
    dollarProfit = howMuchWillYouSelling * priceWhenSold - howMuchWillYouSelling * priceWhenBought

    return f'Profit: {str(percentProfit)[:5]}%  =  {str(dollarProfit)[:4]}$'

status = 1
while status == 1:
    print(profitCounter())
    status = int(input('Write "1" to start again. otherwise press any key...  '))