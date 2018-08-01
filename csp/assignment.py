from copy import deepcopy

class Assignment:

    assignments = {}


    def __len__(self):
        return len(self.assignments)

    def __str__(self):
        s = ''
        for var in self.assignments:
            s += var
            s += ' = '
            s += str(self.assignments[var])
            s += '\n'
        return s

    def __deepcopy__(self, memo):
        copy = Assignment()
        copy.assignments = deepcopy(self.assignments)
        return copy


    def assign(self, name, value):
        self.assignments[name] = value