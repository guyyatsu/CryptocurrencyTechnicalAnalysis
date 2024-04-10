from numpy import where as np_where
import pandas as pd


#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)


class TechnicalIndicators:

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.dataframe.set_index("epoch")
        self.SimpleMovingAverage()
        self.MovingAverageCrossover()
        self.MovingAverageConvergenceDivergence()
        self.RelativeStrengthIndex()


    def MovingAverageCrossover(self, _short=30, _long=60):
        self.SimpleMovingAverage(_short)
        self.SimpleMovingAverage(_long)
        dataframe = self.dataframe
        dataframe["MAC Signal"] = 0.0
        dataframe["MAC Signal"] = np_where(dataframe[f"{_short} Minute SMA"] > dataframe[f"{_long} Minute SMA"], 1.0, 0.0)
        dataframe["MAC Position"] = dataframe["MAC Signal"].diff()
        self.dataframe = dataframe


    def SimpleMovingAverage(self, window=3):
        """
        Calculate the rolling average for a series.
        Calling this without any arguments generates the Simple Moving Average.
        """

        dataframe = self.dataframe
        
        if window == 3: _type = ""
        else: _type = f"{window} Minute "

        dataframe[f"{_type}SMA"] = dataframe["_close"].rolling(window).mean()
        self.dataframe = dataframe


    def MovingAverageConvergenceDivergence(self):
        dataframe = self.dataframe[::-1]

        # Calculate 12-period and 26-period exponential moving averages. 
        dataframe["EMA12"]  = dataframe["_close"].ewm(span=12, adjust=False).mean()
        dataframe["EMA26"]  = dataframe["_close"].ewm(span=26, adjust=False).mean()

        # Compare EMA12 to EMA26 and generate signal.
        dataframe["MACD"]   = dataframe["EMA12"] - dataframe["EMA26"]
        dataframe["MACD Signal"] = dataframe["MACD"].ewm(span=9, adjust=False).mean()
        
        # Evaluate two most recent entries and trigger indicator.
        last_row, secondlast_row = dataframe.iloc[-1], dataframe.iloc[-2]


        # NOTE: Indicates `cross-under`.
        if secondlast_row["MACD"] > secondlast_row["MACD Signal"] and last_row["MACD"] < last_row["MACD Signal"]:
            self.macd_trigger = False
        
        # NOTE: Indicates `cross-over`.
        elif secondlast_row["MACD"] < secondlast_row["MACD Signal"] and last_row["MACD"] > last_row["MACD Signal"]:
            self.macd_trigger = True
        
        # NOTE: Indicates `no-cross`.
        else: self.macd_trigger = None

        self.dataframe = dataframe


    def RelativeStrengthIndex(self, window=3):

        # Update the dataframe to include a daily change.
        dataframe = self.dataframe[::-1]
        dataframe["change"] = dataframe["_close"].diff()
        change = dataframe["change"]

        # Calculate the average upward and downward change.
        up, down = change.copy(), change.copy()
        up[up<0], down[down>0] = 0, 0
        average_up = up.rolling(window).mean()
        average_down = down.rolling(window).mean().abs()

        # Post indicator and trigger signals.
        RSI = 100 - (100 / ( 1 + (average_up / average_down)))

        dataframe["RSI"] = RSI
        self.RSI = [session for session in RSI.iloc[0:]]
        if self.RSI[-1] > 70:   self.rsi_trigger = True
        elif self.RSI[-1] < 30: self.rsi_trigger = False
        else:                   self.rsi_trigger = None
        self.dataframe = dataframe


    def BollingerBands(self, window=20):
        dataframe = self.dataframe
        dataframe["Standard Deviation"] = dataframe["_close"].rolling(window=window).std()
        dataframe['Upper Bound'] = dataframe['SMA'] + 2 * dataframe['Standard Deviation']
        dataframe['Lower Bound'] = dataframe['SMA'] - 2 * dataframe['Standard Deviation']
        self.dataframe = dataframe