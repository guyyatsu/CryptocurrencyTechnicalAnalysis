# Technical Analysis of Cryptocyrrency Trading Pairs


## Step One: Data.
Cryptocurrency moves faster than securities, and so we don't need to collect a lot of high-resolution
data in order to make an accurate prediction.  In fact, if we _are_ going for a high granularity then
I'd say a week at most of every minute would provide a solid enough foundation of information upon
which to think.

Not only just we also need to collect data on **every** currency pair offered by `Alpaca.Markets`, so
we need to design our function with that in mind.

Besides that, there's also the design schema for our database; `alpaca-py` offers cryptocurrency
assets in the form of `trading pairs`, which describe avenues of liquidity through ownership.
If we ignore `USD Coin` and `USD Tether` (because they're trash anyways) then we can
**pretty much assume** that we can only buy assets directly, as opposed to trading eachother.


### Database Layout
The `finance.db` file located within the project root consist of two tables for tracking two different
sources of information; `historic_performance_data` and `live_transaction_ledger`, where the former
keeps a back log of the quoted price at any given moment up to so many minutes ago and the latter
tracks successful transactions as they happen.

#### Historic Performance Data
| Symbol    | Epoch       | High     | Low      | Open     | Close    |
| --------- | ----------- | -------- | -------- | -------- | -------- |
| `BTC/USD` | 10202938.43 | 47632.23 | 46473.34 | 45765.44 | 48754.69 |

#### Live Transaction Ledger
| Symbol    | Epoch       | Ask Price | Ask Size | Bid Price | Bid Size |
| --------- | ----------- | --------- | -------- | --------- | -------- |
| `BTC/USD` | 57438994.99 | 57438.94  | 0.94     | 56473.33  | 0.89     |


### Data-Points tracked by the Historic client:
- `id`: Unique UUID identifier for machine-readable assets.
- `asset_class`: Assets could either be `CRYPTO` or `STOCKS`;.
- `exchange`: Could either be the `STOCK` exchange or the `CRYPTO` exchange.
- `symbol`: Unique namespace for identifying an asset in market terms.
- `name`: Human-Readable representation of an asset pair.
- `status`: Is the asset still alive?
- `tradable`: Is it available for sale?
- `marginable`: Is it open to margining?
- `shortable`: Can it be shorted?
- `easy_to_borrow`: Can it be borrowed?
- `fractionable`: Do I have to own the whole unit?
- `min_order_size`: Least amount able to be purchased.
- `min_trade_increment`
- `price_increment`: Smallest unit of trade.
- `maintenance_margin_requirement`
- `attributes`


### Data-Points tracked by the Live Stream:
- `symbol`:
- `timestamp`:
- `tzinfo`:
- `ask_exchange`:
- `ask_price`:
- `ask_size`:
- `bid_exchange`:
- `bid_price`:
- `bid_size`:
- `conditions`:
- `tape`:


## Step Two: Analysis.
## Step Three: Decision.
## Step Four: Action.