import string
from nltk.tokenize import word_tokenize
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# https://www.nltk.org
# Example sentence: Hey Mark how's it going.
# output: hey mark how it going or somethign lke that
# remove punctionation, and lowercase

def lowercase(text):
    return text.lower()

def listToString(listHere):
    listHere = ' '.join(listHere)
    return listHere

def sanitizeText(text):
    # split into words
    tokens = word_tokenize(text)
    # convert to lower case
    tokens = [lowercase(w) for w in tokens]
    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    # print list
    words = listToString(words)
    return words