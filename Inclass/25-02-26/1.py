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
        return f"Marks are\nTerm 1 : {self.term1}\nTerm 2 : {self.term2}\nTerm 3 : {self.term3}\n"
    

t1 = TermMarks(10, 30, 20)
print(t1)
# t2 = TermMarks()
# print(t2)
