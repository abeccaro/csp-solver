class SearchStats:
    """Class to store statistics of solver search.

    It contains:
    - time: search time
    - explored_sol: number of complete assignments explored
    - backtracks: number of backtracks
    """


    def __init__(self):
        self.time = 0
        self.explored_sol = 0
        self.backtracks = 0


    def __str__(self):
        return 'Search time: ' + str(round(self.time, 3)) + 's\nSolution explored: ' + str(self.explored_sol) + \
               '\nBacktracks: ' + str(self.backtracks)
