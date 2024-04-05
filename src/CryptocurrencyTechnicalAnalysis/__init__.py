#!/bin/python3
"""
"""

from PriceData          import HistoricPerformanceBars
from PriceData          import LiveTransactionLedger
from DatabaseOperations import DataframeCuration
from TechnicalAnalysis  import TechnicalIndicators
from argparse           import ArgumentParser
from decouple           import config


if __name__ == "__main__":

    arguments = ArgumentParser()

    ''' Common Arguments. '''
    arguments.add_argument("-Db", "--database-file",
        default="/home/library/software/CryptocurrencyTechnicalAnalysis/finance.db"
    )

    arguments.add_argument( "-D",  "--days",
        default=7, help=(
            "Set the number of days back to pull data on."
        )
    )

    arguments.add_argument( "-L",  "--logging",
        action="store_true", help=(
            "Enable logging for better runtime tracing."
        )
    )

    arguments.add_argument( "-Lf", "--log-file",
        default="/dev/null", help=(
            f"Specify a filepath for logging to a file.  "
            f"Defaults to `/dev/null`."
        )
    )


    arguments.add_argument("-LT", "--live-transactions", action="store_true", default=False)

    arguments = arguments.parse_args()

    #HistoricPerformanceBars(days=int(arguments.days))

    dataframe = DataframeCuration(
        arguments.database_file,
    )

    indicators = TechnicalIndicators(dataframe)
    trends = indicators.trends