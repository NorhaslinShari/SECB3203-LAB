# SECB3203 Lab 1 - Python fundamentals and a reproducible project

Student: <NORHASLIN BINTI SHARI, A24CS0149>

## Setup
<USING VS CODE
- python -m venv .venv
- dir (to check if .venv is exist in right place)
- .\.venv\Scripts\python.exe -m pip install -r requirements.txt (i cannot run if using syntax in docs, so ask copilot what suitable command to put)
- .\.venv\Scripts\activate.bat (i activate later because i forgot to activate)
- .\.venv\Scripts\python.exe -m pip freeze > requirements-frozen.tx
- dir requirements-frozen.txt (to check if requirements-frozen.txt exist)>

## Run
<Write 
- python -m pytest
- ruff check src
- python src/env_check.py > results/environment_report.txt >

## What is in this repository
<src/ - basics.py,env_check.py
- tests/ - test_visible.py
- data/ - qc_records.csv
- results/ - .gitkeep
- .gitignore, AI_USE_LOG.md, pytest.ini, README.md,requirements-frozen.txt, requirements.txt >

## What is not committed, and why
<.venv/ folder contains (local virtual enviroment) which is can be recreated on another computer. Besides, results/folder is function to generetaed output files that can be recreated too when the project run.>
