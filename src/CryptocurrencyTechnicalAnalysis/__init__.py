#!/bin/python3
from alpaca.trading.client import TradingClient
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame

from datetime import datetime, timedelta
from decouple import config
from datetime import datetime

from sqlite3 import connect


""" Constants Definition """
# Import Alpaca API credentials.
key = config("ALPACA_KEY")
secret = config("ALPACA_SECRET")
database = "/home/library/software/CryptocurrencyTechnicalAnalysis/finance.db"
connection = connect(database)
cursor = connection.cursor()


class HistoricPerformanceBars:
    def __init__( self ):
        yestermorrow = datetime.now() - timedelta(days=3)
        bar = CryptoHistoricalDataClient().get_crypto_bars(
            CryptoBarsRequest( symbol_or_symbols=["BTC/USD"],
                               timeframe=TimeFrame.Minute,
                               start=yestermorrow,
                               end=datetime.now())
        ); bar.df
        self.data = bar["BTC/USD"]


for entry in HistoricPerformanceBars().data:
    cursor.execute("""
        INSERT OR IGNORE INTO historic_price_data(symbol, epoch, _high, _low, _open, _close)
        VALUES(?, ?, ?, ?, ?, ?); """,
        ( "BTC/USD", datetime.timestamp(
            entry.timestamp
         ), entry.high, entry.low,
            entry.open, entry.close     )
    )

connection.commit()
connection.close()