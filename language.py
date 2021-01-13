# 'abstract' class representing a language. A contains a list of phonemes and a list of phonotactical rules.
# A language is used to generate a valid words specifically for use as a character name.

class language:

    def __init__(self, name):
        self.name = name

    def to_string(self):
        print(self.name)

    def create_word(self):
        pass
