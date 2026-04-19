# CLI Contact Book

A terminal-based contact management tool that stores and manages contacts using
a CSV file for persistent storage.

## Features

- Add a new contact (name, phone, email)
- View all contacts in a clean tabular format
- Search contacts by name (partial match supported, case-insensitive)
- Prevents duplicate names
- Auto-creates the CSV file with headers on first run
- Persistent storage via `contacts.csv`

## Project Structure

```
contact_book/
├── contact_book.py
├── contacts.csv         # Auto-generated on first run
└── README.md
```

## How to Run

```bash
python3 contact_book.py
```

No external libraries required — uses only Python standard library (`csv`, `os`).

## Sample Output

```
Contact Book
1. Add Contact
2. View All Contacts
3. Search Contact
4. Exit
Enter Choice (1-4): 2

Your Contacts

Name                 Phone           Email
-----------------------------------------------------------------
Vedant               9876543210      vedant@example.com
Rahul                9123456789      rahul@example.com
Priya                9988776655      priya@example.com
```

## CSV File Format

```csv
Name,Phone,Email
Vedant,9876543210,vedant@example.com
Rahul,9123456789,rahul@example.com
```

## Menu Options

| Option | Action |
|--------|--------|
| 1 | Add a new contact |
| 2 | View all contacts |
| 3 | Search by name (partial match) |
| 4 | Exit |

## Concepts Used

- File I/O with the `csv` module (`csv.reader`, `csv.writer`, `csv.DictReader`)
- Persistent data storage
- File existence check with `os.path.exists()`
- Case-insensitive string matching with `.lower()`
- Formatted table output using f-string width specifiers
- Menu-driven CLI design with a `while` loop
- Input validation

## Dependencies

Python standard library only — no installation needed.
