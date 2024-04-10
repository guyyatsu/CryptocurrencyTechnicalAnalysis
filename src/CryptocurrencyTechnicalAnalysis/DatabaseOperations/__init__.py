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

def DataframeCuration(database, _limit: int = 360):
    database = connect(database)
    query = """
        SELECT * FROM (
            SELECT * FROM historic_price_data
            ORDER BY epoch DESC
            LIMIT ?
        ) ORDER BY epoch ASC;
    """
    dataframe = querysql(
        query,
        database,
        params=[_limit]
    ); database.close()
    return dataframe
