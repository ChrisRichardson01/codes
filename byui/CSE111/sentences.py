import random

determiners = ["the", "a", "an"]
nouns = ["cat", "dog", "book", "city", "car", "house"]
verbs = ["jumped", "ran", "walked", "read", "drove", "ate"]
prepositions = ["over", "under", "on", "behind", "in front of", "near"]

def choose_word(words):
    return random.choice(words)

def make_phrase(words1, words2):
    return choose_word(words1) + " " + choose_word(words2)

def make_sentence(quantity, tense):
    determiner = choose_word(determiners)
    noun = choose_word(nouns)
    verb = choose_word(verbs)
    preposition = choose_word(prepositions)
    if quantity == "single":
        subject = determiner + " " + noun
        if tense == "past":
            verb = verb + "ed"
        elif tense == "present":
            pass
        else:
            verb = "will " + verb
    else:
        subject = " ".join([choose_word(determiners), noun + "s"])
        if tense == "past":
            verb = verb + "ed"
        elif tense == "present":
            verb = verb + "s"
        else:
            verb = "will " + verb
    object_phrase = make_phrase(prepositions, nouns)
    sentence = " ".join([subject, verb, object_phrase])
    return sentence.capitalize() + "."

# Generate and print the six sentences
sentences = []
sentences.append(make_sentence("single", "past"))
sentences.append(make_sentence("single", "present"))
sentences.append(make_sentence("single", "future"))
sentences.append(make_sentence("plural", "past"))
sentences.append(make_sentence("plural", "present"))
sentences.append(make_sentence("plural", "future"))

for sentence in sentences:
    print(sentence)