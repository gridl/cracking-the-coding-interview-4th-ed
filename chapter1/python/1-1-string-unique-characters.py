
# Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?
# Are there any space or time constraints?
#   Yes, space constraints
# Is it possible to use data structures?
#   Initially yes, but this might change
# What are the expected outputs?
#   True if all unique characters, false otherwise
# Is therea minimum letters that appear?
#   Yes,1
# Can I write in Python 3, or Python 2?
#   Python 3 is fine
# Are the words in capital and lower case letters"
#   No, assume lower letters

# For the worst case scenario I could just have an O(N^2) case where for each character I check all of the other characters to see
# if there are any duplicates

# For a better case, I can use a HashMap
# I would add each character to the hashmap and increment the number of times it has appeared
# If any of the characters has appeared more than once I would return false

def dict_answer(word):

    if len(word) < 2: return True

    letters = set()
    for l in word:
        if l not in letters:
            letters.add(l)
        else:
            return False

    return True

# Now, what if we cannot use any additional data structures other than arrays?
# I would use an alphabet-long array (256 characters) initiated with zeros, then
# I would iterate through the letters in the word, and for each letter, convert into integer representation
# and add 1 to the index where the int representation for the character is
# if there's ever a character that is over 0, then i return false, otherwise I return true

def dict_answer_array(word):
    if len(word) < 2: return True

    letters = [0] * 256

    for l in word:
        l_val = ord(l)
        if letters[l_val] > 0:
            return False
        else:
            letters[l_val] += 1

    return True



if __name__ == '__main__':
    print(dict_answer("asdf"))
    print(dict_answer("asdff"))
    print(dict_answer("asddf"))

    print(dict_answer_array("asdf"))
    print(dict_answer_array("asdff"))
    print(dict_answer_array("asddf"))
