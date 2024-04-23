#!/bin/python3
"""
"""

from PriceData          import HistoricPerformanceBars
from DatabaseOperations import DataframeCuration
from TechnicalAnalysis  import TechnicalIndicators
from decouple           import config
from logging            import basicConfig
from logging            import INFO
from datetime           import datetime
from datetime           import timedelta
from argparse           import ArgumentParser


if __name__ == "__main__":

    arguments = ArgumentParser()

    arguments.add_argument("-Lf", "--log-file", default=default_log)
    arguments.add_argument("-Db", "--database", default=default_db)
    arguments.add_argument("-Hd", "--historic-data", action="store_true", default=False)
    arguments.add_argument("-Ti", "--technical-indicators", action="store_true", default=False)
    arguments.add_argument("-D", "--days", type=int, default=1)
    arguments.add_argument("-Ye", "--year-end",  type=int, default=default_start[0])
    arguments.add_argument("-Me", "--month-end", type=int, default=default_start[1])
    arguments.add_argument("-De", "--day-end",   type=int, default=default_start[2])

    args = arguments.parse_args()


basicConfig(filename=args.log_file, level=INFO)

if args.historic_data is True:
    days_end = datetime(args.year_end, args.month_end, args.day_end)
    try: HistoricPerformanceBars(days=args.days, end=days_end)
    except KeyboardInterrupt: exit()

if args.technical_indicators is True:
    TechnicalIndicators(DataframeCuration(default_db))