# Contributing to Sansam

Thank you for your interest in contributing to Sansam! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/OurCompiler.git
   cd OurCompiler
   ```
3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Development Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Making Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes
3. Write or update tests
4. Run tests:
   ```bash
   python -m pytest tests/
   ```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Comment complex logic

## Commit Messages

- Use clear, descriptive commit messages
- Start with a verb in present tense
- Example: "Add support for array operations"

## Pull Requests

1. Push your changes to your fork
2. Create a Pull Request to the `master` branch
3. Describe your changes in detail
4. Link any related issues

## Running Tests

```bash
python -m pytest tests/
```

## Building Documentation

```bash
cd docs
make html
```

## Questions or Need Help?

Open an issue or reach out to the maintainers.

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).
