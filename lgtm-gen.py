from os import getenv
import random

LOOKS_X_TO_ME = "Looks {words} To Me"
LXTM = "L{initials}TM"

GOOD_FILE = getenv('GOOD_FILE') or 'good-synonyms'

good_synonyms = [line.rstrip('\n').title() for line in open(GOOD_FILE)]

rand_num = random.randrange(0, len(good_synonyms))

words = good_synonyms[rand_num].split()

print(LOOKS_X_TO_ME.format(words=' '.join(words)))

print(LXTM.format(initials=''.join([words[i][0] for i in range(len(words))])))
