# IDS706_python_template

# Build/Test Badge:
[![Python Template for IDS706](https://github.com/jordanandrewww/IDS706_python_template/actions/workflows/main.yml/badge.svg)](https://github.com/jordanandrewww/IDS706_python_template/actions/workflows/main.yml)

# Project Description

This project is my first setup for Data Engineering Systems. It demonstrates how to create a Python project skeleton following professional software development practices. This will serve as a template project that can be reused for future assignments.

This repository includes:

1. hello.py: a python script with example functions
2. test_hello.py: unit tests to validate the code
3. Makefile: a makefile for automation (installing dependencies, testing, linting, formatting, cleaning)
4. requirements.txt: file with necessary dependencies
5. A GitHub Actions workflow for continuous integration

# Setup Instructions

1. Clone the respository using git clone
2. Install the dependencies using make install

# Usage examples

Run the Python script:
python hello.py

Inside hello.py:
from hello import say_hello, add

print(say_hello("Jordan"))
print(add(2, 3))

Expected output:
Hello, Jordan, welcome to Data Engineering Systems (IDS 706)!
5

Run tests:
make test

Format code:
make format

Lint code:
make lint

Clean up environment:
make clean
