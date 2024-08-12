import pandas as pd
import numpy as np
from backtesting import Backtest, Strategy

# ATR calculation function
def ATR(df, period=14):
    high_low = df['High'] - df['Low']
    high_close = np.abs(df['High'] - df['Close'].shift())
    low_close = np.abs(df['Low'] - df['Close'].shift())
    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    true_range = np.max(ranges, axis=1)
    return true_range.rolling(period).mean()

# ATR Wobble Trade Strategy
class ATRWobbleTradeStrategy(Strategy):
    atr_period = 14
    position_size = 0.01
    max_open_trades = 3
    
    def init(self):
        self.atr = self.I(ATR, self.data.df, self.atr_period)
    
    def next(self):
        current_price = self.data.Close[-1]
        previous_high = self.data.High[-2]
        previous_low = self.data.Low[-2]
        atr_value = self.atr[-1]
        
        # Buy conditions
        if (current_price <= previous_high and current_price >= previous_low) and ((previous_high - current_price) <= atr_value):
            if len(self.trades) < self.max_open_trades:
                self.buy(size=self.position_size, sl=current_price - atr_value, tp=previous_high + 0.0005)
#TODO SELLS 