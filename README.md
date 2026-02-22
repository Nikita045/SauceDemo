Overview

This repository contains a scalable and maintainable end-to-end UI automation framework built using:

Python 3.10+

Pytest

Playwright (Sync API)

Page Object Model (POM)

GitHub Actions (CI/CD Integration)

The framework automates critical business flows of the SauceDemo web application, validating both positive and negative scenarios across authentication, cart, and checkout modules.

The design emphasizes:

Maintainability

Reusability

Stability

CI readiness

Interview-grade automation standards

🏗 Architecture & Design Principles
🔹 Design Pattern: Page Object Model (POM)

Each page is abstracted into a dedicated class encapsulating:

Page locators

Page actions

Business-specific operations

This ensures:

Reduced duplication

Centralized locator maintenance

Clear separation of test logic and UI interaction

🔹 Folder Structure
SauceDemo/
│
├── .github/workflows/        # CI configuration
│   └── saucedemo.yml
│
├── POM/                      # Page Object classes
│   ├── SauceDemo_Login_Page.py
│   ├── SauceDemo_Dashboard.py
│   └── SauceDemo_Checkout.py
│
├── Authentication Module/    # Login test scenarios
├── Cart Module/              # Cart validation scenarios
├── Checkout Module/          # Checkout flows (positive & negative)
│
├── reports/                  # HTML execution reports
│
├── conftest.py               # Shared fixtures
├── pytest.ini                # Pytest configuration
├── requirements.txt
└── README.md
🧩 Key Automation Features
✅ Test Coverage
Authentication

Valid login

Invalid login

Error validation

Cart

Add single/multiple products

Remove items

Cart navigation

Checkout

Complete purchase flow

Form validation (mandatory field checks)

Continue shopping scenario

✅ Engineering Best Practices Implemented

Reusable pytest fixtures

Stable locators using data-test attributes

Clear separation of concerns

Parameterized negative validation tests

HTML reporting with pytest-html

Headless execution support

CI pipeline integration

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone <repository-url>
cd SauceDemo
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
3️⃣ Install Dependencies
pip install -r requirements.txt
playwright install
▶️ Test Execution
Run Entire Suite
pytest -v --browser chromium
Run in Headless Mode
pytest -v --browser chromium --headed=false
Generate HTML Report
pytest -v --browser chromium --html=reports/report.html --self-contained-html
🔄 Continuous Integration (CI/CD)

This project is integrated with GitHub Actions to enable automated execution on push events.

Pipeline includes:

Repository checkout

Python setup

Dependency installation

Playwright browser installation

Test execution

HTML report artifact upload

Workflow file:

.github/workflows/saucedemo.yml
📊 Why This Framework Design?

This framework was designed to simulate real-world automation standards:

Modular test design

CI-ready structure

Extensible architecture

Easy migration to parallel execution

Ready for Docker/containerization

It can be easily extended to:

Multi-environment support

Data-driven testing

API test integration

Parallel test execution

🚀 Potential Enhancements

Parallel execution using pytest-xdist

Environment configuration management

Docker-based execution

Logging framework integration

API + UI hybrid framework

👩‍💻 Author

Nikita Kataria
QA Automation Engineer
