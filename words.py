def print_upper_words(words,must_start_with):
    """
(Don’t forget to add a docstring to your function!)

Change that function so that it only prints words that start with the letter ‘e’
(either upper or lowercase).

Make your function more general: you should be able to pass in a set of letters,
and it only prints words that start with one of those letters."""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter) or word.startswith(letter.swapcase()):
                print(word.upper())

print_upper_words(
    ["hello", "hey", "goodbye", "yo", "yes"],
    must_start_with={"h", "y"})