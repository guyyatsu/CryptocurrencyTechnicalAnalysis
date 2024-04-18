from sqlite3 import connect
from pandas import read_sql_query as querysql
from _tools import command_subdirectory

command_subdirectory = f'{"/".join( __file__.split("/")[0:-1])}/sql'


def CreateDatabase(database):
  
    cursor = database.cursor()

    with open(f"{command_subdirectory}/CreateDatabase.sql", "r") as sql:
        cursor.executescript(sql.read())
        database.commit()
        del cursor


"""
def ValidateUserCredentials(database, userpass):
    cursor = database.cursor()
    with open(f"{command_subdirectory}/ValidateUser.sql", "r") as sql:
        cursor.executescript(sql.read(), userpass)
"""    
        


def WriteHistoricBars(database, symbol, timestamp, _high, _low, _open, _close):

    cursor = database.cursor()

    with open(f"{command_subdirectory}/WriteBars.sql") as sql:
        cursor.executescript( sql.read(),
                              ( symbol, timestamp,
                                _high, _low, _open, _close ) )

        database.commit(); del cursor


def DataframeCuration(database, _limit: int = 360):

    database = connect(database)

    with open(f"{command_subdirectory}/CollectBars.sql") as sql:
        dataframe = querysql(
            sql,
            database,
            params=[_limit]
        )

        database.close()
        return dataframe
