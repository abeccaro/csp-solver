from enum import Enum

class Operator(Enum):
    eq = "="
    ne = "!="
    lt = "<"
    le = "<="
    gt = ">"
    ge = ">="
    plus = "+"
    minus = "-"
    
    def is_comparison_op(self):
        """Checks if this operator is a comparison operator.
        
        :return: True if it's a comparison operator, False otherwise
        :rtype: bool
        """
        return self.value in ["=", "!=", "<", "<=", ">", ">="]
    
    def is_arithmetic_op(self):
        """Checks if this operator is an arithmetic operator.
        
        :return: True if it's an arithmetic operator, False otherwise
        :rtype: bool
        """
        return self.value in ["+", "-"]
    
    def reverse(self):
        """Transforms this operator in its opposite."""
        if self.value == "=":
            self.values = "!="
        elif self.value == "!=":
            self.values = "="
        elif self.value == "<":
            self.values = ">="
        elif self.value == "<=":
            self.values = ">"
        elif self.value == ">":
            self.values = "<="
        elif self.value == ">=":
            self.values = "<"
        elif self.value == "+":
            self.values = "-"
        elif self.value == "-":
            self.values = "+"
