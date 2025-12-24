Welcome to my website checker.

This is a simple Python Automation side project. It simply checks for website status whether they are UP or DOWN as well as logging responses time and record results.

Some of its features are:
HTTP status monitoring
Response time management
Logging to file
Check interval (configurable)

To setup:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

To run (MacOS specific):
python3 src/checker.py