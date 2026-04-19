# Personal Movie Tracker

A Python CLI tool that lets users maintain their own personal movie database,
similar to a mini IMDb. All data is stored in a JSON file for persistence across
sessions.

## Features

- Add movies with title, genre, and rating (0-10)
- View all movies in a clean tabular format
- Search movies by title or genre (partial match supported)
- Prevents duplicate titles (case-insensitive)
- Persistent storage via `movies.json`

## Project Structure

```
movie_tracker/
├── movie_tracker.py
├── movies.json          # Auto-generated on first run
└── README.md
```

## How to Run

```bash
python3 movie_tracker.py
```

No external libraries required — uses only Python standard library (`json`, `os`).

## Sample Output

```
--- Movie Tracker ---
1. Add movie
2. View all movies
3. Search
0. Exit
Choose: 2

------------------------------------------------------------
Title                          Genre                Rating
------------------------------------------------------------
Inception                      Sci-Fi               8.8
3 Idiots                       Comedy               8.4
Interstellar                   Sci-Fi               8.6
------------------------------------------------------------
```

## JSON File Format

```json
[
  {
    "title": "Inception",
    "genre": "Sci-Fi",
    "rating": 8.8
  }
]
```

## Concepts Used

- File I/O with JSON (`json.load`, `json.dump`)
- Persistent data storage
- List of dictionaries as a data model
- Case-insensitive string matching
- Input validation
- Formatted table output with f-string width specifiers
