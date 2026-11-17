import csv


CSV_FILE = "bannedvideogames.csv"
GAME_FIELDS = [
    "id",
    "name",
    "series",
    "country",
    "details",
    "category",
    "status",
    "wikipedia",
    "image",
    "summary",
    "developer",
    "publisher",
    "genre",
    "homepage",
]
CSV_HEADERS = [
    "Id",
    "Game",
    "Series",
    "Country",
    "Details",
    "Ban Category",
    "Ban Status",
    "Wikipedia Profile",
    "Image",
    "Summary",
    "Developer",
    "Publisher",
    "Genre",
    "Homepage",
]
HEADER_MAP = dict(zip(GAME_FIELDS, CSV_HEADERS))


def load_games(filename=CSV_FILE):
    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        rows = csv.DictReader(file)
        return [
            {
                field: row.get(csv_header, "")
                for field, csv_header in HEADER_MAP.items()
            }
            for row in rows
        ]


def save_games(games, filename=CSV_FILE):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
        writer.writeheader()
        writer.writerows(
            {
                HEADER_MAP[field]: game.get(field, "")
                for field in GAME_FIELDS
            }
            for game in games
        )


def is_currently_banned(game):
    return game.get("status", "").strip().lower() not in {"ban lifted", "lifted"}


def print_information(games):
    banned_games = games
    israel_count = sum(game["country"] == "Israel" for game in banned_games)
    country_counts = {}
    for game in banned_games:
        country_counts[game["country"]] = country_counts.get(game["country"], 0) + 1

    most_bans = max(country_counts.values(), default=0)
    countries_with_most_bans = [
        country for country, count in country_counts.items() if count == most_bans
    ]
    assassin_games = {
        game["name"]
        for game in banned_games
        if game["series"].lower() == "assassin's creed"
    }

    print(f"Games banned in Israel: {israel_count}")
    print(f"Country with most games banned: {', '.join(countries_with_most_bans)}")
    print(f"Assassin's Creed games currently banned: {len(assassin_games)}")
    print("Games banned in Germany:")
    for game in banned_games:
        if game["country"] == "Germany":
            print(f"{game['name']} - {game['details']}")
    print("Countries where Red Dead Redemption was banned:")
    for game in banned_games:
        if game["name"] == "Red Dead Redemption":
            print(f"{game['country']} - {game['details']}")


def modify_games(games):
    modified_games = []
    for game in games:
        if game["country"] == "Germany":
            continue
        if game["name"] == "Silent Hill VI":
            game["name"] = "Silent Hill Remastered"
        if game["name"] == "Bully" and game["country"] == "Brazil":
            game["status"] = "Ban Lifted"
        if game["name"] == "Manhunt II":
            game["genre"] = "Action"
        modified_games.append(game)
    return modified_games


def add_game(games):
    games.append({field: input() for field in GAME_FIELDS})


def print_country_overview(games):
    overview = {}
    for game in games:
        overview.setdefault(game["country"], []).append(game["name"])

    for country, names in overview.items():
        print(f"{country} - {len(names)}- " + "- ".join(names))


def search_by_country(games):
    country = input().strip()
    for game in games:
        if game["country"] == country:
            print(f"{game['name']} - {game['details']}")


def main(filename: str) -> None:
    games = load_games(filename)
    print("[I] Print request info from assignment")
    print("[M] Make modification based on assignment")
    print("[A] Add new game to list")
    print("[O] Overview of banned games per country")
    print("[S] Search the dataset by country")
    print("[Q] Quit program")

    while True:
        choice = input().upper()
        if choice == "I":
            print_information(games)
        elif choice == "M":
            games = modify_games(games)
            save_games(games, filename)
        elif choice == "A":
            add_game(games)
            save_games(games, filename)
        elif choice == "O":
            print_country_overview(games)
        elif choice == "S":
            search_by_country(games)
        elif choice == "Q":
            break


if __name__ == "__main__":
    main("bannedvideogames.csv")
