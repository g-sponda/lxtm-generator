#!/usr/bin/python3
import random
import requests
from os import getenv

def get_synonyms(url, headers, timeout=30):
    req = requests.get(url=url, headers=headers, timeout=timeout)
    if req.status_code != 200:
        raise Exception('API error! HTTP status code: {HTTP_STATUS}'.format(HTTP_STATUS=req.status_code))    
    return req.json().get('synonyms')


DEFAULT_GOOD_SYNONYMS = ['acceptable','ace','admirable','agreeable','awesome','brill','brilliant','champion','class','commitable','cool','distinguished','divine','eminent','excellent','exceptional','exquisite','fab','fantastic','fine','fine informalsuper','first-class','first-rate','glorious','good','gorgeous','grand','gratifiable','great','heroic','honorable','impressive','magic','magnificent','marvelous','matchless','mind-blowing','nice','of high quality','of the highest quality','of the highest standard','out of this world','outstanding','peerless','perfect','positive','precious','preeminent','premium','prime','proud','quite good','rare','remarkable','renowned','resplendent','royal','satisfactory','smashing','splendid','splendiferous','splendorous','sterling','stupendou','sublime','superb','supercalifragilisticexpialidocious','superior','superlative','supreme','terrific','tip-top','too good to be true','top-notch','transcendent','tremendous','unparalleled','valuable','very good','wicked','wonderful','worthy']
DEFAULT_WORD = "good"
RAPIDAPI_TOKEN = "a97b4721a8msh275edcdf05b4f96p1bdd5cjsnf7ec84641ff2"
WORDSAPI_URL = "https://wordsapiv1.p.mashape.com/words/{word}/synonyms".format(word=DEFAULT_WORD)
HEADERS = {
    "X-Mashape-Key": RAPIDAPI_TOKEN,
    "Accept": "application/json"
}

LOOKS_X_TO_ME = "Looks {word} To Me"
LXTM = "L{initial}TM"

try:
    good_synonyms = get_synonyms(WORDSAPI_URL, headers=HEADERS)
    if good_synonyms:
        word = random.choice(good_synonyms)
    else:
        word = random.choice(DEFAULT_GOOD_SYNONYMS)
except Exception as e:
    word = DEFAULT_WORD
    print(e)

full_phrase = LOOKS_X_TO_ME.format(word=''.join(word))
initial = LXTM.format(initial=''.join(word[0].upper()))

print("{initial} ({phrase})".format(initial=initial.upper(), phrase=full_phrase.title()))
