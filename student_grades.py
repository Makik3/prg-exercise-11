from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        a = self.scores[index]  # 91
        if a > 89:
            return "A"
        elif 90 > a > 79:
            return "B"
        elif 80 > a > 69:
            return "C"
        elif 70 > a > 59:
            return "D"
        elif 60 > a > 49:
            return "E"
        else:
            return "F"

    def find(self, konkretni_pocet_bodu):
        seznam = []
        for i in range(len(self.scores)):   # self.scores jakoby je ten seznam [85, 42, 91, 67, 50, 73, 100, 38, 58]
            if self.scores[i] == konkretni_pocet_bodu:
                seznam.append(i)
        return seznam   # vrátí seznam indexů studentů, kteří měli určitý počet bodů, např.: [6]

    def get_sorted(self):
        seznam_cisel = list(self.scores)   # vytvářím lokální kopii seznamu, aby self.scores zůstalo beze změny
        for j in range(len(seznam_cisel)):
            for i in range(1, len(seznam_cisel)):
                if seznam_cisel[i] < seznam_cisel[i - 1]:
                    seznam_cisel[i], seznam_cisel[i - 1] = seznam_cisel[i - 1], seznam_cisel[i]
        return seznam_cisel

def main(self):
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])  # toto je objekt
    pocet_studentu_co_psalo_test = results.count()
    for i in range(0, len(results)):
        print(f"Student{i}: {results.get_by_index(i)} points - {results.get_grade(i)}")  # Student 0: 85 points – B
    print(f"Indexy studentů, kteří měli plný počet bodů: {results.find(100)}")
    print(f"Seřazené výsledky od nejhoršího po nejlepšího: {results.get_sorted()}")

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())












if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]

    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)

    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []

    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny

    print(main())