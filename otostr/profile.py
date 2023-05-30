"""Main module."""

from otostr.testcase import TestCase

def profile(modname, suite):
    def prof(frame, event, arg):
        """Profile function."""
        if event == "call":
            f_location = frame.f_globals["__name__"]
            if modname not in f_location:
                return
        
            f_name = frame.f_code.co_name
            if "<module>" == f_name:
                return
            
            f_fname = f_location + "." + f_name
            f_args = {k:v for k, v in frame.f_locals.items() if k in frame.f_code.co_varnames[:frame.f_code.co_argcount]}
            f_state = {k:v for k, v in frame.f_globals.items() if k in frame.f_code.co_names}

            suite.add_case(TestCase(f_location, f_name, f_args, f_state))
        
    return prof