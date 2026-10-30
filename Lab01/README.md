# SECB3203 Lab 1 - Python fundamentals and a reproducible project

Student: NORHASLIN BINTI SHARI, A24CS0149

## Setup
USING VS CODE
- python -m venv .venv
- dir 
- .\.venv\Scripts\python.exe -m pip install -r requirements.txt 
- .\.venv\Scripts\activate.bat 
- .\.venv\Scripts\python.exe -m pip freeze > requirements-frozen.tx
- dir requirements-frozen.txt

## Run
- python -m pytest
- ruff check src
- python src/env_check.py > results/environment_report.txt 

## What is in this repository
- src/ - basics.py,env_check.py
- tests/ - test_visible.py
- data/ - qc_records.csv
- results/ - .gitkeep, environement_report.txt
- .gitignore, AI_USE_LOG.md, pytest.ini, README.md,requirements-frozen.txt, requirements.txt

## What is not committed, and why
.venv/ folder because contains (local virtual enviroment) which can be recreated on another computer. Besides, results/folder is function to generetaed output files that can be recreated too when the project run.
