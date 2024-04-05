from sqlite3 import connect
from pandas import read_sql_query as querysql


def WriteHistoricBars(database, symbol, timestamp, _high, _low, _open, _close):
    cursor = database.cursor()

    query = """
    INSERT OR IGNORE INTO historic_price_data(
        symbol, epoch, _high, _low, _open, _close
    )
    VALUES(
        ?, ?, ?, ?, ?, ?
    );
    """
    cursor.execute(
        query, (symbol, timestamp, _high, _low, _open, _close)
    )
    database.commit()

def DataframeCuration(database, _limit: int = 100):
    """ Dataset Curation
    With a back-log of data secured, we construct a pandas dataframe from 
    the top &number of most recent bars collected and make it available
    as a member of HistoricPerformanceBars.

    Now that we've caught up on any missed information and skimmed what we
    need, we can finally close the database connection and call it a day.
    """
    database = connect(database)
    dataframe = querysql("SELECT * FROM historic_price_data ORDER BY epoch DESC LIMIT ?;", database,
        params=[_limit]
    ); database.close()

    return dataframe
