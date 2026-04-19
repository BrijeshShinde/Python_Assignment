import csv
import os
import requests
from datetime import date
from collections import Counter

API_KEY = "API_KEY"
CSV_FILE = "weather_log.csv"


class WeatherLogger:
    def __init__(self):
        self.filename = CSV_FILE
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["date", "city", "temperature", "condition"])

    def fetch_weather(self, city):
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": API_KEY, "units": "metric"}

        try:
            response = requests.get(url, params=params, timeout=10)
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None

        if response.status_code == 404:
            print(f"City '{city}' not found.")
            return None
        if response.status_code == 401:
            print("Invalid API key. Check your API_KEY.")
            return None
        if response.status_code != 200:
            print(f"API error: {response.status_code}")
            return None

        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["main"]
        }

    def read_logs(self):
        logs = []
        with open(self.filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                logs.append(row)
        return logs

    def is_duplicate(self, city, today):
        logs = self.read_logs()
        for log in logs:
            if log["city"].lower() == city.lower() and log["date"] == today:
                return True
        return False

    def add_log(self):
        city = input("City name: ").strip()
        if city == "":
            print("City cannot be empty.")
            return

        today = str(date.today())

        # Fetch first to get the "real" city name from API
        weather = self.fetch_weather(city)
        if weather is None:
            return

        # Duplicate check (use the API-returned city name)
        if self.is_duplicate(weather["city"], today):
            print(f"Log for '{weather['city']}' on {today} already exists.")
            return

        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([today, weather["city"], weather["temperature"], weather["condition"]])

        print(f"Logged: {weather['city']} | {weather['temperature']}°C | {weather['condition']}")

    def view_all(self):
        logs = self.read_logs()
        if len(logs) == 0:
            print("No logs yet.")
            return
        self._print_table(logs)

    def show_stats(self):
        logs = self.read_logs()
        if len(logs) == 0:
            print("No logs to analyze.")
            return

        temps = [float(log["temperature"]) for log in logs]
        conditions = [log["condition"] for log in logs]

        average = sum(temps) / len(temps)
        highest = max(temps)
        lowest = min(temps)
        most_common = Counter(conditions).most_common(1)[0][0]

        print("\n" + "=" * 40)
        print("      WEATHER STATISTICS")
        print("=" * 40)
        print(f"Total logs         : {len(logs)}")
        print(f"Average temperature: {average:.2f}°C")
        print(f"Highest temperature: {highest}°C")
        print(f"Lowest temperature : {lowest}°C")
        print(f"Most frequent      : {most_common}")
        print("=" * 40)

    def _print_table(self, logs):
        print("\n" + "-" * 65)
        print(f"{'Date':<12} {'City':<20} {'Temp (°C)':<12} {'Condition':<15}")
        print("-" * 65)
        for log in logs:
            print(f"{log['date']:<12} {log['city']:<20} {log['temperature']:<12} {log['condition']:<15}")
        print("-" * 65)

    def run(self):
        while True:
            print("\n--- Weather Logger ---")
            print("1. Add new weather log")
            print("2. View all logs")
            print("3. Show statistics")
            print("0. Exit")

            choice = input("Choose: ").strip()

            if choice == "1":
                self.add_log()
            elif choice == "2":
                self.view_all()
            elif choice == "3":
                self.show_stats()
            elif choice == "0":
                print("Bye!")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = WeatherLogger()
    app.run()
