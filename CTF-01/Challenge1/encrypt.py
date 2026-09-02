import string
import random

PLAINTEXT = """
This is not the actual plaintext, just for testing only. Horses are beautiful and intelligent animals that have lived 
alongside humans for thousands of years. They are known for their strength, speed, and graceful appearance. Horses come in 
many different breeds, sizes, and colors. Horses have been useful to people in many ways. In the past, they were used for 
transportation, farming, carrying goods, and helping in battles. Today, horses are commonly used for riding, sports, 
competitions, and recreation. They are also valued as loyal and gentle companions. Horses are herbivores and mainly eat grass, 
hay, and grains. They are social animals that often live in groups and communicate through sounds, body movements, and gestures.
 With proper care, horses can form strong bonds with humans. In conclusion, horses are remarkable animals that have played 
 an important role in human history. Their strength, intelligence, and beauty continue to make them one of the most admired 
 animals in the world.
""".strip()


def generate_key():
    alphabet = list(string.ascii_lowercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)

    return dict(zip(alphabet, shuffled))


def encrypt(text, key):
    result = []
    for char in text:
        if char.isalpha():
            encrypted = key[char.lower()]
            if char.isupper():
                encrypted = encrypted.upper()
            result.append(encrypted)
        else:
            result.append(char)

    return "".join(result)


key = generate_key()

ciphertext = encrypt(PLAINTEXT, key)

with open("ciphertext2.txt", "w") as f:
    f.write(ciphertext)

print("Substitution key:")
for letter in string.ascii_lowercase:
    print(key[letter], end="")

