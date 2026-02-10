import time
import json
import os
import sys

from colorama import init, Fore, Style

init(autoreset=True)

# Determine path to bundled data when frozen with PyInstaller
if getattr(sys, 'frozen', False):
    # PyInstaller places bundled files in _MEIPASS
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
else:
    base_path = os.path.dirname(__file__)

OUT = os.path.join(base_path, "pokemon_data.txt")


# New: pretty-print the JSON file on disk to make it easy to read.
def _pretty_print_json_file(path):
    try:
        if not os.path.exists(path):
            return
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Write back with stable ordering and indentation for readability
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)
        # Optional: small notice to stderr (won't disrupt normal output)
        print(f"Formatted `{path}` for readability.", file=sys.stderr)
    except Exception as e:
        # Do not fail if formatting fails; loader will handle the rest
        print(f"Could not format `{path}`: {e}", file=sys.stderr)


# Call formatter before loading so the file becomes pretty on disk
# Avoid attempting to re-write files inside PyInstaller's _MEIPASS
# (read-only extraction area)
if not getattr(sys, 'frozen', False):
    _pretty_print_json_file(OUT)

# Type-effectiveness chart (attack type -> defense type -> multiplier)
# Values: 2.0 = super-effective, 0.5 = not very effective, 0.0 = immune
# This chart covers standard Gen6 interactions (includes Fairy)
_TYPE_CHART = {
    # Attacking type
    "Normal": {"Rock": 0.5, "Ghost": 0.0, "Steel": 0.5},
    "Fire": {
        "Fire": 0.5, "Water": 0.5, "Grass": 2.0, "Ice": 2.0,
        "Bug": 2.0, "Rock": 0.5, "Dragon": 0.5, "Steel": 2.0,
    },
    "Water": {
        "Fire": 2.0, "Water": 0.5, "Grass": 0.5, "Ground": 2.0,
        "Rock": 2.0, "Dragon": 0.5,
    },
    "Electric": {
        "Water": 2.0, "Electric": 0.5, "Grass": 0.5, "Ground": 0.0,
        "Flying": 2.0, "Dragon": 0.5,
    },
    "Grass": {
        "Fire": 0.5, "Water": 2.0, "Grass": 0.5, "Poison": 0.5,
        "Ground": 2.0, "Flying": 0.5, "Bug": 0.5, "Rock": 2.0,
        "Dragon": 0.5, "Steel": 0.5,
    },
    "Ice": {
        "Fire": 0.5, "Water": 0.5, "Grass": 2.0, "Ground": 2.0,
        "Flying": 2.0, "Dragon": 2.0, "Steel": 0.5,
    },
    "Fighting": {
        "Normal": 2.0, "Ice": 2.0, "Rock": 2.0, "Dark": 2.0,
        "Steel": 2.0, "Poison": 0.5, "Flying": 0.5, "Psychic": 0.5,
        "Bug": 0.5, "Ghost": 0.0, "Fairy": 0.5,
    },
    "Poison": {
        "Grass": 2.0, "Fairy": 2.0, "Poison": 0.5, "Ground": 0.5,
        "Rock": 0.5, "Ghost": 0.5, "Steel": 0.0,
    },
    "Ground": {
        "Fire": 2.0, "Electric": 2.0, "Grass": 0.5, "Poison": 2.0,
        "Flying": 0.0, "Bug": 0.5, "Rock": 2.0, "Steel": 2.0,
    },
    "Flying": {
        "Electric": 0.5, "Grass": 2.0, "Fighting": 2.0, "Bug": 2.0,
        "Rock": 0.5, "Steel": 0.5,
    },
    "Psychic": {
        "Fighting": 2.0, "Poison": 2.0, "Psychic": 0.5, "Dark": 0.0,
        "Steel": 0.5,
    },
    "Bug": {
        "Grass": 2.0, "Psychic": 2.0, "Dark": 2.0, "Fire": 0.5,
        "Fighting": 0.5, "Poison": 0.5, "Flying": 0.5, "Ghost": 0.5,
        "Steel": 0.5, "Fairy": 0.5,
    },
    "Rock": {
        "Fire": 2.0, "Ice": 2.0, "Flying": 2.0, "Bug": 2.0,
        "Fighting": 0.5, "Ground": 0.5, "Steel": 0.5,
    },
    "Ghost": {"Ghost": 2.0, "Psychic": 2.0, "Normal": 0.0, "Dark": 0.5},
    "Dragon": {"Dragon": 2.0, "Steel": 0.5, "Fairy": 0.0},
    "Dark": {
        "Psychic": 2.0, "Ghost": 2.0, "Fighting": 0.5, "Dark": 0.5,
        "Fairy": 0.5,
    },
    "Steel": {
        "Ice": 2.0, "Rock": 2.0, "Fairy": 2.0, "Fire": 0.5,
        "Water": 0.5, "Electric": 0.5, "Steel": 0.5,
    },
    "Fairy": {
        "Fighting": 2.0, "Dragon": 2.0, "Dark": 2.0, "Fire": 0.5,
        "Poison": 0.5, "Steel": 0.5,
    },
}

