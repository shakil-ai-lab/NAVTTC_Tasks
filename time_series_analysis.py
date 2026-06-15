import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA

# Synthetic time series data
dates = pd.date_range(start='2023-01-01', periods=48, freq='M')
trend = np.linspace(50, 90, len(dates))
seasonal = 10 * np.sin(2 * np.pi * dates.month / 12)
noise = np.random.normal(scale=3, size=len(dates))
values = trend + seasonal + noise

ts_df = pd.DataFrame({'Date': dates, 'Sales': values})
ts_df.set_index('Date', inplace=True)
print('Time series sample:')
print(ts_df.head())
print()

# Decompose the time series
result = seasonal_decompose(ts_df['Sales'], model='additive', period=12)
print('Seasonal decomposition summary:')
print('Trend last value:', result.trend.dropna().iloc[-1])
print('Seasonal first value:', result.seasonal.iloc[0])
print('Residual first value:', result.resid.dropna().iloc[0])
print()

# Fit ARIMA model as a simple forecast
ts_model = ARIMA(ts_df['Sales'], order=(1,1,1))
model_fit = ts_model.fit()
forecast = model_fit.forecast(steps=6)
print('ARIMA forecast for next 6 periods:')
print(forecast)
