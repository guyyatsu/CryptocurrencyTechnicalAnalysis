# Math-Work Behind Developing a Trading Strategy.
Once the work has been done to procure a trustable dataset formatted in a way we can interact with through code as per the
guidelines laid out by the [`DatasetCuration`](https://github.com/guyyatsu/CryptocurrencyTechnicalAnalysis/tree/master/src/CryptocurrencyTechnicalAnalysis/DatabaseOperations#dataframecuration) sub-routine we can begin to make assumptions based on
`indicators` extrapolated from the baseline data.  Ultimately, it is combinations of votes to either `BUY`, `SELL`, or `HOLD`
that the [`Quantum Table`]() will rate and weight itself based on the performance of.


### Simple Moving Averages
A moving average is the mean of a certain number of periods conducted over a serie, and serves as the basis for other more
complex indicators.  

The in-house implementation of the algorithm accepts the single argument `window_size`, which denotes how many periods to use
for its calculation; defaulting to `3`, which it appends to the dataframe under the `SMA` header.

For any calculations other than the default, the function adds them to the dataframe under the `{window_size}-Minute SMA` header.

![A flowchart diagram of the workflow behind the SMA algorithm.](https://raw.githubusercontent.com/guyyatsu/CryptocurrencyTechnicalAnalysis/master/screenshots/SimpleMovingAverages.jpg)