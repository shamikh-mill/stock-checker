import yahoo_finance
import threading


def check(my_shares, my_cost): 
	# stock = Share('TICKER')

	values = {share: float(yahoo_finance.Share(share).get_price()) for share in my_cost}
	# get stock values 
	profit = {share: float("%.2f" % round((values[share] - my_cost[share]), 2)) for share in values} 
	#stock differential rounded to two decimal places

	up_stocks = [p for p in profit if profit[p] * my_shares[p] > 0]
	
	# paid price and current price differential multiplied by quantity owned 
	print ('my costs: ', my_cost)
	print ('current prices: ',values) 	
	print ('profits: ', profit)
	print('my results:')
	# threading.Timer(10, check(my_shares, my_cost)).start()

	if len(up_stocks) == 0: 
		print ('rip no stocks are positive')
	#	return "you should stop investing", up_stocks
	else:
		print (up_stocks)
	#	return "you should look into selling", up_stocks
	# implement dict with yahoo.refresh()


if __name__ == '__main__':
	my_shares = {'BAC':3, 'SNAP':4, 'TWTR':1}
	my_cost = {'BAC':25.35, 'SNAP':25.09, 'TWTR':18.15} 
	check(my_shares, my_cost)
