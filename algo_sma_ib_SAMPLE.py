import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 500)
df = pd.read_csv('es_data_final.csv', sep=';')
df = df.dropna()

# previous day close and IB range
df['pRTH_C'] = df['RTH_C'].shift(1)
df['pIB_RNG'] = df['IB_RNG'].shift(1)

# indicator SMA 15 close
df['SMA'] = df['RTH_C'].rolling(15).mean()

# signal
df['con1'] = [1 if ibr > pibr else 0 for ibr, pibr in zip(df['IB_RNG'], df['pIB_RNG'])]
df['con2'] = [1 if c < sma else 0 for c, sma in zip(df['RTH_C'], df['SMA'])]
df['signal'] = [1 if c1+c2 == 2 else 0 for c1, c2 in zip(df['con1'], df['con2'])]

# returns
df['return'] = df['RTH_C'].shift(-2) - df['RTH_C'].shift(-1)
df['trades'] = df['signal'] * df['return'] * 50

# drop non trades days
trades = df[df['signal'] == 1]

# P&L, DD charts
trades['P&L'] = trades['trades'].cumsum()
trades['DD'] = trades['P&L'] - trades['P&L'].cummax()

print(df.head(25))

# Plot charts
trades[['P&L', 'DD']].plot(subplots=True)
plt.show()
