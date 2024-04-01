#!/bin/python3
from alpaca.trading.client  import TradingClient
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests   import CryptoBarsRequest
from alpaca.data.timeframe  import TimeFrame
from pandas                 import read_sql_query as querysql
from datetime               import datetime
from datetime               import timedelta
from sqlite3                import connect



class HistoricPerformanceBars:
    def __init__( self, days: int=3,
                  database: str="/home/library/software/CryptocurrencyTechnicalAnalysis/finance.db"
    ):

        # Make database connection and cursor.
        self.database = connect(database)
        self.cursor = self.database\
                          .cursor()
        yestermorrow = datetime.now() - timedelta(days=days)
        bar = CryptoHistoricalDataClient().get_crypto_bars(
            CryptoBarsRequest( symbol_or_symbols=["BTC/USD"],
                               timeframe=TimeFrame.Minute,
                               start=yestermorrow,
                               end=datetime.now())
        ); bar.df
        self.data = bar["BTC/USD"]

        for entry in self.data:
            cursor.execute("""
                INSERT OR IGNORE INTO historic_price_data(
                    symbol, epoch, _high, _low, _open, _close
                )
                VALUES( ?, ?, ?, ?, ?, ? ); """,
                ( "BTC/USD", datetime.timestamp(
                    entry.timestamp
                 ), entry.high, entry.low,
                    entry.open, entry.close     )
            ); connection.commit()

dataframe = querysql("""
    SELECT * FROM historic_price_data
    ORDER BY epoch DESC
    LIMIT 100;""", connection
)


connection.commit()
connection.close()
