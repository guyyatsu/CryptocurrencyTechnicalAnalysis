# Technical Analysis of Cryptocyrrency Trading Pairs


## Data Curation
We need a reliable dataset to train our monkey on; preferrably highly granular, and extending pretty far back.
Luckily, my preferred brokerage `Alpaca` offers minutely candlestick bars going all the way back to
December 2013.  Now we could just use any other pre-made dataset offered by anyone, but I want to showcase an
understanding of real data-science principles and work ethic here so I'm rolling my own.

The `PriceData` and `DatabaseOperations` submodules further describe the method behind data curation in greater
detail.

### Historic Performance Data
| Symbol    | Epoch       | High     | Low      | Open     | Close    |
| --------- | ----------- | -------- | -------- | -------- | -------- |
| `BTC/USD` | 10202938.43 | 47632.23 | 46473.34 | 45765.44 | 48754.69 |

Historic data can be interacted with through the `TechnicalAnalysis` submodule, which expands the dataset further
by calculating indicators based on the bars provided.

#### Live Transaction Ledger
| Symbol    | Epoch       | Ask Price | Ask Size | Bid Price | Bid Size |
| --------- | ----------- | --------- | -------- | --------- | -------- |
| `BTC/USD` | 57438994.99 | 57438.94  | 0.94     | 56473.33  | 0.89     |

Once we have an agent trained on the historic data and tweak it to our liking we need to keep it updated with
current data as it comes in.  The `Alpaca` historic data client only goes up to fifteen minutes ago, but also
they offer live bid/ask/amount transactions as new orders get placed on the books.  This adds a layer of complexity,
as I'm not quite sure on the mechanism behind interpreting this kind of data.  From what I gather, it's similar to
the one about predicting housing prices in a given area using linear regression.

Anyways, we need to be able to interpret this live market data as quickly as possible so we can make a decision
while the information is still relevant.


## Step Two: Analysis.
## Step Three: Decision.
## Step Four: Action.
