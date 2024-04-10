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

    arguments.add_argument("-Lf", "--log-file", default=".log")
    arguments.add_argument("-Db", "--database", default="/tmp/finance.db")
    arguments.add_argument("-Hd", "--historic-data", action="store_true", default=False)
    arguments.add_argument("-Ti", "--technical-indicators", action="store_true", default=False)
    arguments.add_argument("-D", "--days", type=int, default=1)
    arguments.add_argument("-Ye", "--year-end",  type=int, default=default_start[0])
    arguments.add_argument("-Me", "--month-end", type=int, default=default_start[1])
    arguments.add_argument("-De", "--day-end",   type=int, default=default_start[2])

    arguments = arguments.parse_args()

    #HistoricPerformanceBars(days=int(arguments.days))

    dataframe = DataframeCuration(
        arguments.database_file,
    )

    indicators = TechnicalIndicators(dataframe)
    trends = indicators.trends