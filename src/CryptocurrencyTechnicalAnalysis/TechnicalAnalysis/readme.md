# Math-Work Behind Developing a Trading Strategy.

- [Simple Moving Average](https://www.investopedia.com/terms/s/sma.asp)

### Simple Moving Averages
A moving average is the mean of a certain number of periods conducted over a serie, and serves as the basis for other more
complex indicators.  

The in-house implementation of the algorithm accepts the single argument `window_size`, which denotes how many periods to use
for its calculation; defaulting to `3`, which it appends to the dataframe under the `SMA` header.

For any calculations other than the default, the function adds them to the dataframe under the `{window_size}-Minute SMA` header.

![A flowchart diagram of the workflow behind the SMA algorithm.](https://raw.githubusercontent.com/guyyatsu/CryptocurrencyTechnicalAnalysis/master/screenshots/SimpleMovingAverages.jpg)