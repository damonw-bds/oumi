import random

# Define word lists for the poem
nouns = ["moon", "river", "dream", "forest", "ocean", "star", "mountain", "flower", "cloud", "shadow"]
verbs = ["whispers", "dances", "sings", "flows", "shines", "blooms", "falls", "rises", "wanders", "glows"]
adjectives = ["silent", "golden", "endless", "mystic", "gentle", "bright", "lonely", "hidden", "ancient", "soft"]
prepositions = ["beneath", "above", "within", "beyond", "through", "around", "under", "over", "near", "inside"]

# Function to generate a random line of the poem
def generate_line():
    return f"The {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(prepositions)} the {random.choice(adjectives)} {random.choice(nouns)}."

# Function to generate a random poem
def generate_poem(lines=4):
    poem = [generate_line() for _ in range(lines)]
    return "\n".join(poem)

# Generate and print a random poem
if __name__ == "__main__":
    print("Here is your random poem:\n")
    print(generate_poem())