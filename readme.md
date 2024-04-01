# Technical Analysis of Cryptocyrrency Trading Pairs


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



### Data-Points tracked by `Alpaca-Py`:
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

## Database Table Layout.
## Collect and Rotate Bar Data.
