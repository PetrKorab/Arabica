import subprocess

# Variables
PYTHON = "python3.9"
TEST_FILE = "test_arabica.py"

# Targets
def test():
    """Run unit tests."""
    print("Running tests...")
    subprocess.run([PYTHON, "-m", "unittest", TEST_FILE])

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
