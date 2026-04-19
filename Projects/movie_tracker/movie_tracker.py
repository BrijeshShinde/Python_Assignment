import json
import os


class MovieTracker:
    def __init__(self, filename="movies.json"):
        self.filename = filename
        self.movies = self.load()

    def load(self):
        # If file exists, load it. Otherwise start with empty list.
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.movies, f, indent=2)

    def add_movie(self):
        title = input("Title: ").strip()
        if title == "":
            print("Title cannot be empty.")
            return

        # Check for duplicates (case-insensitive)
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                print(f"'{title}' already exists.")
                return

        genre = input("Genre: ").strip()
        try:
            rating = float(input("Rating (0-10): "))
        except ValueError:
            print("Rating must be a number.")
            return

        if rating < 0 or rating > 10:
            print("Rating must be between 0 and 10.")
            return

        self.movies.append({
            "title": title,
            "genre": genre,
            "rating": rating
        })
        self.save()
        print(f"Added '{title}'.")

    def view_all(self):
        if len(self.movies) == 0:
            print("No movies yet.")
            return
        self._print_table(self.movies)

    def search(self):
        query = input("Search by title or genre: ").strip().lower()
        if query == "":
            print("Search query cannot be empty.")
            return

        results = []
        for movie in self.movies:
            if query in movie["title"].lower() or query in movie["genre"].lower():
                results.append(movie)

        if len(results) == 0:
            print("No matches found.")
            return

        print(f"\nFound {len(results)} match(es):")
        self._print_table(results)

    def _print_table(self, movies):
        # Clean table with fixed column widths
        print("\n" + "-" * 60)
        print(f"{'Title':<30} {'Genre':<20} {'Rating':<6}")
        print("-" * 60)
        for m in movies:
            print(f"{m['title']:<30} {m['genre']:<20} {m['rating']:<6}")
        print("-" * 60)

    def run(self):
        while True:
            print("\n--- Movie Tracker ---")
            print("1. Add movie")
            print("2. View all movies")
            print("3. Search")
            print("0. Exit")

            choice = input("Choose: ").strip()

            if choice == "1":
                self.add_movie()
            elif choice == "2":
                self.view_all()
            elif choice == "3":
                self.search()
            elif choice == "0":
                print("Bye!")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = MovieTracker()
    app.run()
