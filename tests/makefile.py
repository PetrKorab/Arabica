# Makefile for running tests and other tasks

# Variables
PYTHON := python3.9
TEST_FILE := arabica_freq_unit_test.py

.PHONY: test clean

test:
	@echo "Running tests..."
	$(PYTHON) -m unittest $(TEST_FILE)

clean:
	@echo "Cleaning up..."
	# Add commands here to clean up generated files or directories
