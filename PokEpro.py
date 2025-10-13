import time

from colorama import init, Fore, Style

init(autoreset=True)

pokemon_by_number = {
    1: {"name": "Bulbasaur", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],"Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    2: {"name": "Ivysaur", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],"Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    3: {"name": "Venusaur", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],"Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    4: {"name": "Charmander", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],"Weakness": ["Water", "Ground", "Rock"]},
    5: {"name": "Charmeleon", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],"Weakness": ["Water", "Ground", "Rock"]},
    6: {"name": "Charizard", "Type": ["Fire", "Flying"], "Strength": ["Grass", "Bug", "Steel", "Fighting"],"Weakness": ["Water", "Electric", "Rock"]},
    7: {"name": "Squirtle", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    8: {"name": "Wartortle", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    9: {"name": "Blastoise", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    10: {"name": "Caterpie", "Type": ["Bug"], "Strength": ["Grass", "Psychic"], "Weakness": ["Fire", "Flying", "Rock"]},
    11: {"name": "Metapod", "Type": ["Bug"], "Strength": ["Grass", "Psychic"], "Weakness": ["Fire", "Flying", "Rock"]},
    12: {"name": "Butterfree", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Psychic"],"Weakness": ["Fire", "Electric", "Ice", "Flying", "Rock"]},
    13: {"name": "Weedle", "Type": ["Bug", "Poison"], "Strength": ["Grass", "Psychic"],"Weakness": ["Fire", "Flying", "Rock", "Psychic"]},
    14: {"name": "Kakuna", "Type": ["Bug", "Poison"], "Strength": ["Grass", "Psychic"],"Weakness": ["Fire", "Flying", "Rock", "Psychic"]},
    15: {"name": "Beedrill", "Type": ["Bug", "Poison"], "Strength": ["Grass", "Psychic"],"Weakness": ["Fire", "Flying", "Rock", "Psychic"]},
    16: {"name": "Pidgey", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],"Weakness": ["Electric", "Ice", "Rock"]},
    17: {"name": "Pidgeotto", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],"Weakness": ["Electric", "Ice", "Rock"]},
    18: {"name": "Pidgeot", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],"Weakness": ["Electric", "Ice", "Rock"]},
    19: {"name": "Rattata", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    20: {"name": "Raticate", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    21: {"name": "Spearow", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],"Weakness": ["Electric", "Ice", "Rock"]},
    22: {"name": "Fearow", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],"Weakness": ["Electric", "Ice", "Rock"]},
    23: {"name": "Ekans", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    24: {"name": "Arbok", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    25: {"name": "Pikachu", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    26: {"name": "Raichu", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    27: {"name": "Sandshrew", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"],"Weakness": ["Water", "Grass", "Ice"]},
    28: {"name": "Sandslash", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"],"Weakness": ["Water", "Grass", "Ice"]},
    29: {"name": "Nidoran Female", "Type": ["Poison"], "Strength": ["Grass", "Fairy"],"Weakness": ["Ground", "Psychic"]},
    30: {"name": "Nidorina", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    31: {"name": "Nidoqueen", "Type": ["Poison", "Ground"],"Strength": ["Grass", "Electric", "Poison", "Rock", "Steel"],"Weakness": ["Water", "Ice", "Ground", "Psychic"]},
    32: {"name": "Nidoran Male", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    33: {"name": "Nidorino", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    34: {"name": "Nidoking", "Type": ["Poison", "Ground"], "Strength": ["Grass", "Electric", "Poison", "Rock", "Steel"],"Weakness": ["Water", "Ice", "Ground", "Psychic"]},
    35: {"name": "Clefairy", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    36: {"name": "Clefable", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    37: {"name": "Vulpix", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],"Weakness": ["Water", "Ground", "Rock"]},
    38: {"name": "Ninetales", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],"Weakness": ["Water", "Ground", "Rock"]},
    39: {"name": "Jigglypuff", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    40: {"name": "Wigglytuff", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    41: {"name": "Zubat", "Type": ["Poison", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],"Weakness": ["Electric", "Ice", "Psychic", "Rock"]},
    42: {"name": "Golbat", "Type": ["Poison", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],"Weakness": ["Electric", "Ice", "Psychic", "Rock"]},
    43: {"name": "Oddish", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],"Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    44: {"name": "Gloom", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],"Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    45: {"name": "Vileplume", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],"Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    46: {"name": "Paras", "Type": ["Bug", "Grass"], "Strength": ["Grass", "Psychic", "Water", "Ground", "Rock"],"Weakness": ["Fire", "Flying", "Poison", "Bug", "Ice"]},
    47: {"name": "Parasect", "Type": ["Bug", "Grass"], "Strength": ["Grass", "Psychic", "Water", "Ground", "Rock"],"Weakness": ["Fire", "Flying", "Poison", "Bug", "Ice"]},
    48: {"name": "Venonat", "Type": ["Bug", "Poison"], "Strength": ["Grass", "Psychic"],"Weakness": ["Fire", "Flying", "Rock", "Psychic"]},
    49: {"name": "Venomoth", "Type": ["Bug", "Poison"], "Strength": ["Grass", "Psychic"],"Weakness": ["Fire", "Flying", "Rock", "Psychic"]},
    50: {"name": "Diglett", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"],"Weakness": ["Water", "Grass", "Ice"]},
    51: {"name": "Dugtrio", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"],"Weakness": ["Water", "Grass", "Ice"]},
    52: {"name": "Meowth", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    53: {"name": "Persian", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    54: {"name": "Psyduck", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    55: {"name": "Golduck", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    56: {"name": "Mankey", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],"Weakness": ["Flying", "Psychic"]},
    57: {"name": "Primeape", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],"Weakness": ["Flying", "Psychic"]},
    58: {"name": "Growlithe", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],"Weakness": ["Water", "Ground", "Rock"]},
    59: {"name": "Arcanine", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],"Weakness": ["Water", "Ground", "Rock"]},
    60: {"name": "Poliwag", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    61: {"name": "Poliwhirl", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    62: {"name": "Poliwrath", "Type": ["Water", "Fighting"],"Strength": ["Fire", "Ground", "Rock", "Normal", "Ice", "Rock", "Dark", "Steel"],"Weakness": ["Electric", "Grass", "Flying", "Psychic"]},
    63: {"name": "Abra", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    64: {"name": "Kadabra", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"],"Weakness": ["Bug", "Ghost", "Dark"]},
    65: {"name": "Alakazam", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"],"Weakness": ["Bug", "Ghost", "Dark"]},
    66: {"name": "Machop", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],"Weakness": ["Flying", "Psychic"]},
    67: {"name": "Machoke", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],"Weakness": ["Flying", "Psychic"]},
    68: {"name": "Machamp", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],"Weakness": ["Flying", "Psychic"]},
    69: {"name": "Bellsprout", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],"Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    70: {"name": "Weepinbell", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],"Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    71: {"name": "Victreebel", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],"Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    72: {"name": "Tentacool", "Type": ["Water", "Poison"], "Strength": ["Fire", "Ground", "Rock", "Grass", "Fairy"],"Weakness": ["Electric", "Psychic", "Ground"]},
    73: {"name": "Tentacruel", "Type": ["Water", "Poison"], "Strength": ["Fire", "Ground", "Rock", "Grass", "Fairy"],"Weakness": ["Electric", "Psychic", "Ground"]},
    74: {"name": "Geodude", "Type": ["Rock", "Ground"],"Strength": ["Fire", "Electric", "Poison", "Flying", "Fire", "Ice", "Rock", "Steel"],"Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    75: {"name": "Graveler", "Type": ["Rock", "Ground"],"Strength": ["Fire", "Electric", "Poison", "Flying", "Fire", "Ice", "Rock", "Steel"],"Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    76: {"name": "Golem", "Type": ["Rock", "Ground"],"Strength": ["Fire", "Electric", "Poison", "Flying", "Fire", "Ice", "Rock", "Steel"],"Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    77: {"name": "Ponyta", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],"Weakness": ["Water", "Ground", "Rock"]},
    78: {"name": "Rapidash", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],"Weakness": ["Water", "Ground", "Rock"]},
    79: {"name": "Slowpoke", "Type": ["Water", "Psychic"], "Strength": ["Fire", "Ground", "Rock", "Fighting", "Poison"],"Weakness": ["Electric", "Grass", "Bug", "Ghost", "Dark"]},
    80: {"name": "Slowbro", "Type": ["Water", "Psychic"], "Strength": ["Fire", "Ground", "Rock", "Fighting", "Poison"],"Weakness": ["Electric", "Grass", "Bug", "Ghost", "Dark"]},
    81: {"name": "Magnemite", "Type": ["Electric", "Steel"], "Strength": ["Water", "Flying", "Ice", "Rock"],"Weakness": ["Fire", "Fighting", "Ground"]},
    82: {"name": "Magneton", "Type": ["Electric", "Steel"], "Strength": ["Water", "Flying", "Ice", "Rock"],"Weakness": ["Fire", "Fighting", "Ground"]},
    83: {"name": "Farfetch'd", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],"Weakness": ["Electric", "Ice", "Rock"]},
    84: {"name": "Doduo", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],"Weakness": ["Electric", "Ice", "Rock"]},
    85: {"name": "Dodrio", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],"Weakness": ["Electric", "Ice", "Rock"]},
    86: {"name": "Seel", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    87: {"name": "Dewgong", "Type": ["Water", "Ice"], "Strength": ["Fire", "Ground", "Rock", "Grass", "Flying", "Dragon"],"Weakness": ["Electric", "Grass", "Fighting", "Rock"]},
    88: {"name": "Grimer", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    89: {"name": "Muk", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    90: {"name": "Shellder", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    91: {"name": "Cloyster", "Type": ["Water", "Ice"],"Strength": ["Fire", "Ground", "Rock", "Grass", "Flying", "Dragon"],"Weakness": ["Electric", "Grass", "Fighting", "Rock"]},
    92: {"name": "Gastly", "Type": ["Ghost", "Poison"], "Strength": ["Psychic", "Ghost", "Grass", "Fairy"],"Weakness": ["Ghost", "Psychic", "Ground"]},
    93: {"name": "Haunter", "Type": ["Ghost", "Poison"], "Strength": ["Psychic", "Ghost", "Grass", "Fairy"],"Weakness": ["Ghost", "Psychic", "Ground"]},
    94: {"name": "Gengar", "Type": ["Ghost", "Poison"], "Strength": ["Psychic", "Ghost", "Grass", "Fairy"],"Weakness": ["Ghost", "Psychic", "Ground"]},
    95: {"name": "Onix", "Type": ["Rock", "Ground"],"Strength": ["Fire", "Electric", "Poison", "Flying", "Fire", "Ice", "Rock", "Steel"],"Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    96: {"name": "Drowzee", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"],"Weakness": ["Bug", "Ghost", "Dark"]},
    97: {"name": "Hypno", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"],"Weakness": ["Bug", "Ghost", "Dark"]},
    98: {"name": "Krabby", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    99: {"name": "Kingler", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    100: {"name": "Voltorb", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    101: {"name": "Electrode", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    102: {"name": "Exeggcute", "Type": ["Grass", "Psychic"],"Strength": ["Water", "Ground", "Rock", "Fighting", "Poison"],"Weakness": ["Fire", "Ice", "Flying", "Bug", "Ghost", "Dark"]},
    103: {"name": "Exeggutor", "Type": ["Grass", "Psychic"], "Strength": ["Water", "Ground", "Rock", "Fighting", "Poison"],"Weakness": ["Fire", "Ice", "Flying", "Bug", "Ghost", "Dark"]},
    104: {"name": "Cubone", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"],"Weakness": ["Water", "Grass", "Ice"]},
    105: {"name": "Marowak", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"],"Weakness": ["Water", "Grass", "Ice"]},
    106: {"name": "Hitmonlee", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],"Weakness": ["Flying", "Psychic"]},
    107: {"name": "Hitmonchan", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],"Weakness": ["Flying", "Psychic"]},
    108: {"name": "Lickitung", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    109: {"name": "Koffing", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    110: {"name": "Weezing", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    111: {"name": "Rhyhorn", "Type": ["Ground", "Rock"],"Strength": ["Fire", "Electric", "Poison", "Flying", "Fire", "Ice", "Rock", "Steel"],"Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    112: {"name": "Rhydon", "Type": ["Ground", "Rock"],"Strength": ["Fire", "Electric", "Poison", "Flying", "Fire", "Ice", "Rock", "Steel"], "Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    113: {"name": "Chansey", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    114: {"name": "Tangela", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"],"Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    115: {"name": "Kangaskhan", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    116: {"name": "Horsea", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    117: {"name": "Seadra", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    118: {"name": "Goldeen", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    119: {"name": "Seaking", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    120: {"name": "Staryu", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    121: {"name": "Starmie", "Type": ["Water", "Psychic"], "Strength": ["Fire", "Ground", "Rock", "Fighting", "Poison"],"Weakness": ["Electric", "Grass", "Bug", "Ghost", "Dark"]},
    122: {"name": "Mr. Mime", "Type": ["Psychic", "Fairy"],"Strength": ["Fighting", "Poison", "Dragon", "Dark", "Fighting"], "Weakness": ["Poison", "Ghost", "Steel"]},
    123: {"name": "Scyther", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Psychic", "Fighting", "Bug"],"Weakness": ["Fire", "Electric", "Ice", "Flying", "Rock"]},
    124: {"name": "Jynx", "Type": ["Ice", "Psychic"],"Strength": ["Grass", "Ground", "Flying", "Dragon", "Fighting", "Poison"],"Weakness": ["Fire", "Rock", "Bug", "Ghost", "Dark", "Steel"]},
    125: {"name": "Electabuzz", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    126: {"name": "Magmar", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],"Weakness": ["Water", "Ground", "Rock"]},
    127: {"name": "Pinsir", "Type": ["Bug"], "Strength": ["Grass", "Psychic"], "Weakness": ["Fire", "Flying", "Rock"]},
    128: {"name": "Tauros", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    129: {"name": "Magikarp", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    130: {"name": "Gyarados", "Type": ["Water", "Flying"],"Strength": ["Fire", "Ground", "Rock", "Grass", "Fighting", "Bug"], "Weakness": ["Electric", "Rock"]},
    131: {"name": "Lapras", "Type": ["Water", "Ice"],"Strength": ["Fire", "Ground", "Rock", "Grass", "Flying", "Dragon"],"Weakness": ["Electric", "Grass", "Fighting", "Rock"]},
    132: {"name": "Ditto", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    133: {"name": "Eevee", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    134: {"name": "Vaporeon", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass"]},
    135: {"name": "Jolteon", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    136: {"name": "Flareon", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],"Weakness": ["Water", "Ground", "Rock"]},
    137: {"name": "Porygon", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    138: {"name": "Omanyte", "Type": ["Rock", "Water"],"Strength": ["Fire", "Ice", "Flying", "Bug", "Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass", "Fighting", "Ground"]},
    139: {"name": "Omastar", "Type": ["Rock", "Water"],"Strength": ["Fire", "Ice", "Flying", "Bug", "Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass", "Fighting", "Ground"]},
    140: {"name": "Kabuto", "Type": ["Rock", "Water"],"Strength": ["Fire", "Ice", "Flying", "Bug", "Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass", "Fighting", "Ground"]},
    141: {"name": "Kabutops", "Type": ["Rock", "Water"],"Strength": ["Fire", "Ice", "Flying", "Bug", "Fire", "Ground", "Rock"],"Weakness": ["Electric", "Grass", "Fighting", "Ground"]},
    142: {"name": "Aerodactyl", "Type": ["Rock", "Flying"],"Strength": ["Fire", "Ice", "Flying", "Bug", "Grass", "Fighting"],"Weakness": ["Water", "Electric", "Ice", "Rock", "Steel"]},
    143: {"name": "Snorlax", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    144: {"name": "Articuno", "Type": ["Ice", "Flying"], "Strength": ["Grass", "Ground", "Flying", "Dragon"],"Weakness": ["Fire", "Electric", "Rock", "Steel"]},
    145: {"name": "Zapdos", "Type": ["Electric", "Flying"], "Strength": ["Water", "Flying", "Grass", "Fighting", "Bug"],"Weakness": ["Ice", "Rock"]},
    146: {"name": "Moltres", "Type": ["Fire", "Flying"], "Strength": ["Grass", "Bug", "Steel", "Fighting"],"Weakness": ["Water", "Electric", "Rock"]},
    147: {"name": "Dratini", "Type": ["Dragon"], "Strength": ["Dragon"], "Weakness": ["Ice", "Dragon"]},
    148: {"name": "Dragonair", "Type": ["Dragon"], "Strength": ["Dragon"], "Weakness": ["Ice", "Dragon"]},
    149: {"name": "Dragonite", "Type": ["Dragon", "Flying"], "Strength": ["Dragon", "Grass", "Fighting", "Bug"], "Weakness": ["Ice", "Rock", "Dragon", "Fairy"]},
    150: {"name": "Mewtwo", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"],"Weakness": ["Bug", "Ghost", "Dark"]},
    152: {"name": "Chikorita", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    153: {"name": "Bayleef", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    154: {"name": "Meganium", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    155: {"name": "Cyndaquil", "Type": ["Fire"], "Strength": ["Grass", "Bug", "Ice", "Steel"], "Weakness": ["Water", "Ground", "Rock"]},
    156: {"name": "Quilava", "Type": ["Fire"], "Strength": ["Grass", "Bug", "Ice", "Steel"], "Weakness": ["Water", "Ground", "Rock"]},
    157: {"name": "Typhlosion", "Type": ["Fire"], "Strength": ["Grass", "Bug", "Ice", "Steel"], "Weakness": ["Water", "Ground", "Rock"]},
    158: {"name": "Totodile", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    159: {"name": "Croconaw", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    160: {"name": "Feraligatr", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    161: {"name": "Sentret", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    162: {"name": "Furret", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    163: {"name": "Hoothoot", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Bug", "Fighting"], "Weakness": ["Electric", "Ice", "Rock"]},
    164: {"name": "Noctowl", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Bug", "Fighting"], "Weakness": ["Electric", "Ice", "Rock"]},
    165: {"name": "Ledyba", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Fighting", "Psychic"], "Weakness": ["Fire", "Electric", "Flying", "Rock", "Ice"]},
    166: {"name": "Ledian", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Fighting", "Psychic"], "Weakness": ["Fire", "Electric", "Flying", "Rock", "Ice"]},
    167: {"name": "Spinarak", "Type": ["Bug", "Poison"], "Strength": ["Grass", "Psychic"], "Weakness": ["Fire", "Flying", "Psychic", "Rock"]},
    168: {"name": "Ariados", "Type": ["Bug", "Poison"], "Strength": ["Grass", "Psychic"], "Weakness": ["Fire", "Flying", "Psychic", "Rock"]},
    169: {"name": "Crobat", "Type": ["Poison", "Flying"], "Strength": ["Grass", "Bug", "Fighting"], "Weakness": ["Electric", "Psychic", "Ice", "Rock"]},
    170: {"name": "Chinchou", "Type": ["Water", "Electric"], "Strength": ["Fire", "Flying", "Water", "Ground", "Rock"], "Weakness": ["Grass", "Ground"]},
    171: {"name": "Lanturn", "Type": ["Water", "Electric"], "Strength": ["Fire", "Flying", "Water", "Ground", "Rock"], "Weakness": ["Grass", "Ground"]},
    172: {"name": "Pichu", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    173: {"name": "Cleffa", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    174: {"name": "Igglybuff", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    175: {"name": "Togepi", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    176: {"name": "Togetic", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Bug", "Fighting"], "Weakness": ["Electric", "Ice", "Rock"]},
    177: {"name": "Natu", "Type": ["Psychic", "Flying"], "Strength": ["Fighting", "Poison", "Grass", "Bug"], "Weakness": ["Electric", "Ice", "Rock", "Ghost", "Dark"]},
    178: {"name": "Xatu", "Type": ["Psychic", "Flying"], "Strength": ["Fighting", "Poison", "Grass", "Bug"], "Weakness": ["Electric", "Ice", "Rock", "Ghost", "Dark"]},
    179: {"name": "Mareep", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    180: {"name": "Flaaffy", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    181: {"name": "Ampharos", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    182: {"name": "Bellossom", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    183: {"name": "Marill", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    184: {"name": "Azumarill", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    185: {"name": "Sudowoodo", "Type": ["Rock"], "Strength": ["Fire", "Ice", "Flying", "Bug"], "Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    186: {"name": "Politoed", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    187: {"name": "Hoppip", "Type": ["Grass", "Flying"], "Strength": ["Water", "Ground", "Fighting", "Bug"], "Weakness": ["Fire", "Ice", "Flying", "Poison", "Rock"]},
    188: {"name": "Skiploom", "Type": ["Grass", "Flying"], "Strength": ["Water", "Ground", "Fighting", "Bug"], "Weakness": ["Fire", "Ice", "Flying", "Poison", "Rock"]},
    189: {"name": "Jumpluff", "Type": ["Grass", "Flying"], "Strength": ["Water", "Ground", "Fighting", "Bug"], "Weakness": ["Fire", "Ice", "Flying", "Poison", "Rock"]},
    190: {"name": "Aipom", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    191: {"name": "Sunkern", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    192: {"name": "Sunflora", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    193: {"name": "Yanma", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Fighting", "Psychic"], "Weakness": ["Fire", "Electric", "Flying", "Rock", "Ice"]},
    194: {"name": "Wooper", "Type": ["Water", "Ground"], "Strength": ["Fire", "Rock", "Poison", "Steel", "Electric"], "Weakness": ["Grass"]},
    195: {"name": "Quagsire", "Type": ["Water", "Ground"], "Strength": ["Fire", "Rock", "Poison", "Steel", "Electric"], "Weakness": ["Grass"]},
    196: {"name": "Espeon", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    197: {"name": "Umbreon", "Type": ["Dark"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Bug", "Fighting"]},
    198: {"name": "Murkrow", "Type": ["Dark", "Flying"], "Strength": ["Psychic", "Ghost", "Grass", "Bug", "Fighting"], "Weakness": ["Electric", "Ice", "Rock"]},
    199: {"name": "Slowking", "Type": ["Water", "Psychic"], "Strength": ["Fire", "Fighting", "Poison", "Ground", "Rock"], "Weakness": ["Electric", "Grass", "Bug", "Ghost", "Dark"]},
    200: {"name": "Misdreavus", "Type": ["Ghost"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Ghost", "Dark"]},
    201: {"name": "Unown", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    202: {"name": "Wobbuffet", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    203: {"name": "Girafarig", "Type": ["Normal", "Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Dark"]},
    204: {"name": "Pineco", "Type": ["Bug"], "Strength": ["Grass", "Psychic", "Dark"], "Weakness": ["Fire", "Flying", "Rock"]},
    205: {"name": "Forretress", "Type": ["Bug", "Steel"], "Strength": ["Grass", "Rock", "Ice", "Fairy"], "Weakness": ["Fire"]},
    206: {"name": "Dunsparce", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    207: {"name": "Gligar", "Type": ["Ground", "Flying"], "Strength": ["Electric", "Poison", "Rock", "Bug"], "Weakness": ["Water", "Ice"]},
    208: {"name": "Steelix", "Type": ["Steel", "Ground"], "Strength": ["Rock", "Fairy", "Poison", "Fire", "Electric"], "Weakness": ["Water", "Fire", "Fighting", "Ground"]},
    209: {"name": "Snubbull", "Type": ["Fairy"], "Strength": ["Fighting", "Dark", "Dragon"], "Weakness": ["Steel", "Poison"]},
    210: {"name": "Granbull", "Type": ["Fairy"], "Strength": ["Fighting", "Dark", "Dragon"], "Weakness": ["Steel", "Poison"]},
    211: {"name": "Qwilfish", "Type": ["Water", "Poison"], "Strength": ["Fire", "Rock", "Fairy", "Grass"], "Weakness": ["Electric", "Ground", "Psychic"]},
    212: {"name": "Scizor", "Type": ["Bug", "Steel"], "Strength": ["Grass", "Ice", "Rock", "Fairy"], "Weakness": ["Fire"]},
    213: {"name": "Shuckle", "Type": ["Bug", "Rock"], "Strength": ["Fire", "Flying", "Ice"], "Weakness": ["Water", "Steel", "Rock"]},
    214: {"name": "Heracross", "Type": ["Bug", "Fighting"], "Strength": ["Dark", "Psychic", "Grass", "Rock", "Steel", "Normal", "Ice"], "Weakness": ["Flying", "Psychic", "Fairy", "Fire"]},
    215: {"name": "Sneasel", "Type": ["Dark", "Ice"], "Strength": ["Psychic", "Ghost", "Flying", "Dragon", "Grass"], "Weakness": ["Fighting", "Rock", "Bug", "Fire", "Steel", "Fairy"]},
    216: {"name": "Teddiursa", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    217: {"name": "Ursaring", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    218: {"name": "Slugma", "Type": ["Fire"], "Strength": ["Grass", "Bug", "Ice", "Steel"], "Weakness": ["Water", "Rock", "Ground"]},
    219: {"name": "Magcargo", "Type": ["Fire", "Rock"], "Strength": ["Bug", "Ice", "Flying", "Grass"], "Weakness": ["Water", "Fighting", "Ground", "Rock"]},
    220: {"name": "Swinub", "Type": ["Ice", "Ground"], "Strength": ["Flying", "Dragon", "Fire", "Rock", "Electric"], "Weakness": ["Fire", "Water", "Grass", "Fighting", "Steel"]},
    221: {"name": "Piloswine", "Type": ["Ice", "Ground"], "Strength": ["Flying", "Dragon", "Fire", "Rock", "Electric"], "Weakness": ["Fire", "Water", "Grass", "Fighting", "Steel"]},
    222: {"name": "Corsola", "Type": ["Water", "Rock"], "Strength": ["Fire", "Flying", "Ice", "Bug"], "Weakness": ["Electric", "Grass", "Fighting", "Ground"]},
    223: {"name": "Remoraid", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    224: {"name": "Octillery", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    225: {"name": "Delibird", "Type": ["Ice", "Flying"], "Strength": ["Grass", "Bug", "Ground", "Dragon"], "Weakness": ["Fire", "Electric", "Steel", "Rock"]},
    226: {"name": "Mantine", "Type": ["Water", "Flying"], "Strength": ["Fire", "Bug", "Fighting", "Ground", "Rock"], "Weakness": ["Electric", "Rock"]},
    227: {"name": "Skarmory", "Type": ["Steel", "Flying"], "Strength": ["Grass", "Bug", "Fairy", "Ice"], "Weakness": ["Fire", "Electric"]},
    228: {"name": "Houndour", "Type": ["Dark", "Fire"], "Strength": ["Psychic", "Ghost", "Grass", "Ice", "Bug"], "Weakness": ["Water", "Rock", "Ground", "Fighting"]},
    229: {"name": "Houndoom", "Type": ["Dark", "Fire"], "Strength": ["Psychic", "Ghost", "Grass", "Ice", "Bug"], "Weakness": ["Water", "Rock", "Ground", "Fighting"]},
    230: {"name": "Kingdra", "Type": ["Water", "Dragon"], "Strength": ["Fire", "Water", "Electric", "Grass"], "Weakness": ["Dragon", "Fairy"]},
    231: {"name": "Phanpy", "Type": ["Ground"], "Strength": ["Fire", "Rock", "Electric", "Poison"], "Weakness": ["Water", "Ice", "Grass"]},
    232: {"name": "Donphan", "Type": ["Ground"], "Strength": ["Fire", "Rock", "Electric", "Poison"], "Weakness": ["Water", "Ice", "Grass"]},
    233: {"name": "Porygon2", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    234: {"name": "Stantler", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    235: {"name": "Smeargle", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    236: {"name": "Tyrogue", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Dark", "Steel", "Rock"], "Weakness": ["Psychic", "Fairy", "Flying"]},
    237: {"name": "Hitmontop", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Dark", "Steel", "Rock"], "Weakness": ["Psychic", "Fairy", "Flying"]},
    238: {"name": "Smoochum", "Type": ["Ice", "Psychic"], "Strength": ["Dragon", "Grass", "Fighting", "Poison"], "Weakness": ["Steel", "Ghost", "Dark", "Fire", "Rock", "Bug"]},
    239: {"name": "Elekid", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    240: {"name": "Magby", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"], "Weakness": ["Water", "Rock", "Ground"]},
    241: {"name": "Miltank", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    242: {"name": "Blissey", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    243: {"name": "Raikou", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    244: {"name": "Entei", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"], "Weakness": ["Water", "Rock", "Ground"]},
    245: {"name": "Suicune", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    246: {"name": "Larvitar", "Type": ["Rock", "Ground"], "Strength": ["Fire", "Electric", "Poison", "Flying"], "Weakness": ["Water", "Grass", "Ice", "Fighting"]},
    247: {"name": "Pupitar", "Type": ["Rock", "Ground"], "Strength": ["Fire", "Electric", "Poison", "Flying"], "Weakness": ["Water", "Grass", "Ice", "Fighting"]},
    248: {"name": "Tyranitar", "Type": ["Rock", "Dark"], "Strength": ["Psychic", "Flying", "Fire", "Ghost"], "Weakness": ["Fighting", "Bug", "Fairy", "Water", "Grass", "Steel", "Ground"]},
    249: {"name": "Lugia", "Type": ["Psychic", "Flying"], "Strength": ["Fighting", "Grass", "Bug"], "Weakness": ["Dark", "Ghost", "Electric", "Ice", "Rock"]},
    250: {"name": "Ho-Oh", "Type": ["Fire", "Flying"], "Strength": ["Bug", "Grass", "Fighting", "Ice", "Steel"], "Weakness": ["Water", "Electric", "Rock"]},
    251: {"name": "Celebi", "Type": ["Psychic", "Grass"], "Strength": ["Fighting", "Water", "Ground", "Rock"], "Weakness": ["Bug", "Ghost", "Fire", "Flying", "Dark", "Ice", "Poison"]},
    252: {"name": "Treecko", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    253: {"name": "Grovyle", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    254: {"name": "Sceptile", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    255: {"name": "Torchic", "Type": ["Fire"], "Strength": ["Grass", "Bug", "Ice", "Steel"], "Weakness": ["Water", "Ground", "Rock"]},
    256: {"name": "Combusken", "Type": ["Fire", "Fighting"], "Strength": ["Grass", "Ice", "Bug", "Steel", "Normal", "Rock", "Dark"], "Weakness": ["Water", "Flying", "Psychic", "Ground"]},
    257: {"name": "Blaziken", "Type": ["Fire", "Fighting"], "Strength": ["Grass", "Ice", "Bug", "Steel", "Normal", "Rock", "Dark"], "Weakness": ["Water", "Flying", "Psychic", "Ground"]},
    258: {"name": "Mudkip", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Grass", "Electric"]},
    259: {"name": "Marshtomp", "Type": ["Water", "Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"], "Weakness": ["Grass"]},
    260: {"name": "Swampert", "Type": ["Water", "Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"], "Weakness": ["Grass"]},
    261: {"name": "Poochyena", "Type": ["Dark"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Fighting", "Bug", "Fairy"]},
    262: {"name": "Mightyena", "Type": ["Dark"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Fighting", "Bug", "Fairy"]},
    263: {"name": "Zigzagoon", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    264: {"name": "Linoone", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    265: {"name": "Wurmple", "Type": ["Bug"], "Strength": ["Grass", "Psychic", "Dark"], "Weakness": ["Fire", "Flying", "Rock"]},
    266: {"name": "Silcoon", "Type": ["Bug"], "Strength": ["Grass", "Psychic", "Dark"], "Weakness": ["Fire", "Flying", "Rock"]},
    267: {"name": "Beautifly", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Fighting", "Bug"], "Weakness": ["Fire", "Flying", "Rock", "Electric", "Ice"]},
    268: {"name": "Cascoon", "Type": ["Bug"], "Strength": ["Grass", "Psychic", "Dark"], "Weakness": ["Fire", "Flying", "Rock"]},
    269: {"name": "Dustox", "Type": ["Bug", "Poison"], "Strength": ["Grass", "Fighting", "Bug", "Fairy"], "Weakness": ["Fire", "Flying", "Rock", "Psychic"]},
    270: {"name": "Lotad", "Type": ["Water", "Grass"], "Strength": ["Fire", "Water", "Ground", "Rock"], "Weakness": ["Flying", "Bug", "Poison", "Ice"]},
    271: {"name": "Lombre", "Type": ["Water", "Grass"], "Strength": ["Fire", "Water", "Ground", "Rock"], "Weakness": ["Flying", "Bug", "Poison", "Ice"]},
    272: {"name": "Ludicolo", "Type": ["Water", "Grass"], "Strength": ["Fire", "Water", "Ground", "Rock"], "Weakness": ["Flying", "Bug", "Poison", "Ice"]},
    273: {"name": "Seedot", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    274: {"name": "Nuzleaf", "Type": ["Grass", "Dark"], "Strength": ["Water", "Ground", "Rock", "Psychic", "Ghost"], "Weakness": ["Fire", "Ice", "Fighting", "Flying", "Bug", "Fairy"]},
    275: {"name": "Shiftry", "Type": ["Grass", "Dark"], "Strength": ["Water", "Ground", "Rock", "Psychic", "Ghost"], "Weakness": ["Fire", "Ice", "Fighting", "Flying", "Bug", "Fairy"]},
    276: {"name": "Taillow", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Bug", "Fighting"], "Weakness": ["Electric", "Rock", "Ice"]},
    277: {"name": "Swellow", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Bug", "Fighting"], "Weakness": ["Electric", "Rock", "Ice"]},
    278: {"name": "Wingull", "Type": ["Water", "Flying"], "Strength": ["Fire", "Water", "Ground"], "Weakness": ["Electric", "Rock", "Ice"]},
    279: {"name": "Pelipper", "Type": ["Water", "Flying"], "Strength": ["Fire", "Water", "Ground"], "Weakness": ["Electric", "Rock", "Ice"]},
    280: {"name": "Ralts", "Type": ["Psychic", "Fairy"], "Strength": ["Fighting", "Dragon", "Dark"], "Weakness": ["Ghost", "Poison", "Steel"]},
    281: {"name": "Kirlia", "Type": ["Psychic", "Fairy"], "Strength": ["Fighting", "Dragon", "Dark"], "Weakness": ["Ghost", "Poison", "Steel"]},
    282: {"name": "Gardevoir", "Type": ["Psychic", "Fairy"], "Strength": ["Fighting", "Dragon", "Dark"], "Weakness": ["Ghost", "Poison", "Steel"]},
    283: {"name": "Surskit", "Type": ["Bug", "Water"], "Strength": ["Grass", "Fire", "Ground", "Rock"], "Weakness": ["Electric", "Flying", "Psychic"]},
    284: {"name": "Masquerain", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Fighting", "Bug"], "Weakness": ["Electric", "Rock", "Fire", "Ice"]},
    285: {"name": "Shroomish", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    286: {"name": "Breloom", "Type": ["Grass", "Fighting"], "Strength": ["Water", "Ground", "Rock", "Normal", "Ice", "Dark", "Steel"], "Weakness": ["Fire", "Flying", "Poison", "Psychic", "Fairy"]},
    287: {"name": "Slakoth", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    288: {"name": "Vigoroth", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    289: {"name": "Slaking", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    290: {"name": "Nincada", "Type": ["Bug", "Ground"], "Strength": ["Grass", "Poison", "Electric", "Rock"], "Weakness": ["Fire", "Flying", "Water", "Ice"]},
    291: {"name": "Ninjask", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Bug", "Fighting"], "Weakness": ["Rock", "Fire", "Electric", "Ice"]},
    292: {"name": "Shedinja", "Type": ["Bug", "Ghost"], "Strength": ["Grass", "Poison", "Fighting"], "Weakness": ["Fire", "Flying", "Rock", "Ghost", "Dark"]},
    293: {"name": "Whismur", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    294: {"name": "Loudred", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    295: {"name": "Exploud", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    296: {"name": "Makuhita", "Type": ["Fighting"], "Strength": ["Normal", "Rock", "Steel", "Ice", "Dark"], "Weakness": ["Flying", "Psychic", "Fairy"]},
    297: {"name": "Hariyama", "Type": ["Fighting"], "Strength": ["Normal", "Rock", "Steel", "Ice", "Dark"], "Weakness": ["Flying", "Psychic", "Fairy"]},
    298: {"name": "Azurill", "Type": ["Normal", "Fairy"], "Strength": ["Fighting", "Dragon", "Dark"], "Weakness": ["Steel", "Poison"]},
    299: {"name": "Nosepass", "Type": ["Rock"], "Strength": ["Fire", "Flying", "Bug", "Ice"], "Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    300: {"name": "Skitty", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    301: {"name": "Delcatty", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    302: {"name": "Sableye", "Type": ["Dark", "Ghost"], "Strength": ["Psychic", "Poison"], "Weakness": ["Fairy"]},
    303: {"name": "Mawile", "Type": ["Steel", "Fairy"], "Strength": ["Dragon", "Dark", "Rock", "Flying", "Psychic"], "Weakness": ["Fire", "Ground"]},
    304: {"name": "Aron", "Type": ["Steel", "Rock"], "Strength": ["Normal", "Flying", "Rock", "Bug", "Ice", "Psychic", "Dragon"], "Weakness": ["Fire", "Fighting", "Ground"]},
    305: {"name": "Lairon", "Type": ["Steel", "Rock"], "Strength": ["Normal", "Flying", "Rock", "Bug", "Ice", "Psychic", "Dragon"], "Weakness": ["Fire", "Fighting", "Ground"]},
    306: {"name": "Aggron", "Type": ["Steel", "Rock"], "Strength": ["Normal", "Flying", "Rock", "Bug", "Ice", "Psychic", "Dragon"], "Weakness": ["Fire", "Fighting", "Ground"]},
    307: {"name": "Meditite", "Type": ["Fighting", "Psychic"], "Strength": ["Normal", "Rock", "Steel", "Fighting", "Poison"], "Weakness": ["Flying", "Ghost", "Fairy"]},
    308: {"name": "Medicham", "Type": ["Fighting", "Psychic"], "Strength": ["Normal", "Rock", "Steel", "Fighting", "Poison"], "Weakness": ["Flying", "Ghost", "Fairy"]},
    309: {"name": "Electrike", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    310: {"name": "Manectric", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    311: {"name": "Plusle", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    312: {"name": "Minun", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    313: {"name": "Volbeat", "Type": ["Bug"], "Strength": ["Grass", "Psychic", "Dark"], "Weakness": ["Fire", "Flying", "Rock"]},
    314: {"name": "Illumise", "Type": ["Bug"], "Strength": ["Grass", "Psychic", "Dark"], "Weakness": ["Fire", "Flying", "Rock"]},
    315: {"name": "Roselia", "Type": ["Grass", "Poison"], "Strength": ["Water", "Grass", "Fairy"], "Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    316: {"name": "Gulpin", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    317: {"name": "Swalot", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    318: {"name": "Carvanha", "Type": ["Water", "Dark"], "Strength": ["Psychic", "Ghost", "Grass"], "Weakness": ["Electric", "Fighting", "Ground", "Bug"]},
    319: {"name": "Sharpedo", "Type": ["Water", "Dark"], "Strength": ["Psychic", "Ghost", "Grass"], "Weakness": ["Electric", "Fighting", "Ground", "Bug"]},
    320: {"name": "Wailmer", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    321: {"name": "Wailord", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    322: {"name": "Numel", "Type": ["Fire", "Ground"], "Strength": ["Grass", "Ice", "Bug", "Steel"], "Weakness": ["Water", "Ground", "Rock"]},
    323: {"name": "Camerupt", "Type": ["Fire", "Ground"], "Strength": ["Grass", "Ice", "Bug", "Steel"], "Weakness": ["Water", "Ground", "Rock"]},
    324: {"name": "Torkoal", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"], "Weakness": ["Water", "Ground", "Rock"]},
    325: {"name": "Spoink", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    326: {"name": "Grumpig", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    327: {"name": "Spinda", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    328: {"name": "Trapinch", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"], "Weakness": ["Water", "Grass", "Ice"]},
    329: {"name": "Vibrava", "Type": ["Ground", "Dragon"], "Strength": ["Fire", "Electric", "Poison", "Rock"], "Weakness": ["Ice", "Dragon", "Fairy"]},
    330: {"name": "Flygon", "Type": ["Ground", "Dragon"], "Strength": ["Fire", "Electric", "Poison", "Rock"], "Weakness": ["Ice", "Dragon", "Fairy"]},
    331: {"name": "Cacnea", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    332: {"name": "Cacturne", "Type": ["Grass", "Dark"], "Strength": ["Water", "Ground", "Rock", "Psychic", "Ghost"], "Weakness": ["Fire", "Ice", "Fighting", "Flying", "Bug", "Fairy"]},
    333: {"name": "Swablu", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Bug", "Fighting"], "Weakness": ["Electric", "Rock", "Ice"]},
    334: {"name": "Altaria", "Type": ["Dragon", "Flying"], "Strength": ["Grass", "Bug", "Fighting"], "Weakness": ["Ice", "Dragon", "Rock", "Fairy"]},
    335: {"name": "Zangoose", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    336: {"name": "Seviper", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    337: {"name": "Lunatone", "Type": ["Rock", "Psychic"], "Strength": ["Normal", "Fire", "Flying", "Poison"], "Weakness": ["Water", "Grass", "Ice", "Bug", "Ghost", "Dark", "Steel"]},
    338: {"name": "Solrock", "Type": ["Rock", "Psychic"], "Strength": ["Normal", "Fire", "Flying", "Poison"], "Weakness": ["Water", "Grass", "Ice", "Bug", "Ghost", "Dark", "Steel"]},
    339: {"name": "Barboach", "Type": ["Water", "Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"], "Weakness": ["Grass"]},
    340: {"name": "Whiscash", "Type": ["Water", "Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"], "Weakness": ["Grass"]},
    341: {"name": "Corphish", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    342: {"name": "Crawdaunt", "Type": ["Water", "Dark"], "Strength": ["Psychic", "Ghost", "Grass"], "Weakness": ["Electric", "Fighting", "Ground", "Bug"]},
    343: {"name": "Baltoy", "Type": ["Ground", "Psychic"], "Strength": ["Fire", "Poison", "Rock"], "Weakness": ["Water", "Grass", "Ice", "Ghost", "Dark"]},
    344: {"name": "Claydol", "Type": ["Ground", "Psychic"], "Strength": ["Fire", "Poison", "Rock"], "Weakness": ["Water", "Grass", "Ice", "Ghost", "Dark"]},
    345: {"name": "Lileep", "Type": ["Rock", "Grass"], "Strength": ["Fire", "Ground", "Flying"], "Weakness": ["Water", "Ice", "Fighting", "Steel"]},
    346: {"name": "Cradily", "Type": ["Rock", "Grass"], "Strength": ["Fire", "Ground", "Flying"], "Weakness": ["Water", "Ice", "Fighting", "Steel"]},
    347: {"name": "Anorith", "Type": ["Rock", "Bug"], "Strength": ["Fire", "Flying", "Ice"], "Weakness": ["Water", "Rock", "Steel", "Ground"]},
    348: {"name": "Armaldo", "Type": ["Rock", "Bug"], "Strength": ["Fire", "Flying", "Ice"], "Weakness": ["Water", "Rock", "Steel", "Ground"]},
    349: {"name": "Feebas", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    350: {"name": "Milotic", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    351: {"name": "Castform", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    352: {"name": "Kecleon", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    353: {"name": "Shuppet", "Type": ["Ghost"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Dark"]},
    354: {"name": "Banette", "Type": ["Ghost"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Dark"]},
    355: {"name": "Duskull", "Type": ["Ghost"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Dark"]},
    356: {"name": "Dusclops", "Type": ["Ghost"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Dark"]},
    357: {"name": "Tropius", "Type": ["Grass", "Flying"], "Strength": ["Water", "Ground", "Grass", "Fighting", "Bug"], "Weakness": ["Fire", "Ice", "Poison", "Rock"]},
    358: {"name": "Chimecho", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    359: {"name": "Absol", "Type": ["Dark"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Fighting", "Bug", "Fairy"]},
    360: {"name": "Wynaut", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    361: {"name": "Snorunt", "Type": ["Ice"], "Strength": ["Grass", "Ground", "Flying", "Dragon"], "Weakness": ["Fire", "Fighting", "Rock", "Steel"]},
    362: {"name": "Glalie", "Type": ["Ice"], "Strength": ["Grass", "Ground", "Flying", "Dragon"], "Weakness": ["Fire", "Fighting", "Rock", "Steel"]},
    363: {"name": "Spheal", "Type": ["Ice", "Water"], "Strength": ["Grass", "Ground", "Flying", "Dragon", "Fire", "Ground", "Rock"], "Weakness": ["Fighting", "Steel", "Electric"]},
    364: {"name": "Sealeo", "Type": ["Ice", "Water"], "Strength": ["Grass", "Ground", "Flying", "Dragon", "Fire", "Ground", "Rock"], "Weakness": ["Fighting", "Steel", "Electric"]},
    365: {"name": "Walrein", "Type": ["Ice", "Water"], "Strength": ["Grass", "Ground", "Flying", "Dragon", "Fire", "Ground", "Rock"], "Weakness": ["Fighting", "Steel", "Electric"]},
    366: {"name": "Clamperl", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    367: {"name": "Huntail", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    368: {"name": "Gorebyss", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    369: {"name": "Relicanth", "Type": ["Water", "Rock"], "Strength": ["Fire", "Ice", "Flying", "Bug"], "Weakness": ["Grass", "Electric", "Fighting"]},
    370: {"name": "Luvdisc", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    371: {"name": "Bagon", "Type": ["Dragon"], "Strength": ["Dragon"], "Weakness": ["Ice", "Dragon", "Fairy"]},
    372: {"name": "Shelgon", "Type": ["Dragon"], "Strength": ["Dragon"], "Weakness": ["Ice", "Dragon", "Fairy"]},
    373: {"name": "Salamence", "Type": ["Dragon", "Flying"], "Strength": ["Dragon", "Grass", "Fighting", "Bug"], "Weakness": ["Ice", "Rock", "Dragon", "Fairy"]},
    374: {"name": "Beldum", "Type": ["Steel", "Psychic"], "Strength": ["Normal", "Grass", "Ice", "Flying", "Rock", "Psychic", "Dragon", "Fairy"], "Weakness": ["Ground", "Fire"]},
    375: {"name": "Metang", "Type": ["Steel", "Psychic"], "Strength": ["Normal", "Grass", "Ice", "Flying", "Rock", "Psychic", "Dragon", "Fairy"], "Weakness": ["Ground", "Fire"]},
    376: {"name": "Metagross", "Type": ["Steel", "Psychic"], "Strength": ["Normal", "Grass", "Ice", "Flying", "Rock", "Psychic", "Dragon", "Fairy"], "Weakness": ["Ground", "Fire"]},
    377: {"name": "Regirock", "Type": ["Rock"], "Strength": ["Fire", "Ice", "Flying", "Bug"], "Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    378: {"name": "Regice", "Type": ["Ice"], "Strength": ["Grass", "Ground", "Flying", "Dragon"], "Weakness": ["Fire", "Fighting", "Rock", "Steel"]},
    379: {"name": "Registeel", "Type": ["Steel"], "Strength": ["Normal", "Grass", "Ice", "Flying", "Rock", "Psychic", "Dragon", "Fairy"], "Weakness": ["Fire", "Fighting", "Ground"]},
    380: {"name": "Latias", "Type": ["Dragon", "Psychic"], "Strength": ["Dragon", "Fighting", "Grass", "Poison"], "Weakness": ["Ice", "Bug", "Ghost", "Dark", "Fairy"]},
    381: {"name": "Latios", "Type": ["Dragon", "Psychic"], "Strength": ["Dragon", "Fighting", "Grass", "Poison"], "Weakness": ["Ice", "Bug", "Ghost", "Dark", "Fairy"]},
    382: {"name": "Kyogre", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    383: {"name": "Groudon", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"], "Weakness": ["Water", "Grass", "Ice"]},
    384: {"name": "Rayquaza", "Type": ["Dragon", "Flying"], "Strength": ["Dragon", "Grass", "Fighting", "Bug"], "Weakness": ["Ice", "Rock", "Dragon", "Fairy"]},
    385: {"name": "Jirachi", "Type": ["Steel", "Psychic"], "Strength": ["Normal", "Grass", "Ice", "Flying", "Rock", "Psychic", "Dragon", "Fairy"], "Weakness": ["Ground", "Fire"]},
    386: {"name": "Deoxys", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    387: {"name": "Turtwig", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    388: {"name": "Grotle", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    389: {"name": "Torterra", "Type": ["Grass", "Ground"], "Strength": ["Water", "Electric", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Flying", "Bug"]},
    390: {"name": "Chimchar", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"], "Weakness": ["Water", "Ground", "Rock"]},
    391: {"name": "Monferno", "Type": ["Fire", "Fighting"], "Strength": ["Grass", "Ice", "Bug", "Steel", "Normal", "Rock", "Dark"], "Weakness": ["Water", "Flying", "Psychic", "Ground"]},
    392: {"name": "Infernape", "Type": ["Fire", "Fighting"], "Strength": ["Grass", "Ice", "Bug", "Steel", "Normal", "Rock", "Dark"], "Weakness": ["Water", "Flying", "Psychic", "Ground"]},
    393: {"name": "Piplup", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    394: {"name": "Prinplup", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    395: {"name": "Empoleon", "Type": ["Water", "Steel"], "Strength": ["Fire", "Ground", "Rock", "Normal", "Grass", "Ice", "Psychic", "Dragon", "Fairy"], "Weakness": ["Electric", "Fighting", "Ground"]},
    396: {"name": "Starly", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Bug", "Fighting"], "Weakness": ["Electric", "Rock", "Ice"]},
    397: {"name": "Staravia", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Bug", "Fighting"], "Weakness": ["Electric", "Rock", "Ice"]},
    398: {"name": "Staraptor", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Bug", "Fighting"], "Weakness": ["Electric", "Rock", "Ice"]},
    399: {"name": "Bidoof", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    400: {"name": "Bibarel", "Type": ["Normal", "Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass", "Fighting"]},
    401: {"name": "Kricketot", "Type": ["Bug"], "Strength": ["Grass", "Psychic", "Dark"], "Weakness": ["Fire", "Flying", "Rock"]},
    402: {"name": "Kricketune", "Type": ["Bug"], "Strength": ["Grass", "Psychic", "Dark"], "Weakness": ["Fire", "Flying", "Rock"]},
    403: {"name": "Shinx", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    404: {"name": "Luxio", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    405: {"name": "Luxray", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    406: {"name": "Budew", "Type": ["Grass", "Poison"], "Strength": ["Water", "Grass", "Fairy"], "Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    407: {"name": "Roserade", "Type": ["Grass", "Poison"], "Strength": ["Water", "Grass", "Fairy"], "Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    408: {"name": "Cranidos", "Type": ["Rock"], "Strength": ["Fire", "Ice", "Flying", "Bug"], "Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    409: {"name": "Rampardos", "Type": ["Rock"], "Strength": ["Fire", "Ice", "Flying", "Bug"], "Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    410: {"name": "Shieldon", "Type": ["Rock", "Steel"], "Strength": ["Normal", "Grass", "Ice", "Flying", "Rock", "Psychic", "Dragon", "Fairy"], "Weakness": ["Fighting", "Ground", "Water"]},
    411: {"name": "Bastiodon", "Type": ["Rock", "Steel"], "Strength": ["Normal", "Grass", "Ice", "Flying", "Rock", "Psychic", "Dragon", "Fairy"], "Weakness": ["Fighting", "Ground", "Water"]},
    412: {"name": "Burmy", "Type": ["Bug"], "Strength": ["Grass", "Psychic", "Dark"], "Weakness": ["Fire", "Flying", "Rock"]},
    413: {"name": "Wormadam", "Type": ["Bug", "Grass"], "Strength": ["Grass", "Psychic", "Dark", "Water", "Ground", "Rock"], "Weakness": ["Fire", "Flying", "Ice", "Poison"]},
    414: {"name": "Mothim", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Fighting", "Bug"], "Weakness": ["Rock", "Electric", "Ice", "Fire"]},
    415: {"name": "Combee", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Fighting", "Bug"], "Weakness": ["Rock", "Electric", "Ice", "Fire"]},
    416: {"name": "Vespiquen", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Fighting", "Bug"], "Weakness": ["Rock", "Electric", "Ice", "Fire"]},
    417: {"name": "Pachirisu", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    418: {"name": "Buizel", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    419: {"name": "Floatzel", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    420: {"name": "Cherubi", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    421: {"name": "Cherrim", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    422: {"name": "Shellos", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    423: {"name": "Gastrodon", "Type": ["Water", "Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"], "Weakness": ["Grass"]},
    424: {"name": "Ambipom", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    425: {"name": "Drifloon", "Type": ["Ghost", "Flying"], "Strength": ["Grass", "Fighting", "Bug"], "Weakness": ["Ghost", "Electric", "Dark", "Rock", "Ice"]},
    426: {"name": "Drifblim", "Type": ["Ghost", "Flying"], "Strength": ["Grass", "Fighting", "Bug"], "Weakness": ["Ghost", "Electric", "Dark", "Rock", "Ice"]},
    427: {"name": "Buneary", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    428: {"name": "Lopunny", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    429: {"name": "Mismagius", "Type": ["Ghost"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Dark"]},
    430: {"name": "Honchkrow", "Type": ["Dark", "Flying"], "Strength": ["Psychic", "Ghost", "Grass", "Bug", "Fighting"], "Weakness": ["Electric", "Ice", "Rock", "Fairy"]},
    431: {"name": "Glameow", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    432: {"name": "Purugly", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    433: {"name": "Chingling", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    434: {"name": "Stunky", "Type": ["Poison", "Dark"], "Strength": ["Grass", "Ghost", "Psychic"], "Weakness": ["Fighting", "Ground", "Bug", "Fairy"]},
    435: {"name": "Skuntank", "Type": ["Poison", "Dark"], "Strength": ["Grass", "Ghost", "Psychic"], "Weakness": ["Fighting", "Ground", "Bug", "Fairy"]},
    436: {"name": "Bronzor", "Type": ["Steel", "Psychic"], "Strength": ["Normal", "Grass", "Ice", "Flying", "Rock", "Psychic", "Dragon", "Fairy"], "Weakness": ["Fire", "Ground", "Ghost", "Dark"]},
    437: {"name": "Bronzong", "Type": ["Steel", "Psychic"], "Strength": ["Normal", "Grass", "Ice", "Flying", "Rock", "Psychic", "Dragon", "Fairy"], "Weakness": ["Fire", "Ground", "Ghost", "Dark"]},
    438: {"name": "Bonsly", "Type": ["Rock"], "Strength": ["Fire", "Ice", "Flying", "Bug"], "Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    439: {"name": "Mime Jr.", "Type": ["Psychic", "Fairy"], "Strength": ["Fighting", "Dragon", "Dark"], "Weakness": ["Ghost", "Poison", "Steel"]},
    440: {"name": "Happiny", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    441: {"name": "Chatot", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Bug", "Fighting"], "Weakness": ["Electric", "Rock", "Ice"]},
    442: {"name": "Spiritomb", "Type": ["Ghost", "Dark"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Fairy"]},
    443: {"name": "Gible", "Type": ["Dragon", "Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"], "Weakness": ["Ice", "Dragon", "Fairy", "Water", "Grass"]},
    444: {"name": "Gabite", "Type": ["Dragon", "Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"], "Weakness": ["Ice", "Dragon", "Fairy", "Water", "Grass"]},
    445: {"name": "Garchomp", "Type": ["Dragon", "Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"], "Weakness": ["Ice", "Dragon", "Fairy", "Water", "Grass"]},
    446: {"name": "Munchlax", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    447: {"name": "Riolu", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"], "Weakness": ["Flying", "Psychic", "Fairy"]},
    448: {"name": "Lucario", "Type": ["Fighting", "Steel"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"], "Weakness": ["Fire", "Fighting", "Ground"]},
    449: {"name": "Hippopotas", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"], "Weakness": ["Water", "Grass", "Ice"]},
    450: {"name": "Hippowdon", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"], "Weakness": ["Water", "Grass", "Ice"]},
    451: {"name": "Skorupi", "Type": ["Poison", "Bug"], "Strength": ["Grass", "Fairy"], "Weakness": ["Fire", "Flying", "Psychic", "Rock"]},
    452: {"name": "Drapion", "Type": ["Poison", "Dark"], "Strength": ["Grass", "Fairy", "Ghost", "Psychic"], "Weakness": ["Ground", "Fighting"]},
    453: {"name": "Croagunk", "Type": ["Poison", "Fighting"], "Strength": ["Grass", "Fairy", "Normal", "Ice", "Rock", "Dark", "Steel"], "Weakness": ["Flying", "Psychic", "Ground"]},
    454: {"name": "Toxicroak", "Type": ["Poison", "Fighting"], "Strength": ["Grass", "Fairy", "Normal", "Ice", "Rock", "Dark", "Steel"], "Weakness": ["Flying", "Psychic", "Ground"]},
    455: {"name": "Carnivine", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    456: {"name": "Finneon", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    457: {"name": "Lumineon", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    458: {"name": "Mantyke", "Type": ["Water", "Flying"], "Strength": ["Fire", "Fighting", "Bug", "Grass"], "Weakness": ["Electric", "Rock"]},
    459: {"name": "Snover", "Type": ["Grass", "Ice"], "Strength": ["Water", "Ground", "Rock", "Dragon", "Flying"], "Weakness": ["Fire", "Fighting", "Poison", "Steel"]},
    460: {"name": "Abomasnow", "Type": ["Grass", "Ice"], "Strength": ["Water", "Ground", "Rock", "Dragon", "Flying"], "Weakness": ["Fire", "Fighting", "Poison", "Steel"]},
    461: {"name": "Weavile", "Type": ["Dark", "Ice"], "Strength": ["Psychic", "Ghost", "Dragon", "Grass", "Flying"], "Weakness": ["Fire", "Fighting", "Rock", "Steel", "Fairy"]},
    462: {"name": "Magnezone", "Type": ["Electric", "Steel"], "Strength": ["Water", "Flying", "Normal", "Grass", "Ice", "Psychic", "Dragon", "Fairy", "Rock"], "Weakness": ["Ground"]},
    463: {"name": "Lickilicky", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    464: {"name": "Rhyperior", "Type": ["Ground", "Rock"], "Strength": ["Fire", "Electric", "Poison", "Flying", "Normal", "Ice", "Flying", "Bug"], "Weakness": ["Water", "Grass", "Fighting", "Steel", "Ground", "Ice"]},
    465: {"name": "Tangrowth", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    466: {"name": "Electivire", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    467: {"name": "Magmortar", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"], "Weakness": ["Water", "Ground", "Rock"]},
    468: {"name": "Togekiss", "Type": ["Fairy", "Flying"], "Strength": ["Fighting", "Dragon", "Grass", "Bug"], "Weakness": ["Electric", "Ice", "Poison", "Rock"]},
    469: {"name": "Yanmega", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Fighting", "Bug"], "Weakness": ["Rock", "Electric", "Ice", "Fire"]},
    470: {"name": "Leafeon", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    471: {"name": "Glaceon", "Type": ["Ice"], "Strength": ["Grass", "Ground", "Flying", "Dragon"], "Weakness": ["Fire", "Fighting", "Rock", "Steel"]},
    472: {"name": "Gliscor", "Type": ["Ground", "Flying"], "Strength": ["Grass", "Fighting", "Bug"], "Weakness": ["Water", "Ice", "Rock"]},
    473: {"name": "Mamoswine", "Type": ["Ice", "Ground"], "Strength": ["Grass", "Electric", "Flying", "Dragon", "Poison", "Rock"], "Weakness": ["Fire", "Fighting", "Steel", "Water"]},
    474: {"name": "Porygon-Z", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    475: {"name": "Gallade", "Type": ["Psychic", "Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"], "Weakness": ["Flying", "Ghost", "Fairy"]},
    476: {"name": "Probopass", "Type": ["Rock", "Steel"], "Strength": ["Normal", "Grass", "Ice", "Flying", "Rock", "Psychic", "Dragon", "Fairy"], "Weakness": ["Fighting", "Ground", "Water"]},
    477: {"name": "Dusknoir", "Type": ["Ghost"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Dark"]},
    478: {"name": "Froslass", "Type": ["Ice", "Ghost"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Fire", "Dark", "Rock", "Steel"]},
    479: {"name": "Rotom", "Type": ["Electric", "Ghost"], "Strength": ["Water", "Flying", "Psychic", "Ghost"], "Weakness": ["Dark", "Ground"]},
    480: {"name": "Uxie", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    481: {"name": "Mesprit", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    482: {"name": "Azelf", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    483: {"name": "Dialga", "Type": ["Steel", "Dragon"], "Strength": ["Normal", "Grass", "Ice", "Flying", "Rock", "Psychic", "Dragon", "Fairy"], "Weakness": ["Ground", "Fighting"]},
    484: {"name": "Palkia", "Type": ["Water", "Dragon"], "Strength": ["Fire", "Ground", "Rock", "Dragon"], "Weakness": ["Dragon", "Fairy", "Ice"]},
    485: {"name": "Heatran", "Type": ["Fire", "Steel"], "Strength": ["Grass", "Ice", "Bug", "Steel", "Normal", "Flying", "Rock", "Psychic", "Dragon", "Fairy"], "Weakness": ["Water", "Ground"]},
    486: {"name": "Regigigas", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    487: {"name": "Giratina", "Type": ["Ghost", "Dragon"], "Strength": ["Psychic", "Ghost", "Dragon"], "Weakness": ["Ice", "Dragon", "Dark", "Fairy"]},
    488: {"name": "Cresselia", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    489: {"name": "Phione", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    490: {"name": "Manaphy", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    491: {"name": "Darkrai", "Type": ["Dark"], "Strength": ["Psychic", "Ghost"], "Weakness": ["Fighting", "Bug", "Fairy"]},
    492: {"name": "Shaymin", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"], "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    493: {"name": "Arceus", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]}

}

pokemon_by_name = {info["name"].lower(): number for number, info in pokemon_by_number.items()}

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
    print(Fore.BLUE + f"  Strengths: {', '.join(pokemon['Strength']) or 'None'}")
    print(Fore.RED + f"  Weaknesses: {', '.join(pokemon['Weakness']) or 'None'}\n")

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

def main():
    history = []

    blinking_dots("Booting PokEpro V2")
    time.sleep(2)

    blinking_dots("Loading Pokédex system")
    time.sleep(1.5)

    blinking_dots("Initializing data modules")
    time.sleep(2)

    type_out("Welcome to PokEpro!\n", Fore.BLUE)
    type_out("Type a Pokémon name or Pokédex number to look it up.", Fore.MAGENTA)
    type_out("Commands: 'list' to show all Pokémon, 'undo' to go back, 'quit' to exit.\n", Fore.MAGENTA)

    while True:
        user_input = input(Fore.WHITE + "Enter Pokémon name or number (or command): ").strip().lower()

        if user_input in ["quit", "exit"]:
            print(Fore.CYAN + "Thanks for using PokEpro! Goodbye!")
            break

        if user_input == "undo":
            if len(history) >= 2:
                history.pop()  #remove lookup
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
            else:
                print(Fore.RED + "❌ ERROR: Unknown Pokédex number.")
        else:
            # Try exact name
            if user_input in pokemon_by_name:
                number = pokemon_by_name[user_input]
                print_pokemon_info(number)
                history.append(number)
            else:
                # Try partial/fuzzy
                matches = search_pokemon_by_partial_name(user_input)
                if len(matches) == 0:
                    print(Fore.RED + "❌ ERROR: Unknown Pokémon name.")
                elif len(matches) == 1:
                    number = pokemon_by_name[matches[0]]
                    print_pokemon_info(number)
                    history.append(number)
                else:
                    print(Fore.YELLOW + "Multiple Pokémon found matching your input:")
                    for i, name in enumerate(matches, 1):
                        print(f"{i}. {pokemon_by_number[pokemon_by_name[name]]['name']}")
                    try:
                        choice = int(input("Enter number of the Pokémon to select (or 0 to cancel): "))
                        if choice == 0:
                            print("Cancelled selection.")
                            continue
                        selected_name = matches[choice - 1]
                        number = pokemon_by_name[selected_name]
                        print_pokemon_info(number)
                        history.append(number)
                    except (ValueError, IndexError):
                        print(Fore.RED + "Invalid selection. Please try again.")

        cont = input("Lookup another? (yes/no): ").strip().lower()
        if cont not in ['yes', 'y']:
            print(Fore.CYAN + "Thanks for using PokEpro! Goodbye!")
            break

if __name__ == "__main__":
    main()
