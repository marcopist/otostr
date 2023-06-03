import sys
from unittest.mock import patch
import copy


class Unit:
    def __init__(self, module, name, args, state):
        self.module = module
        self.name = name
        self.args = copy.deepcopy(args)
        self.state = copy.deepcopy(state)
        

    def _run(self):
        print("\n\n Running test case:")
        method = getattr(sys.modules[self.module], self.name)
        mock_state = patch(self.module, self.state)
        with mock_state:
            self.result = method(**self.args)
            self.altstate = {k: getattr(sys.modules[self.module], k) for k in self.state.keys()}
        
    
    def __str__(self):
        self._run()
        return f"""
        name = {self.name}
        state = {self.state}
        args = {self.args}
        return = {self.result}
        altstate = {self.altstate}
        """