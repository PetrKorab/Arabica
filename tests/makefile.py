import subprocess

# Variables
PYTHON = "python3.9"
TEST_FILES = ["arabica_freq_unit_test.py",
              "cappuccino_unit_test.py",
              "coffee_break_unit_test.py",
              "paper_graphs_unit_test.py"]  # Assuming you have a file named paper_graphs_unit_test.py

# Targets
def test():
    """Run unit tests."""
    print("Running tests...")
    for test_file in TEST_FILES:
        subprocess.run([PYTHON, "-m", "unittest", test_file])

def clean():
    """Clean up generated files."""
    print("Cleaning up...")
    # Add commands here to clean up generated files or directories

def lint():
    """Lint the code."""
    print("Linting the code...")
    subprocess.run(["flake8", "."])  # Assuming flake8 is installed

if __name__ == "__main__":
    test()
