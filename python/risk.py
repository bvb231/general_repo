import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


def calcKelly(mean, std, r):
  return (mean - r) / std**2

def getKellyFactor(returns: pd.Series, r=0.01, 
  max_leverage=None, periods=252, rolling=True):
  '''
  Calculates the Kelly Factor for each time step based
  on the parameters provided.
  '''
  if rolling:
    std = returns.rolling(periods).std()
    mean = returns.rolling(periods).mean()
  else:
    std = returns.expanding(periods).std()
    mean = returns.expanding(periods).mean()

  r_daily = np.log((1 + r) ** (1 / 252))
  kelly_factor = calcKelly(mean, std, r_daily)
  # No shorts
  kelly_factor = np.where(kelly_factor<0, 0, kelly_factor)
  if max_leverage is not None:
    kelly_factor = np.where(kelly_factor>max_leverage,
      max_leverage, kelly_factor)
    
  return kelly_factor

def LongOnlyKellyStrategy(data, r=0.02, max_leverage=2, periods=252, 
  rolling=True):
  data['returns'] = data['Close'] / data['Close'].shift(1)
  data['log_returns'] = np.log(data['returns'])
  data['kelly_factor'] = getKellyFactor(data['log_returns'], 
    r, max_leverage, periods, rolling)
  cash = np.zeros(data.shape[0])
  equity = np.zeros(data.shape[0])
  portfolio = cash.copy()
  portfolio[0] = 1
  cash[0] = 1
  for i, _row in enumerate(data.iterrows()):
    row = _row[1]
    if np.isnan(row['kelly_factor']):
      portfolio[i] += portfolio[i-1]
      cash[i] += cash[i-1]
      continue

    portfolio[i] += cash[i-1] * (1 + r)**(1/252) + equity[i-1] * row['returns']
    equity[i] += portfolio[i] * row['kelly_factor']
    cash[i] += portfolio[i] * (1 - row['kelly_factor'])

  data['cash'] = cash
  data['equity'] = equity
  data['portfolio'] = portfolio
  data['strat_returns'] = data['portfolio'] / data['portfolio'].shift(1)
  data['strat_log_returns'] = np.log(data['strat_returns'])
  data['strat_cum_returns'] = data['strat_log_returns'].cumsum()
  data['cum_returns'] = data['log_returns'].cumsum()

  return data

def getStratStats(log_returns: pd.Series, risk_free_rate: float = 0.02):
  stats = {}  # Total Returns
  stats['tot_returns'] = np.exp(log_returns.sum()) - 1  
  
  # Mean Annual Returns
  stats['annual_returns'] = np.exp(log_returns.mean() * 252) - 1  
  
  # Annual Volatility
  stats['annual_volatility'] = log_returns.std() * np.sqrt(252)  
  
  # Sortino Ratio
  annualized_downside = log_returns.loc[log_returns<0].std() * \
    np.sqrt(252)
  stats['sortino_ratio'] = (stats['annual_returns'] - \
    risk_free_rate) / annualized_downside  
  
  # Sharpe Ratio
  stats['sharpe_ratio'] = (stats['annual_returns'] - \
    risk_free_rate) / stats['annual_volatility']  
  
  # Max Drawdown
  cum_returns = log_returns.cumsum() - 1
  peak = cum_returns.cummax()
  drawdown = peak - cum_returns
  max_idx = drawdown.argmax()
  stats['max_drawdown'] = 1 - np.exp(cum_returns[max_idx]) / np.exp(peak[max_idx])
  
  # Max Drawdown Duration
  strat_dd = drawdown[drawdown==0]
  strat_dd_diff = strat_dd.index[1:] - strat_dd.index[:-1]
  strat_dd_days = strat_dd_diff.map(lambda x: x.days).values
  strat_dd_days = np.hstack([strat_dd_days,
    (drawdown.index[-1] - strat_dd.index[-1]).days])
  stats['max_drawdown_duration'] = strat_dd_days.max()

  return stats

