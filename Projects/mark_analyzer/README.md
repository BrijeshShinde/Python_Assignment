# Student Marks Analyzer

A Python CLI tool that lets users input students with their marks and calculates
useful statistics like average, highest, and lowest scores.

## Features

- Add students with name and marks
- Remove students by name
- Prevent duplicate names
- List all students
- Generate a report showing:
  - Total number of students
  - Average marks
  - Highest marks and who scored it
  - Lowest marks and who scored it
- Handles ties (multiple students with same highest/lowest)

## Project Structure

```
marks_analyzer/
├── marks_analyzer.py
└── README.md
```

## How to Run

```bash
python3 marks_analyzer.py
```

## Sample Output

```
--- Student Marks Analyzer ---
1. Add student
2. Remove student
3. List all students
4. Show report
0. Exit
Choose: 4

========================================
      STUDENT MARKS REPORT
========================================
Total students : 5
Average marks  : 76.40
Highest marks  : 92  ->  Rahul
Lowest marks   : 60  ->  Regved, Meena
========================================
```

## Concepts Used

- Classes and methods
- Dictionaries for storing student data
- List comprehensions for finding matches
- Built-in functions: `sum()`, `max()`, `min()`, `len()`
- String formatting with f-strings
- Input validation with `try/except`
