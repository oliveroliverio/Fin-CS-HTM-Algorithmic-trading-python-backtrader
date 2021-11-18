import backtrader as bt
import datetime

# data = bt.feeds.YahooFinancialData()

cerebro = bt.Cerebro()
cerebro.broker.set_cash(2000000)

print("starting portfolio value: %.2f" % cerebro.broker.getvalue())

cerebro.run()