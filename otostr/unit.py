import contextlib
import sys, os
from unittest.mock import patch
import copy

@contextlib.contextmanager
def _nostdout():
    save_stdout = sys.stdout
    sys.stdout = open(os.devnull, "w")
    yield
    sys.stdout = save_stdout

class Unit:
    def __init__(self, fullname, module, name, filename, args, state):
        self.fullname = fullname
        self.module = module
        self.name = name
        self.filename = filename
        self.args = copy.deepcopy(args)
        self.state = copy.deepcopy(state)
        self.ran = False
        
    def run(self):
        print(">>> [OTOSTR]: RUNNING UNIT", self.filename, self.name, self.args, self.state)
        method = getattr(sys.modules[self.module], self.name)
        mock_state = patch(self.module, self.state)
        with mock_state:
            with _nostdout():
                self.result = method(**self.args)
            self.altstate = {k: getattr(sys.modules[self.module], k) for k in self.state.keys()}
        self.ran = True
        
    
    def __str__(self):
        return f"""
        name = {self.name}
        state = {self.state}
        args = {self.args}
        return = {self.result}
        altstate = {self.altstate}
        """