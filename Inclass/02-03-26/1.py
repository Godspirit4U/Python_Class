''' Exercise 4 Q 5'''


class TermMarks:
    def __init__(self, term1, term2, term3):

        self.term1 = 0
        self.term2 = 0
        self.term3 = 0

        if term1 > 0:
            self.term1 = term1
        else:
            print("Term1 marks cannot be negative and initialised to 0\n.")

        if term2 > 0:
            self.term2 = term2
        else:
            print("Term2 marks cannot be negative and initialised to 0\n.")

        if term3 > 0:
            self.term3 = term3
        else:
            print("Term3 marks cannot be negative and initialised to 0\n.")

    def __str__(self):
        return f"\nMarks are\nTerm 1 : {self.term1}\nTerm 2 : {self.term2}\nTerm 3 : {self.term3}\n"

    def average(self):
        return f"Average: {(self.term1 + self.term1 + self.term1) / 3}"
    
    def maximum(self):
        if self.term1 >= self.term2 and self.term1 >= self.term3:
            return f"Maximum: {self.term1}\n"
        elif self.term2 >= self.term1 and self.term2 >= self.term3:
            return f"Maximum: {self.term2}\n"
        else:
            return f"Maximum: {self.term3}\n"


t1 = TermMarks(10, 30, 20)
print(t1)
print(t1.average())
print(t1.maximum())