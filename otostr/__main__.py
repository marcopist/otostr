import runpy, sys
from otostr.profile import profile

suite = []

# Make a CLI which takes a file path and runs it using runpy.run_path
# with a custom profile function which adds the TestCase to the suite.

if __name__ == "__main__":
    target = sys.argv[1]
    sys.setprofile(profile(suite))
    runpy.run_path(target)
    print(suite[0])
