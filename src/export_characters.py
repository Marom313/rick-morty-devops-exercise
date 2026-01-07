import csv
import os
import requests

API_URL = "https://rickandmortyapi.com/api/character"
OUTPUT_DIR = "output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "characters.csv")


def fetch_all_characters():
    characters = []
    url = API_URL

    while url:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        characters.extend(data["results"])
        url = data["info"]["next"]

    return characters


def is_valid_character(character):
    return (
        character.get("species") == "Human"
        and character.get("status") == "Alive"
        and character.get("origin", {}).get("name") == "Earth"
    )


def write_csv(characters):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Location", "Image"])

        for c in characters:
            writer.writerow([
                c.get("name", ""),
                c.get("location", {}).get("name", ""),
                c.get("image", ""),
            ])


def main():
    all_characters = fetch_all_characters()
    filtered = [c for c in all_characters if is_valid_character(c)]
    write_csv(filtered)

    print(f"Total characters fetched: {len(all_characters)}")
    print(f"Characters written to CSV: {len(filtered)}")
    print(f"CSV path: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
