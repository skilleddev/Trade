class MultidimensionalTransdimensionalSplitter(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2021, 6, 1) # Set Start Date
        self.setCash(150000)  # Set Strategy Cash
        # self.AddEquity("SPY", Resolution.Minute)


    def OnData(self, data):
        '''OnData event is the primary entry point for your algorithm.
        each new data point will be pumped
        Arguments: 
            data: Slice object keyed by symbol containing the stock data
        '''

        # if not self.Portfolio.Invested:
        #    self.SetHoldings("SPY", 1)
