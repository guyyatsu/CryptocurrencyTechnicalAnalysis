SELECT * FROM (
    SELECT * FROM historic_price_data
    ORDER BY epoch DESC
    LIMIT ?
) ORDER BY epoch ASC;
