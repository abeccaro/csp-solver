from copy import deepcopy

class Assignment:

    assignments = {}


    def __len__(self):
        return len(self.assignments)

    def __str__(self):
        s = ''
        for a in self.assignments:
            s += a.name
            s += ' = '
            s += str(self.assignments[a])
            s += '\n'
        return s

    def __deepcopy__(self, memo):
        copy = Assignment()
        copy.assignments = deepcopy(self.assignments)
        return copy


    def assign(self, var, value):
        self.assignments[var] = value