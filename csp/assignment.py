class Assignment:

    assignments = {}


    def __len__(self):
        return len(assignments)

    def assign(self, var, value):
        assignments[var] = value