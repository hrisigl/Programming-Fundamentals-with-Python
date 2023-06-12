import random

names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas", "Berkovitsa"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]

def random_word(words):
    return random.choice(words)

print("Hello, this is your first message: ")

while True:
    random_name = random_word(names)
    random_place = random_word(places)
    random_verb = random_word(verbs)
    random_noun = random_word(nouns)
    random_adverb = random_word(adverbs)
    random_detail = random_word(details)
    print(f"{random_name} from {random_place} "
          f"{random_adverb} {random_verb} {random_noun}")
    input("Click [Enter] to generate a new one.")