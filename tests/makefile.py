import subprocess

PYTHON = "python3.9"
TEST_FILES = ["arabica_freq_unit_test.py",
              "cappuccino_unit_test.py",
              "coffee_break_unit_test.py",
              "paper_graphs.py"]

def test():
    """Run unit tests."""
    print("Running tests...")
    for test_file in TEST_FILES:
        subprocess.run([PYTHON, "-m", "unittest", test_file])

def clean():
    """Clean up generated files."""
    print("Cleaning up...")


def lint():
    """Lint the code."""
    print("Linting the code...")
    subprocess.run(["flake8", "."]) 

if __name__ == "__main__":
    test()
