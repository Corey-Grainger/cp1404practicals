"""CP1404 Week 05 Prac
Wimbledon Program"""

FILENAME = "wimbledon.csv"


def main():
    """Load a CSV file of wimbledon stats and print selected stats."""
    wimbledon_records = load_file(FILENAME)
    player_to_number_of_wins = extract_player_number_of_wins(wimbledon_records)
    wimbledon_winning_countries = extract_wimbledon_winning_countries(wimbledon_records)
    display_wimbledon_winner_statistics(player_to_number_of_wins, wimbledon_winning_countries)


def display_wimbledon_winner_statistics(player_to_number_of_wins, wimbledon_winning_countries):
    """Display wimbledon winner statistics."""
    print("Wimbledon Champions: ")
    longest_name_length = max((len(name) for name in player_to_number_of_wins))
    print(longest_name_length)
    for player, number_of_wins in player_to_number_of_wins.items():
        print(f"{player:{longest_name_length}} - {number_of_wins}")
    print()
    print("These 12 countries have won Wimbledon: ")
    print(", ".join(wimbledon_winning_countries))


def load_file(filename):
    """Load data from a CSV file."""
    lines = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            lines.append(line)
    data = [line.strip().split(",") for line in lines]
    return data


def extract_player_number_of_wins(wimbledon_records):
    """Extract the player and their number of wins from wimbledon records."""
    player_to_number_of_wins = {}
    for wimbledon_record in wimbledon_records:
        try:
            player_to_number_of_wins[wimbledon_record[2]] += 1
        except KeyError:
            player_to_number_of_wins[wimbledon_record[2]] = 1
    return player_to_number_of_wins


def extract_wimbledon_winning_countries(wimbledon_records):
    """Extract a set of winning wimbledon countries from wimbledon records."""
    wimbledon_winning_countries = set([record[1] for record in wimbledon_records])
    return wimbledon_winning_countries


main()