# Kelly money management for trading strategy
def KellySMACrossOver(data, SMA1=50, SMA2=200, r=0.01, 
  periods=252, max_leverage=None, rolling=True):
  '''
  Sizes a simple moving average cross-over strategy according
  to the Kelly Criterion.
  '''
  data['returns'] = data['Close'] / data['Close'].shift(1)
  data['log_returns'] = np.log(data['returns'])
  # Calculate positions
  data['SMA1'] = data['Close'].rolling(SMA1).mean()
  data['SMA2'] = data['Close'].rolling(SMA2).mean()
  data['position'] = np.nan
  data['position'] = np.where(data['SMA1']>data['SMA2'], 1, 0)
  data['position'] = data['position'].ffill().fillna(0)
  data['_strat_returns'] = data['position'].shift(1) * \
    data['returns']
  data['_strat_log_returns'] = data['position'].shift(1) * \
    data['log_returns']
  # Calculate Kelly Factor using the strategy's returns
  kf = getKellyFactor(data['_strat_log_returns'], r, 
    max_leverage, periods, rolling)
  data['kelly_factor'] = kf
  
  cash = np.zeros(data.shape[0])
  equity = np.zeros(data.shape[0])
  portfolio = cash.copy()
  portfolio[0] = 1
  cash[0] = 1
  for i, _row in enumerate(data.iterrows()):
    row = _row[1]
    if np.isnan(kf[i]):
      portfolio[i] += portfolio[i-1]
      cash[i] += cash[i-1]
      continue
    
    portfolio[i] += cash[i-1] * (1 + r)**(1/252) + equity[i-1] * row['returns']
    equity[i] += portfolio[i] * row['kelly_factor']
    cash[i] += portfolio[i] * (1 - row['kelly_factor'])

  data['cash'] = cash
  data['equity'] = equity
  data['portfolio'] = portfolio
  data['strat_returns'] = data['portfolio'] / data['portfolio'].shift(1)
  data['strat_log_returns'] = np.log(data['strat_returns'])
  data['strat_cum_returns'] = data['strat_log_returns'].cumsum()
  data['cum_returns'] = data['log_returns'].cumsum()
  return data


ticker = 'VTI'
yfObj = yf.Ticker(ticker)
data = yfObj.history(start='2000-01-01', end='2020-01-01')
# Drop unused columns
data.drop(['Open', 'High', 'Low', 'Volume', 'Dividends', 
  'Stock Splits'], axis=1, inplace=True)




kelly_sma = KellySMACrossOver(data.copy(), max_leverage=3)

fig, ax = plt.subplots(2, figsize=(15, 8), sharex=True)

ax[0].plot(np.exp(kelly_sma['cum_returns']) * 100, label='Buy-and-Hold')
ax[0].plot(np.exp(kelly_sma['strat_cum_returns'])* 100, label='SMA-Kelly')
ax[0].plot(np.exp(kelly_sma['_strat_log_returns'].cumsum()) * 100, label='SMA')
ax[0].set_ylabel('Returns (%)')
ax[0].set_title('Moving Average Cross-Over Strategy with Kelly Sizing')
ax[0].legend()

ax[1].plot(kelly_sma['kelly_factor'])
ax[1].set_ylabel('Leverage')
ax[1].set_xlabel('Date')
ax[1].set_title('Kelly Factor')

plt.tight_layout()
plt.show()

sma_stats = pd.DataFrame(getStratStats(kelly_sma['log_returns']), 
                         index=['Buy and Hold'])
sma_stats = pd.concat([sma_stats,
            pd.DataFrame(getStratStats(kelly_sma['strat_log_returns']),
              index=['Kelly SMA Model'])])
sma_stats = pd.concat([sma_stats,
            pd.DataFrame(getStratStats(kelly_sma['_strat_log_returns']),
              index=['SMA Model'])])
sma_stats