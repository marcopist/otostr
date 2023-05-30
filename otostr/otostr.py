"""Main module."""

class TestCase:
    def __init__(self, name, args, state):
        self.name = name
        self.args = args
        self.state = state


class TestSuite:
    def __init__(self):
        self.cases = []
    
    def add_case(self, case):
        self.cases.append(case)


def profile_farm(modname, collector):
    def profile(frame, event, arg):
        """Profile function."""
        if event == "call":
            f_location = frame.f_globals["__name__"]
            if modname not in f_location:
                return
            f_name = frame.f_code.co_name
            f_fname = f_location + "." + f_name
            f_args = {k:v for k, v in frame.f_locals.items() if k in frame.f_code.co_varnames[:frame.f_code.co_argcount]}
            f_state = {k:v for k, v in frame.f_globals.items() if k in frame.f_code.co_names}

            collector.add_case(TestCase(f_fname, f_args, f_state))
        
    return profile