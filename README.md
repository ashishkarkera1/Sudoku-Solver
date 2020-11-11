# Sudoku-Solver

A Simple Sudoku Solver, Which takes given input's and solves the Sudoku Based 
on the input's. This is achieved by using a simple Backtracking Algorithm, Which
fills an empty square by checking for all the possible values and validating each value,
finding a suitable number between 1-9 and then filling the empty square with a valid possible number.
This step is recursively called for every empty square. If an empty square has no valid value possible,
this means that previously filled values were incorrect. Now the Algorithm Backtracks to the previous empty
position and tries to update it to next possible number (1-9).


Project Requirements:
* Python- 3.6.2
* Django (latest)

Steps to run the project:
* pip install requirements.txt (Install all dependencies)
* python manage.py runserver

Possible Errors:
* For PostgreSQL db set in settings.py for Heroku

 Sol- Change the "DATABASES" value to defualt django value in settings.py

