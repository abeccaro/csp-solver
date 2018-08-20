class SearchStatistics:
    """Class that stores statistics about a solver search.

    It keeps track of:
    - explored: number of explored solutions (complete)
    - backtracks: number of backtracks
    - time: search time
    """

    def __init__(self):
        self.explored = 0
        self.backtracks = 0
        self.time = 0


    def __str__(self):
        s = '\nExplored solutions: ' + str(self.explored)
        s += '\nBacktracks: ' + str(self.backtracks)
        s += '\nSearch time: ' + str(round(self.time, 3)) + 's'

        return s
