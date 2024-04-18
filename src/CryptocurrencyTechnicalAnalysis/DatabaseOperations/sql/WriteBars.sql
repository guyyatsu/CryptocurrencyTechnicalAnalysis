INSERT OR IGNORE INTO historic_price_data(
    symbol, epoch, _high, _low, _open, _close
) VALUES( ?, ?, ?, ?, ?, ? );
