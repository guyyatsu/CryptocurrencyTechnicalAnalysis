# Technical Analysis of Cryptocyrrency Trading Pairs
- [Curate Data](#step-one-curate-a-dataset)
  1. [Identify Currency Pairs](#database-table-layout)
- Interpret Data

## Step One: Curate a Dataset.

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

### Currencies offered by `Alpaca-Py`:
- `DOGE`
- `USDC`
- `AAVE`
- `USD`
- `USDT`
- `AVAX`
- `BAT`
- `BCH`
- `BTC`
- `CRV`
- `DOT`
- `ETH`
- `GRT`
- `LINK`
- `LTC`
- `MKR`
- `SHIB`
- `SUSHI`
- `UNI`
- `XTZ`
- `YFI`

### Currency Pairs offered by `Alpaca-Py`:
- `Dogecoin  &  USD Coin`
- `Aave  &  US Dollar`
- `Aave  &  USD Coin`
- `Aave  &  USD Tether`
- `Avalanche  &  US Dollar`
- `Avalanche  &  USD Coin`
- `Avalanche  &  USD Tether`
- `Basic Attention Token  &  US Dollar`
- `Basic Attention Token  &  USD Coin`
- `Bitcoin Cash  &  Bitcoin `
- `Bitcoin Cash  &  US Dollar`
- `Bitcoin Cash  &  USD Coin`
- `Bitcoin Cash  &  USD Tether`
- `Bitcoin   &  US Dollar`
- `Bitcoin  &  USD Coin`
- `Bitcoin  &  USD Tether`
- `Curve  &  US Dollar`
- `Curve  &  USD Coin`
- `Dogecoin  &  US Dollar`
- `Dogecoin  &  USD Tether`
- `Polkadot  &  US Dollar`
- `Polkadot  &  USD Coin`
- `Ethereum  &  Bitcoin `
- `Ethereum  &  US Dollar`
- `Ethereum  &  USD Coin`
- `Ethereum  &  USD Tether`
- `The Graph  &  US Dollar`
- `The Graph  &  USD Coin`
- `Chainlink  &  Bitcoin `
- `Chainlink  &  US Dollar`
- `Chainlink  &  USD Coin`
- `Chainlink  &  USD Tether`
- `Litecoin  &  Bitcoin `
- `Litecoin  &  US Dollar`
- `Litecoin  &  USD Coin`
- `Litecoin  &  USD Tether`
- `Maker  &  US Dollar`
- `Maker  &  USD Coin`
- `Shiba Inu  &  US Dollar`
- `Shiba Inu  &  USD Coin`
- `SushiSwap  &  US Dollar`
- `SushiSwap  &  USD Coin`
- `SushiSwap  &  USD Tether`
- `Uniswap  &  Bitcoin`
- `Uniswap  &  US Dollar`
- `Uniswap  &  USD Coin`
- `Uniswap  &  USD Tether`
- `USD Tether  &  US Dollar`
- `USD Tether  &  USD Coin`
- `Tezos  &  US Dollar`
- `Tezos  &  USD Coin`
- `Yearn Finance  &  US Dollar`
- `Yearn Finance  &  USD Coin`
- `Yearn Finance  &  USD Tether`
- `USDC & USD pair`

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
