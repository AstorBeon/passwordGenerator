from itertools import permutations


class generator():
    def __init__(self,words:[str]):
        self.provided_words = list(words)
        self.passwords=[]
        self.separators=[","," ","_","-",""]
        self.special_chars = ["?","!",".","#","$","@"]
        self.generate_simple_provided_words_mix()


    def help(self):
        print("Hello there mate! This generator is creating passwords, however you like! Just"
              "shove in some key words (name of pet, city of birth maybe?) and enjoy list of passwords!"
              "By default, creating a generator generates passwords made of mixes of keywords joined by different separators")
        print("\nMethods:\n-add_numbers -> adds numbers to generated passwords (from 0 to 10000"
              "\n-add_special_characters -> adds special characters (just 1) to every password")

    def generate_simple_provided_words_mix(self):
        for i in range(0, len(self.provided_words) + 1):
            for subset in permutations(self.provided_words, i):
                for sep in self.separators:
                    self.passwords.append(sep.join(subset))


    def add_numbers(self):
        templist=[]
        for pwd in self.passwords:
            for num_of_nums in range(1,10000):
                templist.append(pwd+str(num_of_nums))
        self.passwords.extend(templist)


    def add_special_characters(self):
        templist=[]
        for pwd in self.passwords:
            for char in self.special_chars:
                templist.append(pwd+char)
        self.passwords.extend(templist)






if __name__ == '__main__':
    gen = generator(["Mumbo","Jumbo","Lumbo"])
    gen.generate_simple_provided_words_mix()
    print(len(gen.passwords))
    gen.add_numbers()
    print(len(gen.passwords))
    gen.add_special_characters()
    print(len(gen.passwords))