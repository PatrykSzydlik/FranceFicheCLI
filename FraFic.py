# write interactive command line interface in python3 using module 

import cmd
import json
import os
from datetime import datetime
from enum import Enum

class grammar():
    # define used languages for translation
    Languages = ['french',
                 'english',
                 'polish']
    
    # define enum for types of words in french
    WordType = ["NOUN", 
                "VERB", 
                "ADJECTIVE", 
                "ADVERB", 
                "PRONOUN",
                "PREPOSITION", 
                "CONJUNCTION",
                "INTERJECTION"]
    
    # define enum for types of verbs in french
    VerbType = {
    "ER": "regular verbs that end in -er (e.g. parler, aimer)",
    "IR": "verbs that end in -ir and are conjugated like finir (e.g. choisir, réagir)",
    "RE": "irregular verbs that end in -ir (e.g. partir, sortir)",
    "AUXILIARY": "irregular verbs that end in -re (e.g. prendre, mettre)"
    }

    # define enum for types of nouns in french
    NounType = ["MASCULINE",
                "FEMININE",
                "MASCULINE_PLURAL",
                "FEMININE_PLURAL"]
    
    # define enum for types of adjectives in french
    AdjectiveType = {
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
    AdverbType = ["manière",
                  "fréquence",
                  "temps",
                  "place",
                  "quantité",
                  "négation"]

    def prompt_word(self):
        

def import_json(filename):
    with open(filename, 'r') as file:        
        data = json.load(file)
        return data

class MyCLI(cmd.Cmd):
    intro = 'France Fiche CLI\n'
    prompt = '>>> '
    file = "test.json"
    word_list = []

    def do_entry(self, arg):
        new_word = {}
        arguments=arg.split(' ')
        for attribute in arguments:
            key, value = attribute.split("=")
            new_word[key] = value
        print(new_word)
        self.word_list.append(new_word)

    def do_add(self, arg):
        new_word = {}

    def do_del(self, arg):
        try:
            print(f"Deleting {self.word_list[int(arg)]}")
            self.word_list.pop(int(arg))
        except IndexError:
            print("Wrong Index")

    def do_show(self, arg):
        for word in self.word_list:
            print('\n')
            for elem in word.keys():
                print(f"{elem} = {word[elem]}")
    
    def do_save(self, arg):
        categorized_words = {w_type: [] for w_type in grammar.WordType}
        categorized_words['RANDOM'] = []
        for word in self.word_list:
            
            try:
                WordType = word.pop('WordType')
                categorized_words[WordType].append(word)
            except:
                categorized_words["RANDOM"].append(word)
        export_dicts_to_json(categorized_words)
        self.word_list = []

    def do_quit(self, arg):
        """Exit the CLI"""
        print('Quitting...')
        return True

# Create data class for storing french to english translation
def export_dicts_to_json(dicts_list):
    """
    Exports a list of dictionaries to JSON format.
    Saves them with the current date and time in the filename.
    :param dicts_list: a list of dictionaries to be saved as JSON files
    :return: None
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    base_dir = f"json_exports"
    os.makedirs(base_dir, exist_ok=True)
    for cathegory in dicts_list.keys():
        directory = f"{base_dir}/{cathegory}"
        os.makedirs(directory, exist_ok=True)
        filename = f"{directory}/words_{timestamp}.json"
        with open(filename, "w") as f:
            json.dump(dicts_list[cathegory], f)

if __name__ == '__main__':
    MyCLI().cmdloop()