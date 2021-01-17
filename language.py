# 'abstract' class representing a language. A contains a list of phonemes and a list of phonotactical rules.
# A language is used to generate a valid words specifically for use as a character name.
import random


class Language:

    # Args:
    # name              string
    # consonants        list of string
    # vowels            list of string
    # min_onset         int             the minimum number of consonants in the onset
    # max_onset         int             the maximum number of consonants in the onset
    # min_nucleus       int             the minimum number of vowels in the nucleus
    # max_nucleus       int             the maximum number of vowels in the nucleus
    # min_coda          int             the minimum number of consonants in the coda
    # max_coda          int             the maximum number of consonants in the coda
    def __init__(self, name, consonants, vowels, min_onset, max_onset, min_nucleus, max_nucleus, min_coda, max_coda):
        self.name = name
        self.consonants = consonants
        self.vowels = vowels
        self.min_onset = min_onset
        self.max_onset = max_onset
        self.min_nucleus = min_nucleus
        self.max_nucleus = max_nucleus
        self.min_coda = min_coda
        self.max_coda = max_coda

    def to_string(self):
        print(self.name)

    def _create_word(self, syllables):
        word = ""
        for i in range(0, syllables):
            # We only use the onset rules once here. See following comment.
            if i == 0:
                for j in range(0, random.randint(self.min_onset, self.max_onset)):
                    word += str.lower(self.consonants[random.randint(0, len(self.consonants) - 1)])

            for k in range(0, random.randint(self.min_nucleus, self.max_nucleus)):
                word += str.lower(self.vowels[random.randint(0, len(self.vowels) - 1)])

            # This prevents gigantic consonant clusters from forming in the middle of words, by recognizing that
            # the coda of one non-word-final syllable becomes the onset of the next syllable
            if i == syllables:
                this_coda_max = self.max_coda
            else:
                this_coda_max = self.max_onset

            for l in range(0, random.randint(self.min_coda, this_coda_max)):
                word += str.lower(self.consonants[random.randint(0, len(self.consonants) - 1)])
        return word.capitalize()

    def create_word(self):
        return self._create_word(random.randint(1, 3))


Harrondian = Language("Harrondian",
                      ['m', 'n', 'p', 'b', "p'", 't', 'd', "t'", 'k', 'g', "k'", 'dz', "ts'", 'mv', 's', 'nz', 'h', 'r',
                       'l'],
                      ['a', 'e', 'i', 'o'],
                      0, 1, 1, 1, 0, 2)
Naal_Ayan = Language("Nal Ayan",
                     ['m', 'n', 'p', 'b', 't', 'd', 'k', 'g', 'z', 's', 'sh', 'j', 'v', 'h', 'r',
                      'l', 'y'],
                     ['a', 'e', 'i', 'o', 'u'],
                     0, 2, 1, 2, 0, 2)
Dizaki = Language("Dizaki",
                  ['m', 'n', 'p', 'b', 't', 'd', 'th', 'dh', 'k', 'g', 'kh', 'gh', 's', 'sh', 'j', 'v', 'h', 'r',
                   'l', 'y'],
                  ['a', 'e', 'i', 'o', 'u'],
                  1, 1, 1, 1, 0, 1)
Jianangese = Language("Jian-angese",
                      ['m', 'n', 'p', 'b', 't', 'd', 'k', 'g', 's', 'sh', 'zh', 'w', 'h', 'r',
                       'l', 'ng', 'y', "'"],
                      ['a', 'e', 'i', 'o', 'u'],
                      0, 1, 1, 3, 0, 1)
Ked = Language("Ked",
               ['m', 'n', 'p', 'b', 't', 'd', 'q', 's', 'z', 'sh', 'zh', 'w', 'hh', 'kh', 'r',
                'l', 'y', "'"],
               ['a', 'e', 'i', 'o', 'u'],
               0, 1, 0, 2, 1, 3)
Mauali = Language("Mauali",
                  ['m', 'n', 'p', 'b', 't', 'd', 'c', 'g', 's', 'z', 'ch', 'll', 'h', 'r',
                   'l'],
                  ['a', 'e', 'i', 'o', 'u'],
                  0, 2, 1, 2, 1, 1)
