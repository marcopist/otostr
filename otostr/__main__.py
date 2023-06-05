import runpy, sys
from otostr.profile import profile
from otostr.suite import Suite
import sys, os, contextlib

@contextlib.contextmanager
def _nostdout():
    save_stdout = sys.stdout
    sys.stdout = open(os.devnull, "w")
    yield
    sys.stdout = save_stdout

suite = Suite()

# Make a CLI which takes a file path and runs it using runpy.run_path
# with a custom profile function which adds the TestCase to the suite.

if __name__ == "__main__":
    target = sys.argv[1]
    sys.setprofile(profile(suite))
    runpy.run_path(target)
    sys.setprofile(None)

    # fst = suite.allunits[0]
    # fst.run()
    # print(fst)
