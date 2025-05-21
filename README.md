***Behavior-Driven Test Automation for DS Algo Portal -https://dsportalapp.herokuapp.com/***


 ***Overview***
 
 This project uses Behave (a BDD testing framework for Python) to automate and validate the login functionality of the DS Algo Portal. All test scenarios are written in plain English (Gherkin language), making it beginner-friendly and easily understandable by non-developers too.
Whether you're new to test automation or practicing for your next coding interview, this project helps you understand how to use BDD to ensure reliable access to data structures and algorithms practice portals.

***Setup Instructions***
1. Clone the repository:
  git clone https://github.com/mayababuji/DSALGOBDD.git
  cd DSALGOBDD
2. Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies:
  pip install -r requirements.txt

***How to Run Tests***

1. Run all BDD tests:
   behave
   
2. Run specific feature:
   behave features/<feature_name>.feature
  
***Dependencies***
   Python 3.x

   Behave

   Selenium (for browser automation)

   Webdriver (e.g., ChromeDriver or GeckoDriver)

```markdown
##  Project Structure
DSALGOBDD/
│
├── features/
│   ├── login.feature         # Gherkin scenarios for login
│   ├── steps/
│   │   └── login_steps.py    # Step definitions in Python
│   └── environment.py        # Optional hooks (before/after scenarios)
│
├── requirements.txt          # Python dependencies
└── README.md                 # You are here!


## 📚 Helpful Resources

- 📖 [Behave Official Docs](https://behave.readthedocs.io/)
- 🌐 [Selenium Python Docs](https://selenium-python.readthedocs.io/)




