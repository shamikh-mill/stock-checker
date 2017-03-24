from yahoo_finance import Share

my_shares = {'BAC':3, 'SNAP':4, 'TWTR':1}

my_cost = {'BAC':25.35, 'SNAP':25.09, 'TWTR':18.15} 
# stock = Share('TICKER')

values = {share: float(Share(share).get_price()) for share in my_cost}

print ('my costs: ', my_cost)
print ('current prices: ',values) 	



