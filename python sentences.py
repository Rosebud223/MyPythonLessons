import random

def main():
    """Defines quantity and tense, calls the sentence 
    function to generate a sentence, and prints it"""
    
    ##determine quantity and tense with random numbers
    quantity_values = [1,2]
    tense_values= ["past", "present", "future"]
    tense = random.choice(tense_values)
    quantity = random.choice(quantity_values)
    
    #call the sentence function and print the returned value
    sentence = make_sentence(quantity, tense)
    print(sentence)

def make_sentence(quantity, tense):
    """Uses the quantity and tense established in main()
    to call other functions and form a sentence"""

    # Call other functions to assign values to the parts of a sentence
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    
    #puts it all together! Capitalize is used in the sentence variable to simplify
    sentence = (f"{determiner.capitalize()} {noun} {verb}.")
    return sentence

def get_determiner(quantity):
    # Use quantity to choose a whether to use plural or singular
    if quantity == 1:
        # Singular determiner
        words = ["a", "one", "the"]
    else:
        # Plural determiner
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    # Use quantity value to decide what nouns to use
    # If-else statement to choose between plural and singular nouns
    if quantity == 1:
        # Uses singular nouns
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "abomination", "girl", "man", "woman", "rabbit"]
    else:
        # Uses plural nouns
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "abominations", "girls", "men", "women", "rabbits"]

    # Get a noun using random and return
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    # Determines if the tense is past, present(singular or plural) or future and provides lists for each tense
   
    if tense == "past":
        # Uses past tense verbs
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote", "mauled"]
    elif tense == "present" and quantity == 1:
        # Uses singular past present tense verbs
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes", "mauls"]
    elif tense == "present" and quantity != 1:
        # Uses plural, present tense verbs
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write", "maul"]
    else:
        # Uses future tense verbs
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will write", "will maul"]
    
    # Choose random verb based on verbs list
    verb = random.choice(verbs)
    return verb

main()