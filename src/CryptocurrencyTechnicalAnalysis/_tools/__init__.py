#!/bin/python3


from datetime import timedelta


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

