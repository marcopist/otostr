from typing import List
from otostr.unit import Unit

# UNIT_TEMPLATE = '''
# @pyest.mark.parametrize(
#     "args,state,expected",
#     [
#         {{tuple(unit.args,unit.state,unit.result}}
#     ]
# )
# @unittest.mock.patch(
#     unit.module
# )
# def test_{{unit.name}}("mock_module,args,state,expected"):
#     mock_module = state
#     actual = {{unit.name}}(**args)
#     assert actual == expected
# '''


def to_test_def(group: List[Unit]):
    [unit.run() for unit in group if not unit.ran]


class Suite:
    def __init__(self):
        self.groups = {}
        self.allunits = []
    
    def add_unit(self, unit):
        file = unit.module.replace(".", "/")
        name = unit.name
        self.allunits.append(unit)
        if file not in self.groups:
            self.groups[file] = {
                name: [unit]
            }
        elif name not in self.groups[file]:
            self.groups[file].update(
                {
                    name: [unit]
                }
            )
        else:
            self.groups[file][name].append(unit)

    def pytest_unit(self, group):
        for unit in group:
            unit.run()
    

