from copy import deepcopy

class Assignment:

    def __init__(self, vars = []):
        self.assignments = {}
        self.domains = {}
        for v in vars:
            self.domains[v.name] = v.domain


    def __len__(self):
        return len(self.assignments)

    def __str__(self):
        s = ''
        for var in self.assignments:
            s += var + ' = ' + str(self.assignments[var]) + '\n'
        return s

    def __deepcopy__(self, memo):
        copy = Assignment()
        copy.assignments = deepcopy(self.assignments)
        copy.domains = deepcopy(self.domains)
        return copy


    def assign(self, name, value):
        self.assignments[name] = value
        self.update_domain(name, [value])

    def update_domain(self, name, domain):
        self.domains[name] = domain

    def remove_from_domain(self, name, value):
        self.domains[name].remove(value)