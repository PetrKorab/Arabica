# Makefile for running tests and other tasks

# Variables
PYTHON := python3
TEST_FILE := test_arabica.py

.PHONY: test clean

test:
	@echo "Running tests..."
	$(PYTHON) -m unittest $(TEST_FILE)

clean:
	@echo "Cleaning up..."
	# Add commands here to clean up generated files or directories
