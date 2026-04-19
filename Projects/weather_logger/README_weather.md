# Real-Time Weather Logger

A Python CLI tool that fetches real-time weather data from the OpenWeatherMap
API and logs it to a CSV file for daily tracking and analysis.

## Features

- Fetch current weather for any city using OpenWeatherMap API
- Log temperature and weather conditions to `weather_log.csv`
- View all logs in a clean tabular format
- Statistics: average, highest, lowest temperature, and most frequent condition
- Prevents duplicate entries (same city, same day)
- Graceful handling of API failures, network errors, and invalid city names

## Project Structure

```
weather_logger/
├── weather_logger.py
├── weather_log.csv      # Auto-generated on first run
└── README.md
```

## Setup

1. **Get a free API key**
   - Sign up at [openweathermap.org/api](https://openweathermap.org/api)
   - Copy your API key from the dashboard

2. **Install dependencies**
   ```bash
   pip install requests
   ```

3. **Configure the API key**
   - Open `weather_logger.py`
   - Replace `YOUR_API_KEY_HERE` with your actual key:
     ```python
     API_KEY = "your_api_key_here"
     ```

## How to Run

```bash
python3 weather_logger.py
```

## Sample Output

```
--- Weather Logger ---
1. Add new weather log
2. View all logs
3. Show statistics
0. Exit
Choose: 2

-----------------------------------------------------------------
Date         City                 Temp (°C)    Condition
-----------------------------------------------------------------
2026-04-15   Pune                 32.5         Clear
2026-04-16   Pune                 29.8         Rain
2026-04-17   Mumbai               34.1         Clear
-----------------------------------------------------------------

========================================
      WEATHER STATISTICS
========================================
Total logs         : 3
Average temperature: 32.13°C
Highest temperature: 34.1°C
Lowest temperature : 29.8°C
Most frequent      : Clear
========================================
```

## CSV File Format

```csv
date,city,temperature,condition
2026-04-17,Pune,28.5,Clear
2026-04-17,Mumbai,34.1,Rain
```

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Invalid API key | Clear error message, no data logged |
| City not found (404) | User informed, no data logged |
| Network failure | Exception caught, user informed |
| Duplicate entry | Skipped with message |

## Concepts Used

- REST API integration with `requests` library
- CSV file I/O using the `csv` module
- Error handling with `try/except` and HTTP status codes
- Statistical analysis with `Counter` from `collections`
- Date handling with `datetime.date`
- Formatted tabular output

## Dependencies

- `requests` (install via `pip install requests`)
- Python standard library: `csv`, `os`, `datetime`, `collections`
