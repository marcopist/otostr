"""Main module."""
import os
from pathlib import Path

from otostr.unit import Unit
from otostr.suite import Suite

def profile(suite: Suite):
    cwd = Path(os.getcwd())
    def prof(frame, event, arg):
        """Profile function."""
        if event == "call":
            f_location = frame.f_globals["__name__"]
            f_file = frame.f_code.co_filename
            f_name = frame.f_code.co_name

            if (
                f_file[0] == "<"
                or cwd not in Path(f_file).parents
                or "/otostr/otostr" in f_file
                or "<lambda>" in f_name
                or "venv" in f_file
            ):
                #print(f_file, "is not a relative path")
                return prof
            
            if "<module>" in f_name:
                return prof
            
            f_fname = f_location + "." + f_name
            f_args = {k:v for k, v in frame.f_locals.items() if k in frame.f_code.co_varnames[:frame.f_code.co_argcount]}
            f_state = {k:v for k, v in frame.f_globals.items() if k in frame.f_code.co_names}

            print(">>> [OTOSTR]: FOUND UNIT:", f_file, f_location, f_name)
            suite.add_unit(Unit(f_fname, f_location, f_name, f_file, f_args, f_state))
        
    return prof