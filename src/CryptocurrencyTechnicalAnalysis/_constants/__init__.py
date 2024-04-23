#!/bin/python3
from datetime import timedelta, datetime
from Lab93CryptographyAPI import CryptogramAPI


cryptogram = CryptogramAPI()
SHA256   = lambda string: cryptogram.sha_256(string)
BUILDKEY = lambda string: cryptogram.build_key(string)
ENCRYPT = lambda target, phrase: cryptogram.encryption(target, phrase)
DECRYPT = lambda target, phrase: cryptogram.decryption(target, phrase)


# List out the Year Month and Day for todays date as a default fallback.
default_start = [
    int(number) for number in \
        datetime.strftime( datetime.now(),
                           "%Y %-m %-d"     )\
                .split()
]

default_db = "finance.db"
default_log = ".log"

def date_counter(days, date):
    """
    Give a list of consecutive datetime objects
    going backwards from the current date.
    """
    step, _list = 1, []
    while step <= days:
        _list.append(
            date - timedelta(days=step)
        ); step += 1
    return _list
