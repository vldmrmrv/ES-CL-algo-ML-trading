## ES algo trading SAMPLES
Algorithmic trading is a method of executing orders using automated pre-programmed trading instructions accounting for variables such as time, price, and volume.

## #1 Example:
Sample of strategy using simple condicions based on moving average with period 15 and initial balance range for buy-only trading ES futures. Chart with P&L (profit and loss - cumulative) and DD (drawdown - maximum cumulative) for better understanting potential Profit and Risk.
```python
df['con1'] = [1 if ibr > pibr else 0 for ibr, pibr in zip(df['IB_RNG'], df['pIB_RNG'])]
df['con2'] = [1 if c < sma else 0 for c, sma in zip(df['RTH_C'], df['SMA'])]
df['signal'] = [1 if c1+c2 == 2 else 0 for c1, c2 in zip(df['con1'], df['con2'])]
```
![Algo IRET](https://github.com/vldmrmrv/ES-algorithmic-trading-strategy/blob/main/ALGO_iret_SAMPLE.png)

## #2 Example:
Long term Buy&Hold timeing strategy using %change of price to indicate potentional long term buying opportunities in SPX (entries with markers for visual interpretation). 
![Buy Opp](https://github.com/vldmrmrv/ES-algorithmic-trading-strategy/blob/main/buying%20opportunities.png)

## #3 Example:
Sample of strategy using simple condicions based on opening above SMA20 and specific previous days closes for buy-only trading ES futures. Chart with P&L (profit and loss - cumulative) and DD (drawdown - maximum cumulative) for better understanting potential Profit and Risk.
```python
df['con2'] = [1 if op >= sm else 0 for op, sm in zip(df['Open'], df['SMA'])]
df['con3'] = [1 if p == 'D' and pp == 'D' else 0 for p, pp in zip(df['p_UD'], df['pp_UD'])]
df['signal'] = [1 if c1+c2+c3 == 3 else 0 for c1, c2, c3 in zip(df['con1'], df['con2'], df['con3'])]
```
![Algo sma](https://github.com/vldmrmrv/ES-algorithmic-trading-strategy/blob/main/ALGO_sma20_pD_ppD_SAMPLE.png)

## #4 Example:
Sample of strategy similar to #3 useing SMA20 and specific previous days closes for buy-only trading ES futures with an intraday holding time (no possitions are hold overnight). Chart with P&L (profit and loss - cumulative) and DD (drawdown - maximum cumulative) for better understanting potential Profit and Risk.

![Algo intra](https://github.com/vldmrmrv/ES-algorithmic-trading-strategy/blob/main/ALGO_intra_SAMPLE.png)

## #5 Example:
Strategy useing candle patterns and OHLC values for buy-only trading ES futures with an intraday holding time (no possitions are hold overnight). Chart with P&L (profit and loss - cumulative) and DD (drawdown - maximum cumulative) for better understanting potential Profit and Risk.

![Algo rrtt](https://github.com/vldmrmrv/ES-algorithmic-trading-strategy/blob/main/ALGO_rrtt.png)
