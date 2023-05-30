import sys
from unittest.mock import patch
import copy

class TestCase:
    def __init__(self, module, name, args, state):
        self.module = module
        self.name = name
        self.args = args
        self.state = state
        print(self.module)

    def run(self):
        print(self.state)
        method = getattr(sys.modules[self.module], self.name)
        
        with patch.multiple(self.module, **self.state) as values:
            self.result = method(**self.args)
            self.altstate = values

        for key, value in self.altstate.items():
            if self.state[key] != value:
                print(f"Detected change in state: {key} = {value}, was {self.state[key]}")
        
    
    def __str__(self):
        return f"""
        name = {self.name}
        state = {self.state}
        args = {self.args}
        """