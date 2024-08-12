import pandas as pd
import MetaTrader5 as mt5

def load_data(symbol, timeframe, start_date, end_date):
    mt5.initialize()
    timezone = mt5.TIMEFRAME_M1 if timeframe == '1min' else \
              mt5.TIMEFRAME_M5 if timeframe == '5min' else \
              mt5.TIMEFRAME_M15 if timeframe == '15min' else \
              mt5.TIMEFRAME_M30 if timeframe == '30min' else \
              mt5.TIMEFRAME_H1 if timeframe == '1hour' else \
              mt5.TIMEFRAME_H4 if timeframe == '4hour' else \
              mt5.TIMEFRAME_D1 if timeframe == 'daily' else None

    if timezone is None:
        raise ValueError("Unsupported timeframe")

    rates = mt5.copy_rates_range(symbol, timezone, start_date, end_date)
    mt5.shutdown()

    data = pd.DataFrame(rates)
    data['time'] = pd.to_datetime(data['time'], unit='s')
    data.set_index('time', inplace=True)

    data.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close'}, inplace=True)

    return data