class TechnicalIndicators:

    def __init__(self, dataframe):
        self.trends = self.Trends(dataframe)
        #rmeans = MeansReversion(dataframe)
        #moment = Momentum(dataframe)
        #volume = Volume(dataframe)

    class Trends:

        def __init__(self, dataframe):
            self.dataframe = dataframe
            self.RelativeStrengthIndex()
            self.MovingAverageConvergenceDivergence()

        def MovingAverageConvergenceDivergence(self):
            dataframe = self.dataframe

            # Calculate 12-period and 26-period exponential moving averages. 
            dataframe["EMA12"]  = dataframe["_close"].ewm(span=12, adjust=False).mean()
            dataframe["EMA26"]  = dataframe["_close"].ewm(span=26, adjust=False).mean()

            # Compare EMA12 to EMA26 and generate signal.
            dataframe["MACD"]   = dataframe["EMA12"] - dataframe["EMA26"]
            dataframe["Signal"] = dataframe["MACD"].ewm(span=9, adjust=False).mean()
            
            # Evaluate two most recent entries and trigger indicator.
            last_row, secondlast_row = dataframe.iloc[0], dataframe.iloc[1]

            # NOTE: Indicates `cross-under`.
            if secondlast_row["MACD"] > secondlast_row["Signal"] and last_row["MACD"] < last_row["Signal"]:
                self.MACD = False
            
            # NOTE: Indicates `cross-over`.
            elif secondlast_row["MACD"] < secondlast_row["Signal"] and last_row["MACD"] > last_row["Signal"]:
                self.MACD = True
            
            # NOTE: Indicates `no-cross`.
            else: self.MACD = None


        def RelativeStrengthIndex(self):
    
            # Update the dataframe to include a daily change.
            dataframe = self.dataframe
            dataframe["change"] = dataframe["_close"].diff()
            change = dataframe["change"]
            change.dropna(inplace=True)
    
            # Calculate the average upward and downward change.
            up, down = change.copy(), change.copy()
            up[up<0], down[down>0] = 0, 0
            average_up = up.rolling(3).mean()
            average_down = down.rolling(3).mean().abs()

    
            # Post indicator and trigger signals.
            RSI = 100 - (100 / ( 1 + (average_up / average_down)))
            RSI.dropna(inplace=True)
            self.RSI = RSI.iloc[0]
            if self.RSI > 70:   self.overbought, self.oversold = True, False
            elif self.RSI < 30: self.overbought, self.oversold = False, True
            else:               self.overbought, self.oversold = False, False


    class MeanReversion: pass
    class Momentum: pass
    class Volume: pass