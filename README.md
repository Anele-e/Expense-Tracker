# Expense-Tracker

## Project URL for roadmap.sh project
https://roadmap.sh/projects/expense-tracker

## Setup

1. Clone repository:

    ```bash
    git clone https://github.com/Anele-e/Expense-Tracker.git

2. Navigate to the project directory:


3. Install the 'virtualenv' package in python if you do not have one.

    ```bash
    pip install virtualenv
    ```

4. Create a virtual environment. 'venv' is an optional name

    ```bash
    virtualenv venv
    ```

    Python 3.3 or newer 

    ```bash
    python -m venv venv
    ```
5. Activate the virtual environment

    On Powershell
    ```bash
     .\venv\Scripts\Activate.ps1

    ```
    On Unix or MacOS:

    ```bash
     source venv\Scripts\activate

    ```

## To run program

In the command line/Terminal run the command below with your github username

1. To list all expenses
```bash
python expense_tracker.py list

```

2. To delete expense
```bash
python expanse_tracker.py delete --id <id_number>
```



