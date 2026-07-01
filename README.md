# Python API Testing Framework

A job-focused API test automation project built with **Python**, **pytest**, and **requests**.

This repository demonstrates how to create a clean and maintainable API automation framework for public REST endpoints using:
- pytest
- requests
- reusable API client design
- smoke and regression test suites
- shared fixtures with `conftest.py`
- HTML reporting
- GitHub Actions CI

## Project Purpose

This project was created as a portfolio repository for QA Automation / Software Test Engineer roles.

The goal is to demonstrate practical API testing skills that are directly relevant for industry work, including:
- validating REST API responses
- checking response structure and business data
- testing positive and negative scenarios
- separating reusable client logic from test logic
- integrating automated API tests into CI pipelines

## Tech Stack

- Python
- pytest
- requests
- pytest-html
- GitHub Actions

## API Under Test

This project uses **Fake Store API** as the application under test.

It is a public mock e-commerce API that provides realistic endpoints for:
- products
- categories
- carts

This makes it suitable for demonstrating API testing patterns in a portfolio-friendly project.

## Implemented Test Coverage

### Smoke Tests
- Get all products
- Validate non-empty product list
- Validate expected product response keys
- Get single product by ID
- Get all categories
- Validate non-empty category list
- Validate products returned by category

### Regression Tests
- Create cart with POST request
- Validate returned cart payload fields
- Validate returned user ID
- Validate products list in cart response
- Validate non-existing product handling
- Validate non-existing category handling

## Framework Features

- Reusable API client in `api/client.py`
- Test data separated into `test_data/`
- Shared pytest fixture via `conftest.py`
- Smoke and regression test separation
- Defensive validation for inconsistent fake API behavior
- HTML test reports via `pytest-html`
- GitHub Actions workflow for automated test execution

## Project Structure

```text
python-api-testing-framework/
├── .github/
│   └── workflows/
│       └── python-api-tests.yml
├── api/
│   └── client.py
├── test_data/
│   ├── carts.py
│   └── products.py
├── tests/
│   ├── regression/
│   │   ├── test_carts.py
│   │   └── test_negative_products.py
│   └── smoke/
│       ├── test_categories.py
│       └── test_products.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/anshi43/python-api-testing-framework.git
cd python-api-testing-framework
```

### 2. Create and activate a virtual environment

#### Windows PowerShell
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Run Tests

### Run the full suite
```bash
pytest
```

### Run smoke tests only
```bash
pytest tests/smoke
```

### Run regression tests only
```bash
pytest tests/regression
```

### Run a single test file
```bash
pytest tests/regression/test_carts.py
```

## HTML Reporting

This project uses `pytest-html` to generate a self-contained HTML report.

After running the test suite, the report is available at:

```text
reports/report.html
```

## CI Integration

This repository includes a GitHub Actions workflow that:
- checks out the repository
- sets up Python
- installs dependencies
- runs pytest
- uploads the HTML test report as an artifact

This demonstrates how automated API tests can be integrated into a continuous integration workflow.

## Why This Project Matters

This project is intended to demonstrate practical API testing skills for QA and test automation roles, especially:
- REST API validation using Python
- maintainable test framework structure
- smoke and regression suite design
- handling both positive and negative scenarios
- CI-ready automated testing

## Future Improvements

Possible next improvements for this repository:
- response schema validation
- test parameterization
- environment-based configuration
- logging improvements
- additional POST / PUT / DELETE scenarios

## Author

**Ankit Mavani**  
Berlin, Germany

- GitHub: https://github.com/anshi43
- LinkedIn: https://www.linkedin.com/in/ankitmavani/
- Email: mavaniankit09@gmail.com