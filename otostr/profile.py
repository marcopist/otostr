"""Main module."""
import os
from pathlib import Path

from otostr.unit import Unit

def profile(suite):
    #cwd = Path(os.getcwd())
    def prof(frame, event, arg):
        """Profile function."""
        if event == "call":
            f_location = frame.f_globals["__name__"]
            f_file = frame.f_code.co_filename
            if f_file[0] == "<":
                return
        
            f_name = frame.f_code.co_name
            if "<module>" == f_name:
                return
            
            f_fname = f_location + "." + f_name
            f_args = {k:v for k, v in frame.f_locals.items() if k in frame.f_code.co_varnames[:frame.f_code.co_argcount]}
            f_state = {k:v for k, v in frame.f_globals.items() if k in frame.f_code.co_names}

            suite.append(Unit(f_location, f_name, f_args, f_state))
        
    return prof