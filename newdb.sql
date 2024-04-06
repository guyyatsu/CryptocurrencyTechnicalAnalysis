CREATE TABLE historic_price_data(  
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    symbol TEXT,
    epoch TIMESTAMP UNIQUE,
    _high REAL,
    _low REAL,
    _open REAL,
    _close REAL
);