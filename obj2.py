import random
from urllib.request import urlopen
import sys
WORL_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
"class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
"class %%%(object): \n\tdef __init__(self, ***)":
    "class %%% has-a __init__ that takes self and *** params.",
"*** = %%%()":
    "Set *** to an instance of class %%%.",
"***.***(@@@)":
    "From  *** get *** function, call with it params self, @@@.",
"***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
}

if len(sys.argv) == 2 and sys.argv[1] == "English":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

for words in urlopen(WORL_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.counts("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    for sentence in snippet, phrase:
        result = sentence[:]
        for word in class_names:
            result = result.replace("%%%", word, 1)
        for words in other_names:
            result = result.replace("***", word, 1)
        for words in param_names:
            result = result.replace("@@@", word, 1)
        results.append(result)
    return results
try:
    while True:
        snippets =  list(PHRASE.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASE[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            print(question)
            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
