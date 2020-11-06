from PhrasesToCheck import testphrases

# Function that checks lines of a string do not have repeated words, thus checking if a passphrase is valid.
# Returns true/false.
def passPhraseValidator(passphrase):
    passphrase = passphrase.split(" ")

    for listiterator in range(0, len(passphrase)):

        for comparisoniterator in range(listiterator + 1, len(passphrase)):
            if passphrase[listiterator] == passphrase[comparisoniterator]:
                return False

    return True

# Function that uses passPhraseValidator to check for passphrases in a string. Returns the number of valid passphrases.
def checkPhraseList(phrases):
    phrases = phrases.split("\n")
    total = 0
    for i in range(0, len(phrases)):
        if passPhraseValidator(phrases[i]):
            total += 1

    return total

print(checkPhraseList(testphrases))

# Function that checks if two words are anagrams by sorting and comparing them.
def isAnagram(phrase1, phrase2):
    return sorted(phrase1) == sorted(phrase2)

# Function that checks for passphrases with the added requirement of no words that are anagrams of each other.
def anagramPassphraseValidator(phrase):
    phrase = phrase.split(" ")

    for listiterator in range(0, len(phrase)):
        # Nested loop to ensure that a words is not compared with itself.
        for comparisoniterator in range(listiterator + 1, len(phrase)):
            if isAnagram(phrase[listiterator], phrase[comparisoniterator]):
                return False

    return True

# Function that takes a string where the rows consist of potential passphrases and returns the number that are valid.
# Could merge with above almost identical function and take function used as argument?
def checkPhraseListAnagram(phrases):
    phrases = phrases.split("\n")
    total = 0
    for i in range(0, len(phrases)):
        if anagramPassphraseValidator(phrases[i]):
            total += 1

    return total

print(checkPhraseListAnagram(testphrases))