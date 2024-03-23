import subprocess

# Variables
PYTHON = "python3.9"
TEST_FILE_1 = "arabica_freq_unit_test.py"
TEST_FILE_2 = "cappuccino_unit_test.py"
TEST_FILE_3 = "coffee_break_unit_test.py"
TEST_FILE_4 = "paper_graphs.py"


paper_graphs.py


# Targets
def test():
    """Run unit tests."""
    print("Running tests...")
    subprocess.run([PYTHON, "-m", "unittest", TEST_FILE_1])
    subprocess.run([PYTHON, "-m", "unittest", TEST_FILE_2])
    subprocess.run([PYTHON, "-m", "unittest", TEST_FILE_3])
    subprocess.run([PYTHON, "-m", "unittest", TEST_FILE_4])


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
