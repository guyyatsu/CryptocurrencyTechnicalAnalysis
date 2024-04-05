#!/bin/python3
"""
"""


""" Third-Party Imports """
from alpaca.trading.client  import TradingClient
from alpaca.data.live       import CryptoDataStream
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests   import CryptoBarsRequest
from alpaca.data.timeframe  import TimeFrame

""" In-House Imports """
from DatabaseOperations     import WriteHistoricBars

""" Built-In Imports """
from sqlite3                import connect
from datetime               import datetime
from datetime               import timedelta
from logging                import getLogger
from time                   import sleep


timestamp = lambda: datetime.timestamp(datetime.now())
default_db = "/home/library/software/CryptocurrencyTechnicalAnalysis/finance.db"


def date_counter(days):
    """
    Give a list of consecutive datetime objects
    going backwards from the current date.
    """
    step, _list = 1, []
    while step <= days:
        _list.append(
            datetime.now() - timedelta(days=step)
        ); step += 1
    return _list


class HistoricPerformanceBars:
    def __init__( self,
        days: int=7,
        symbol: str="BTC/USD",
        database: str=default_db,
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

        ''' Historic Data Request
        The Chunk-Request Loop consists of two iterative actions nested
        one within the other: for every *day we request all the minute-bars
        for that day, then for every minute within that day we write the
        symbol name, timestamp, high, low, open, and close to the HPD table
        within the designated SQLite3 datbase file.
        
        To get started with iterating day-by-day first we establish today
        as the ending point; then request up to today - 1, conduct our db
        transactions, then replace the end with the current start and repeat
        the process on the day before until no more days have been counted out
        for us by the day_counter function.
        '''
        # Delimiter for buffering our requests.
        end = datetime.today()
        database = connect(database)

        # Iterative chunk-collection.
        for day in date_counter(days):

            # Formulate data request for the current range of dates.
            bar = CryptoHistoricalDataClient().get_crypto_bars(
                CryptoBarsRequest( symbol_or_symbols=[symbol],
                                   timeframe=TimeFrame.Minute,
                                   start=day,
                                   end=end)
            )

            # Iterate through members of the day-chunk.
            for entry in bar[symbol]: WriteHistoricBars( database,
                                                         symbol,
                                                         datetime.timestamp(
                                                             entry.timestamp
                                                         ),
                                                         entry.high, entry.low,
                                                         entry.open, entry.close )
            # Increment the step.
            end = day
        database.close()


class LiveTransactionLedger:
    def __init__( self, key, secret,
        database: str="/home/library/software/CryptocurrencyTechnicalAnalysis/finance.db"
    ):
        self.database = database

        # asynchronous object handler.
        async def _handler(data):
            db = connect(self.database)
            cursor = db.cursor()
            cursor.execute("""
                INSERT OR IGNORE INTO live_transaction_ledger(
                    symbol, epoch, _ask_price, _ask_size, 
                    _bid_price, _bid_size
                )
                VALUES( ?, ?, ?, ?, ?, ?);""",
                ("BTC/USD", datetime.timestamp(data.timestamp),
                data.ask_price, data.ask_size, data.bid_price, data.bid_size)
            ); db.commit(); db.close(); sleep(.5)
            

        stream = CryptoDataStream(key, secret)
        stream.subscribe_quotes( _handler,
                                 "BTC/USD" )
        stream.run()