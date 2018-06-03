import sys

if hasattr(sys, 'real_prefix'):
  print('yay')
else:
  print('Not running in virtual environment')
  print('Run "./.venv/Scripts/activate.ps1"')