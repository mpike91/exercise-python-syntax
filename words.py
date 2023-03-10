def print_upper_words(string_list, must_start_with):
    '''Prints out each word in string_list on separate lines fully capitalized'''
    for word in string_list:
        word = word.upper()
        for char in must_start_with:
            char = char.upper()
            if word[0] == char:
                print(f"{word}")


strings = ["hello", "hey", "goodbye", 'yo', 'yes', 'elephant']
must_start_with = {"h", "y"}
print_upper_words(strings, must_start_with)
