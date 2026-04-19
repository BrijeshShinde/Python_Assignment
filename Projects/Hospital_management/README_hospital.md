# Hospital Patient Queue Management System

A Python CLI application for managing patient queues across multiple hospital
specializations, with priority-based ordering.

## Features

- Create multiple specializations (e.g., Cardiology, Neurology) with custom capacity
- Add patients with urgency levels: Normal, Urgent, Super-Urgent
- Automatic priority-based queue ordering
- Get the next patient to be served
- Remove patients by name
- View queue state per specialization

## Priority Rules

| Status | Level |
|--------|-------|
| 2 | Super-Urgent (served first) |
| 1 | Urgent |
| 0 | Normal (served last) |

Within the same priority, patients are served in the order they arrived (FIFO).

## Project Structure

```
hospital_queue/
├── patient.py              # Patient class (name + status)
├── specialization.py       # Priority queue per specialization
├── operations_manager.py   # CLI menu and multi-spec management
└── README.md
```

## Classes

| Class | Responsibility |
|-------|----------------|
| `Patient` | Represents a patient with name and status (0/1/2) |
| `Specialization` | Manages a priority queue of patients |
| `OperationsManager` | CLI interface; holds multiple specializations |

## How to Run

```bash
python3 operations_manager.py
```

## Sample Output

```
--- Hospital Queue ---
1. Add specialization
2. Add patient
3. List patients
4. Get next patient
5. Remove patient
0. Exit
Choose: 3

Cardiology (3/5):
  1. Suresh (Super-Urgent)
  2. Rahul (Urgent)
  3. Asmita (Normal)
```

## Concepts Used

- Classes and composition
- Priority queues
- Dictionaries for mapping names to objects
- Sorting and filtering with `lambda`
- Menu-driven CLI design
