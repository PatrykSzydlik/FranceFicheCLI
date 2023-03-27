# write interactive command line interface in python3 using module 

import cmd
import json
import os
from datetime import datetime
from enum import Enum

# define enum for types of words in french
class WordType(Enum):
    NOUN = 1
    VERB = 2
    ADJECTIVE = 3
    ADVERB = 4
    PRONOUN = 5
    PREPOSITION = 6
    CONJUNCTION = 7
    INTERJECTION = 8

# define enum for types of verbs in french
class VerbType(Enum):
    ER = "Verbs ending in -er"
    IR = "Verbs ending in -ir"
    RE = "Verbs ending in -re"
    AUXILIARY = "Auxiliary verbs"

# Write dictionary explaining each type of verb in french
VerbTypeExplained = {
    VerbType.ER: "regular verbs that end in -er (e.g. parler, aimer)",
    VerbType.IR: "verbs that end in -ir and are conjugated like finir (e.g. choisir, réagir)",
    VerbType.RE: "irregular verbs that end in -ir (e.g. partir, sortir)",
    VerbType.AUXILIARY: "irregular verbs that end in -re (e.g. prendre, mettre)"
}

# define enum for types of nouns in french
class NounType(Enum):
    MASCULINE = 1
    FEMININE = 2
    MASCULINE_PLURAL = 3
    FEMININE_PLURAL = 4


# define enum for types of adjectives in french
class AdjectiveType(Enum):
    QUALIFICATIF = "qualificatif"
    NUMERAL = "numéral"
    DEMONSTRATIF = "démonstratif"
    INTERROGATIF = "interrogatif"
    EXCLAMATIF = "exclamatif"
    INDEFINI = "indéfini"
    POSSESSIF = "possessif"
    RELATIF = "relatif"
    NEGATIF = "negatif"

# As a comment explain what are the types of adjectives in french
AdjectiveTypeExplained = {
    "qualificatif": "Adjectives of quality: describe the quality or characteristic of a noun.",
    "numéral": "Adjectives of quantity: indicate the quantity or amount of a noun.",
    "possessif": "Possessive adjectives: show ownership or possession of a noun.",
    "démonstratif": "Demonstrative adjectives: point out the noun or clarify its identity.",
    "indéfini": "Indefinite adjectives: refer to an unspecified noun of a particular type or group.",
    "interrogatif": "Interrogative adjectives: used in questions to identify a noun or ask about its characteristics.",
    "exclamatif": "Exclamatory adjectives: express strong emotions or feelings about a noun.",
    "relatif":"Relative adjectives: describe a noun's relationship to another noun. ",
    "negatif": "Negative adjectives: describe or imply a negative meaning to a noun"
}

# define enum for types of adverbs in french
class AdverbType(Enum):
    MANNER = "manière"
    FREQUENCY = "fréquence"
    TIME = "temps"
    PLACE = "place"
    QUANTITY = "quantité"
    NEGATION = "négation"

# define enum for types of conjuctions in french
class ConjunctionType(Enum):
    COORDINATING = "coordination"
    SUBORDINATING = "subordination"
    CORRELATIVE = "corrélation"
    
# Create data class for storing french to english translation
def export_dicts_to_json(dicts_list):
    """
    Exports a list of dictionaries to JSON format.
    Saves them with the current date and time in the filename.
    :param dicts_list: a list of dictionaries to be saved as JSON files
    :return: None
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    directory = f"json_exports/{timestamp}"
    os.makedirs(directory, exist_ok=True)
    for i, dictionary in enumerate(dicts_list):
        filename = f"{directory}/dictionary_{i+1}.json"
        with open(filename, "w") as f:
            json.dump(dictionary, f)

def import_json(filename):
    with open(filename, 'r') as file:        
        data = json.load(file)
        return data

class MyCLI(cmd.Cmd):
    intro = 'Welcome to my CLI. Type help or ? to list commands.\n'
    prompt = '> '
    file = None

# define function exporting the python dictionaries into json dictonaries and saving them in the file with directory timestamp

    def do_hello(self, arg):
        """Say hello to the user"""
        print(f'Hello, {arg}!')

    def do_quit(self, arg):
        """Exit the CLI"""
        print('Quitting...')
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()