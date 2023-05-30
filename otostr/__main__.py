import runpy, sys
from otostr.profile import profile
from otostr.testsuite import TestSuite

suite = TestSuite()
sys.setprofile(profile("ignore", suite))
# Make a CLI which takes a file path and runs it using runpy.run_path
# with a custom profile function which adds the TestCase to the suite.

if __name__ == "__main__":
    runpy.run_path(sys.argv[1])
    print(suite.cases[0].run())
