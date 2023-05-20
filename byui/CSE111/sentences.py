import random

determiners = ["the", "a", "an"]
nouns = ["cat", "dog", "book", "city", "car", "house"]
verbs = ["jumped", "ran", "walked", "read", "drove", "ate"]
prepositions = ["over", "under", "on", "behind", "in front of", "near"]

def choose_word(words):
    return random.choice(words)

def get_determiner():
    return choose_word(determiners)

def get_noun():
    return choose_word(nouns)

def get_verb():
    return choose_word(verbs)

def get_preposition():
    return choose_word(prepositions)

def get_prepositional_phrase():
    preposition = get_preposition()
    determiner = get_determiner()
    noun = get_noun()
    return f"{preposition} {determiner} {noun}"

def make_sentence(quantity, tense):
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    prepositional_phrase = get_prepositional_phrase()

    if quantity == "single":
        subject = f"{determiner} {noun}"
        if tense == "past":
            verb = f"{verb}ed"
        elif tense == "future":
            verb = f"will {verb}"
    else:
        subject = f"{choose_word(determiners)} {noun}s"
        if tense == "past":
            verb = f"{verb}ed"
        elif tense == "future":
            verb = f"will {verb}"
        else:
            verb = f"{verb}s"

    sentence = f"{subject} {verb} {prepositional_phrase}"
    return sentence.capitalize() + "."

def main():
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

if __name__ == "__main__":
    main()