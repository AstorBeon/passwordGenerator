import string
from itertools import permutations
import argparse


def set_arg_parser():
    parser = argparse.ArgumentParser(description="""
                                    Hello there mate! This generator is creating passwords, however you like! 
                                    Just shove in some key words (name of pet, city of birth maybe?) 
                                    and enjoy list of passwords!
                                    """)

    # example
    parser.add_argument(
        '-E', '--example',
        type=str,  # type of argument
        default="",
        help='example (default: "")'
    )

    parser.add_argument(
        '-min', '--min_number',
        type=int,
        default=0,
        help='min number (default: 0)'
    )

    parser.add_argument(
        '-max', '--max_number',
        type=int,
        default=1000,
        help='max number (default: 1000)'
    )

    parser.add_argument(
        '-W', '--words',
        type=list,
        default=["Mumbo", "Jumbo", "Lumbo"],
        help='max number (default: ["Mumbo", "Jumbo", "Lumbo"])'
    )

    parser.add_argument(
        '-R', '--router_name',
        type=str,
        default="WiFi",
        help='router name (default: WiFi)'
    )

    return parser.parse_args()


class generator():
    def __init__(self, words: [str]):
        self.provided_words = list(words)
        self.passwords = []
        self.separators = [",", " ", "_", "-", ""]
        self.special_chars = ["?", "!", ".", "#", "$", "@"]

    def help(self):
        print("Hello there mate! This generator is creating passwords, however you like! Just"
              "shove in some key words (name of pet, city of birth maybe?) and enjoy list of passwords!")
        print("\nMethods:\n-add_numbers -> adds numbers to generated passwords (from 0 to 10000"
              "\n-add_special_characters -> adds special characters (just 1) to every password"
              "\n-go_big -> just uses all avaliable methods. Generates shitload of possible passwords"
              "\n-go_small -> takes minimalistic way of generating passes. characters+numbers(might be provided"
              "by user) and number of keywords used in single passwords(might be provided by user, defualt 2")

    def generate_simple_provided_words_mix(self):
        # generates all variations of provided words, joined by predefined separators
        for i in range(0, len(self.provided_words) + 1):
            for subset in permutations(self.provided_words, i):
                for sep in self.separators:
                    self.passwords.append(sep.join(subset))

    def add_numbers(self, max_number: int, min_number: int = 0):
        # adds numbers to passwords from 0 to max_number
        templist = []
        for pwd in self.passwords:
            for num_of_nums in range(min_number, max_number):
                templist.append(pwd + str(num_of_nums))
        self.passwords.extend(templist)

    def add_special_characters(self):
        # add single special character at the end, at the beginning and both beginning and end
        templist = []
        for pwd in self.passwords:
            for char in self.special_chars:
                templist.append(pwd + char)
                templist.append(char + pwd)
                templist.append(char + pwd + char)
        self.passwords.extend(templist)

    def clear(self):
        self.passwords.clear()

    def add_random_passwords(self, number_of_chars: int):
        # generates absolutely random passwords made of numbers, letters and special chars
        letters = string.ascii_letters
        numbers = string.digits
        characters = string.punctuation

        # tip: itertools:product

    def go_big(self, amount_of_additional_numbers: int = 100):
        # generates all possibilities with avaliable methods
        self.generate_simple_provided_words_mix()
        self.add_numbers(amount_of_additional_numbers)
        self.add_special_characters()

    def go_small(self, max_added_number: int = 2025, min_added_number: int = 2000,
                 number_of_keywords_in_password: int = 2):
        # generates minimalistic set of passwords
        if len(self.provided_words) < 2:
            number_of_keywords_in_password = len(self.provided_words)
        for i in range(0, number_of_keywords_in_password + 1):
            for subset in permutations(self.provided_words, i):
                for sep in self.separators:
                    self.passwords.append(sep.join(subset))

        self.add_numbers(min_added_number, max_added_number)

    def save(self, filename):
        # saves generated passwords to file as txt
        with open(filename, 'w') as f:
            for single_pass in self.passwords:
                f.write("{}\n".format(single_pass))


if __name__ == '__main__':
    args = set_arg_parser()
    print(args)

    gen = generator(args.words)
    gen.go_big()
    print(len(gen.passwords))