# Ensure keys exist for all known types (default to 1.0 vs others)
# derive from union of attack and defense types
_ALL_TYPES = sorted(set(
    list(_TYPE_CHART.keys()) +
    [d for a in _TYPE_CHART for d in _TYPE_CHART[a].keys()]
))


def _attack_multiplier(attack_type, defend_types):
    """Return the damage multiplier when attack_type hits a Pokémon
    with defend_types (list)."""
    base_map = _TYPE_CHART.get(attack_type, {})
    mul = 1.0
    for d in defend_types:
        mul *= float(base_map.get(d, 1.0))
    return mul


def compute_strengths_and_weaknesses(types):
    """Given a Pokémon's typing (list), return (strength_list,
    weakness_list).

    - strength_list: defender types where this Pokémon's
      attacks are super-effective (>1)
    - weakness_list: attacking types that are super-effective
      against this Pokémon (>1)"""
    types = [t.title() for t in types if t]

    strengths = []
    weaknesses = []

    # Strengths: for each possible defender type, check whether any of
    # this Pokémon's own attack types would be super-effective against
    # that defender.
    for defender in _ALL_TYPES:
        for atk in types:
            if _attack_multiplier(atk, [defender]) > 1.0:
                strengths.append(defender)
                break

    # Weaknesses: incoming attack types that are super-effective
    # against this Pokémon's typing.
    for atk in _TYPE_CHART.keys():
        if _attack_multiplier(atk, types) > 1.0:
            weaknesses.append(atk)

    # Deduplicate and sort
    strengths = sorted(set(strengths))
    weaknesses = sorted(set(weaknesses))
    return strengths, weaknesses


# Replace the previous large inline dict with the loader
# (existing code kept, shown here)
# (initial empty assignment removed - loader will create the dict)

def _load_pokemon_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # convert string keys to ints and post-process entries
        result = {}
        for k, v in data.items():
            try:
                ik = int(k)
            except ValueError:
                continue
            entry = dict(v)
            # Ensure name exists
            name = entry.get("name") or entry.get("Name") or ""
            # Normalize type list
            types = entry.get("Type") or entry.get("type") or []
            if isinstance(types, str):
                types = [t.strip() for t in types.split(',') if t.strip()]
            types = [t.title() for t in types if t]
            entry["Type"] = types

            # If Strength/Weakness missing or empty, compute them
            if not entry.get("Strength") or not entry.get("Weakness"):
                strengths, weaknesses = compute_strengths_and_weaknesses(types)
                entry["Strength"] = strengths
                entry["Weakness"] = weaknesses

            entry["name"] = name
            result[ik] = entry
        return result
    except FileNotFoundError:
        print(f"Pokédex file not found: {path}", file=sys.stderr)
        return {}
    except Exception as e:
        print(f"Failed to load Pokédex from {path}: {e}", file=sys.stderr)
        return {}


pokemon_by_number = _load_pokemon_file(OUT)
if pokemon_by_number:
    print(f"Loaded {len(pokemon_by_number)} entries from `{OUT}`.")
else:
    msg = ("No Pokédex data loaded (pokemon_by_number is empty). "
           "Add a valid pokemon_data.txt in the same folder.")
    print(msg, file=sys.stderr)

pokemon_by_name = {
    info["name"].lower(): number
    for number, info in pokemon_by_number.items()
}


def search_pokemon_by_partial_name(partial_name):
    return [name for name in pokemon_by_name if partial_name in name]


def type_out(text, color=Fore.WHITE, delay=0.02):
    for char in text:
        print(f"{color}{char}", end="", flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)


