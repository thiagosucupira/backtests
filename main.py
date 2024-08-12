from backtesting import Backtest
from strategies.ATR_Wobble import ATRWobbleTradeStrategy
from utils.data_loader import load_data

# Backtesting setup
symbol = "EURUSD"
backtest_start_date = '2023-01-01'
backtest_end_date = '2023-12-31'

# Load data
data = load_data(symbol, '1hour', backtest_start_date, backtest_end_date)

# Backtest execution
bt = Backtest(data, ATRWobbleTradeStrategy, cash=10000, commission=0.0002)
stats = bt.run()

# Output results
print(stats)
bt.plot()