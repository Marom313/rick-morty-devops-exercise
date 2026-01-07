from fastapi import FastAPI
import requests

API_URL = "https://rickandmortyapi.com/api/character"

app = FastAPI(title="Rick & Morty Service")


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
    origin_name = character.get("origin", {}).get("name", "")
    return (
        character.get("species") == "Human"
        and character.get("status") == "Alive"
        and "Earth" in origin_name
    )


@app.get("/characters")
def get_characters():
    characters = fetch_all_characters()
    filtered = [
        {
            "name": c.get("name"),
            "location": c.get("location", {}).get("name"),
            "image": c.get("image"),
        }
        for c in characters
        if is_valid_character(c)
    ]
    return {"count": len(filtered), "results": filtered}


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}
