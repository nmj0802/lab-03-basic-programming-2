# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Replace each `pass` with your code, and use `return` to send the answer
# back (not `print`).


def pig_latin(word):
    vowels = "aeiou"
   
    if word[0].lower() in vowels:
        return word[1:] + word [0] + "way" 

    else:
        return word[1:] + word [0] + "ay"





    # TODO (Part 1): return the Pig Latin form of a single lowercase word.
    #   If it starts with a vowel (a, e, i, o, u): add "way" to the end.
    #   Otherwise: move the first letter to the end and add "ay".
    pass





def word_lengths(sentence):

    current_word_letters = 0

    word_lengths = []
    for char in sentence:
        if char == " ":
            if current_word_letters > 0:
                current_word_letters = 0

        elif char.isalpha:
            current_word_letters += 1

    if current_word_letters > 0:
        word_lengths.append(current_word_letters)









    # TODO (Part 2): return a list with the length of each word in `sentence`
    #   (words are separated by spaces).
    pass


def reverse_words(sentence):

    words = sentence.split()

    words.rev()

    return " ".join(words)

    # TODO (Part 3): return `sentence` with the order of its words reversed.
    #   e.g. "hello world" -> "world hello"
    pass


def letter_counts(text):
    counts = []

    for char in text.lower():
        if char.isalpha():
            counts[char] = counts[char] + 1
        else:
            counts[char] = 0

    return counts

    # TODO (Part 4 - STRETCH, optional): return a dictionary mapping each letter
    #   to how many times it appears in `text`. Ignore case, and ignore anything
    #   that isn't a letter.
    pass


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # print(pig_latin("banana"))                    # ananabay
    # print(word_lengths("the quick brown fox"))    # [3, 5, 5, 3]
    # print(reverse_words("the quick brown fox"))   # fox brown quick the
    # print(letter_counts("hello"))                 # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    pass


if __name__ == "__main__":
    main()
