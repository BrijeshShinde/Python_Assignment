# Employees System

A simple Python CLI application that demonstrates object-oriented programming
by managing a list of employees with basic CRUD operations.

## Features

- Add a new employee (name, age, salary)
- List all employees
- Find an employee by name
- Update an employee's salary
- Delete employees by age range

## Project Structure

```
employees_system/
├── employee.py              # Employee class (data model)
├── employees_manager.py     # Business logic (CRUD operations)
├── frontend_manager.py      # CLI menu and user input
└── README.md
```

## Classes

| Class | Responsibility |
|-------|----------------|
| `Employee` | Represents a single employee |
| `EmployeesManager` | Manages the list of employees |
| `FrontendManager` | Handles CLI menu and user interaction |

## How to Run

```bash
python3 frontend_manager.py
```

## Sample Output

```
--- Employees System ---
1. Add employee
2. List employees
3. Delete by age range
4. Find employee
5. Update salary
0. Exit
Choose: 1
Name: brijesh
Age: 27
Salary: 120000
Added Brijesh
```

## Concepts Used

- Classes and objects
- Separation of concerns (data / logic / UI layers)
- List operations and filtering
- Menu-driven CLI design
