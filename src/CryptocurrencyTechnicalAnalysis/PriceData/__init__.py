#!/bin/python3
from alpaca.trading.client  import TradingClient
from alpaca.data.live       import CryptoDataStream
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests   import CryptoBarsRequest
from alpaca.data.timeframe  import TimeFrame
from pandas                 import read_sql_query as querysql
from datetime               import datetime
from datetime               import timedelta
from sqlite3                import connect



class HistoricPerformanceBars:
    def __init__( self, days: int=7,
                  database: str="/home/library/software/CryptocurrencyTechnicalAnalysis/finance.db"
    ):
        """ __  __ _             _       _         ____ _____ ____ 
           |  \/  (_)_ __  _   _| |_ ___| |_   _  | __ )_   _/ ___|
           | |\/| | | '_ \| | | | __/ _ \ | | | | |  _ \ | || |    
           | |  | | | | | | |_| | ||  __/ | |_| | | |_) || || |___ 
           |_|  |_|_|_| |_|\__,_|\__\___|_|\__, | |____/ |_| \____|
                                           |___/                   
            ____       _                ____               ____        _        
           |  _ \ _ __(_) ___ ___      | __ )  __ _ _ __  |  _ \  __ _| |_ __ _ 
           | |_) | '__| |/ __/ _ \_____|  _ \ / _` | '__| | | | |/ _` | __/ _` |
           |  __/| |  | | (_|  __/_____| |_) | (_| | |    | |_| | (_| | || (_| |
           |_|   |_|  |_|\___\___|     |____/ \__,_|_|    |____/ \__,_|\__\__,_|
        A database-population system for practicing data interpretation within a self-
        hosted environment.

            This tool does two things relating to the low-end side of data science; the
        building out of an in-house financial bar data file for keeping track of Bitcoin,
        as well as skim the most recent information and present it as a dataframe for
        further work down the line.

          -- Arguments:
            - days:     How many whole-days back tocollect data for.
            - database: Absolute filepath to an `sqlite3.db` file.
        """

        # Make database connection and cursor.
        self.database = connect(database)
        self.cursor = self.database\
                          .cursor()

        def date_counter(days):
            step, _list = 1, []
            while step <= days:
                _list.append(
                    datetime.now() - timedelta(days=step)
                ); step += 1
            return _list

        end = datetime.today()

        for day in date_counter(days):
            bar = CryptoHistoricalDataClient().get_crypto_bars(
                CryptoBarsRequest( symbol_or_symbols=["BTC/USD"],
                                   timeframe=TimeFrame.Minute,
                                   start=day,
                                   end=end)
            ); end = day; bar.df
        
            # Allow the results to be globally accessible.
            self.data = bar["BTC/USD"]

            # Write the information we're looking for to the database.
            # --Be sure to save our work ;)
            for entry in self.data:
                self.cursor.execute("""
                    INSERT OR IGNORE INTO historic_price_data(
                        symbol, epoch, _high, _low, _open, _close
                    )
                    VALUES( ?, ?, ?, ?, ?, ? ); """,
                    ( "BTC/USD", datetime.timestamp(
                        entry.timestamp
                     ), entry.high, entry.low,
                        entry.open, entry.close     )
                ); self.database.commit()

        # Populate a dataframe with the most recent data.
        self.dataframe = querysql("""
            SELECT * FROM historic_price_data
            ORDER BY epoch DESC
            LIMIT 120;""", self.database
        )
        
        self.database\
            .close()


class LiveTransactionLedger:
    def __init__( self, key, secret,
        database: str="/home/library/software/CryptocurrencyTechnicalAnalysis/finance.db"
    ):
        self.database = database

        # asynchronous object handler.
        async def _handler(data):
            db = connect(db)
            cursor = db.cursor()
            cursor.execute("""
                INSERT OR IGNORE INTO live_transaction_ledger(
                    symbol, epoch, _ask_price, _ask_size, 
                    _bid_price, _bid_size
                )
                VALUES( ?, ?, ?, ?, ?, ?);""",
                ("BTC/USD", datetime.timestamp(data.timestamp),
                data.ask_price, data.ask_size, data.bid_price, data.bid_size)
            ); db.commit(); db.close()
            

        stream = CryptoDataStream(key, secret)
        stream.subscribe_quotes( _handler,
                                 "BTC/USD" )
        stream.run()