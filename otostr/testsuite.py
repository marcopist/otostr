from otostr.testcase import TestCase

class TestSuite:
    def __init__(self):
        self.cases = []
    
    def add_case(self, case):
        self.cases.append(case)

    def __str__(self):
        return "\n\n".join(map(str, self.cases))