def print_pokemon_info(number):
    pokemon = pokemon_by_number[number]
    print(Fore.CYAN + f"\n#{number} - {pokemon['name']}")
    print(Fore.GREEN + f"  Type: {', '.join(pokemon['Type'])}")
    strengths_str = ', '.join(pokemon['Strength']) or 'None'
    print(Fore.BLUE + f"  Strengths: {strengths_str}")
    weaknesses_str = ', '.join(pokemon['Weakness']) or 'None'
    print(Fore.RED + f"  Weaknesses: {weaknesses_str}\n")


def list_all_pokemon(pokedex):
    print(Fore.CYAN + "\n--- Pokédex Entries ---")
    for number in sorted(pokedex.keys()):
        name = pokedex[number]["name"]
        print(Fore.YELLOW + f"#{number:03d} - {name}")
    print()


def blinking_dots(message="Loading", cycles=3, delay=0.4):
    for _ in range(cycles):
        for dots in ['.', '..', '...']:
            print(f"\r{Fore.GREEN}{message}{dots}   ", end='', flush=True)
            time.sleep(delay)
    print("\r" + " " * (len(message) + 5), end='\r')


def _ask_lookup_another():
    """Prompt until user answers yes/no.
    
    Return True to continue, False to exit.
    """
    while True:
        prompt = "Would you like to Lookup another? (yes/no): "
        cont = input(prompt).strip().lower()
        if cont in ("yes", "y"):
            return True
        if cont in ("no", "n"):
            print(Fore.CYAN + "Thanks for using PokEpro! Goodbye!")
            return False
        print(Fore.YELLOW + "Please answer 'yes' or 'no'.")


def main():
    history = []

    blinking_dots("Booting PokEpro V5.01")
    time.sleep(2)

    blinking_dots("Loading Pokédex system")
    time.sleep(1.5)

    blinking_dots("Initializing data modules")
    time.sleep(2)

    type_out("Welcome to PokEpro!\n", Fore.BLUE)
    type_out("Type a Pokémon name or Pokédex number to look it up.",
             Fore.MAGENTA)
    type_out("Commands: 'list' to show all Pokémon, 'undo' to go back, "
             "'quit' to exit.\n", Fore.MAGENTA)

    while True:
        prompt_text = "Enter Pokémon name or number (or type commands): "
        user_input = input(Fore.WHITE + prompt_text).strip().lower()

        if user_input in ["quit", "exit"]:
            print(Fore.CYAN + "Thanks for using PokEpro! Goodbye!")
            return

        if user_input == "undo":
            if len(history) >= 2:
                history.pop()
                # remove lookup
                previous = history[-1]
                print(Fore.YELLOW + "🔄 Undoing. Showing previous Pokémon:")
                print_pokemon_info(previous)
            else:
                print(Fore.RED + "❌ Nothing to undo.")
            continue

        if user_input == "list":
            list_all_pokemon(pokemon_by_number)
            continue

        # what if number
        if user_input.isdigit():
            number = int(user_input)
            if number in pokemon_by_number:
                print_pokemon_info(number)
                history.append(number)
                if not _ask_lookup_another():
                    return
            else:
                print(Fore.RED + "❌ ERROR: Unknown Pokédex number.")
        else:
            # Try exact name
            if user_input in pokemon_by_name:
                number = pokemon_by_name[user_input]
                print_pokemon_info(number)
                history.append(number)
                if not _ask_lookup_another():
                    return
                continue
            else:
                # Try partial/fuzzy
                matches = search_pokemon_by_partial_name(user_input)
                if len(matches) == 0:
                    print(Fore.RED + "❌ ERROR: Unknown Pokémon name.")
                elif len(matches) == 1:
                    number = pokemon_by_name[matches[0]]
                    print_pokemon_info(number)
                    history.append(number)
                    if not _ask_lookup_another():
                        return
                    continue
                else:
                    print(Fore.YELLOW + "Multiple Pokémon found matching "
                          "your input:")
                    for i, name in enumerate(matches, 1):
                        poke_name = pokemon_by_number[
                            pokemon_by_name[name]]['name']
                        print(f"{i}. {poke_name}")
                    try:
                        choice = int(input("Enter number of the Pokémon to select (or 0 to cancel): "))
                        if choice == 0:
                            print("Cancelled selection.")
                            continue
                        selected_name = matches[choice - 1]
                        number = pokemon_by_name[selected_name]
                        print_pokemon_info(number)
                        history.append(number)
                        if not _ask_lookup_another():
                            return
                    except (ValueError, IndexError):
                        print(Fore.RED + "Invalid selection. Please try again.")


if __name__ == "__main__":
    main()
