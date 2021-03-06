import string
from itertools import permutations
import argparse


def set_arg_parser():
    parser = argparse.ArgumentParser(description="""
                                    Hello there mate! This generator is creating passwords, however you like! 
                                    Just shove in some key words (name of pet, city of birth maybe?) 
                                    and enjoy list of passwords!
                                    """)
    # group = parser.add_mutually_exclusive_group()

    parser.add_argument(
        '-r', '--random',
        action="store_true",
        help='random password '
    )

    parser.add_argument(
        '-b', '--big',
        action="store_true",
        help='big letters'
    )

    parser.add_argument(
        '-s', '--small',
        action="store_true",
        help='small letters'
    )

    parser.add_argument(
        '-n', '--numbers',
        action="store_true",
        help='numbers'
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
    #TODO if you use -W olek -> returns [o,l,e,k], it should be ["olek"] needs fixing
    parser.add_argument(
        '-W', '--words',
        type=list,
        default=["Mumbo", "Jumbo", "Lumbo"],
        help='special words (default: ["Mumbo", "Jumbo", "Lumbo"])'
    )

    parser.add_argument(
        '-N', '--router_name',
        type=str,
        default="WiFi",
        help='router name (default: WiFi)'
    )

    parser.add_argument(
        '-L', '--length',
        type=int,
        default=9,
        help='router name (default: 9)'
    )

    parser.add_argument(
        '-F', '--file',
        type=str,
        default="file.txt",
        help='router name (default: file.txt)'
    )

    return parser.parse_args()


def random_passwords(number_of_chars: int, *options) -> list:
    returns = []
    big_letters = string.ascii_uppercase
    small_letters = string.ascii_lowercase
    numbers = [str(i) for i in range(0, 10)]
    tab = []
    if options[0]:
        tab += big_letters
    if options[1]:
        tab += small_letters
    if options[2]:
        tab += numbers

    index = []
    for _ in range(0, number_of_chars+1):
        index.append(0)

    b = True
    while index[-1] != 1:
        password = ""
        for k in range(0, number_of_chars):
            # print("k={},index[k]={}".format(k, index[k]))
            password += tab[index[k]]
        returns.append(password)
        index[0] += 1
        for i, el in enumerate(index):
            if el == len(tab):
                index[i + 1] += 1
                index[i] = 0

    return returns


class Generator:
    def __init__(self, words: [str]):
        self.provided_words = words
        self.passwords = []
        self.separators = [",", " ", "_", "-", "", ";"]
        self.special_chars = ["?", "!", ".", "#", "$", "@"]
        self.big_letters = string.ascii_uppercase
        self.small_letters = string.ascii_lowercase
        self.numbers = [i for i in range(0, 10)]

    def help(self):
        print("Hello there mate! This generator is creating passwords, however you like! Just"
              "shove in some key words (name of pet, city of birth maybe?) and enjoy list of passwords!")
        print("\nMethods:\n-add_numbers -> adds numbers to generated passwords (from 0 to 10000"
              "\n-add_special_characters -> adds special characters (just 1) to every password"
              "\n-go_big -> just uses all avaliable methods. Generates shitload of possible passwords"
              "\n-go_small -> takes minimalistic way of generating passes. characters+numbers(might be provided"
              "by user) and number of keywords used in single passwords(might be provided by user, defualt 2")

    def add_capital(self):
        self.provided_words.extend([x.capitalize() for x in self.provided_words])
        self.provided_words = list(set(self.provided_words))

    def add_lower(self):
        self.provided_words.extend([x.lower() for x in self.provided_words])
        self.provided_words = list(set(self.provided_words))

    def add_upper(self):
        self.provided_words.extend([x.upper() for x in self.provided_words])
        self.provided_words = list(set(self.provided_words))

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

    def add_random_passwords(self, number_of_chars: int, option: dict):
        raise NotImplementedError("Add_random_passwords is not implemented yet")
        # generates absolutely random passwords made of numbers, letters and special chars
        letters = string.ascii_letters  # zwraca duże i małe!
        numbers = string.digits
        characters = string.punctuation  # too much!
        tab = []

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
    if args.random:
        passwords = random_passwords(args.length, args.big, args.small, args.numbers)
        print(len(passwords))
    else:
        gen = Generator(args.words)

        gen.generate_simple_provided_words_mix()
        gen.add_numbers(args.max_number)
        print("olekjas1" in gen.passwords)
