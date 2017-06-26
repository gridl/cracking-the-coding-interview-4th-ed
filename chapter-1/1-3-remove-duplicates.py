
# Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer
# Does time complexity matter?
#   No
# What is the smallest size of the string?
#   1 character
# Does it count if they are capital or lower case?
#   They will all be lower case
# Does it matter if the order of the characters in the string is initially changed?
#   Yes
# What should the output be, a string with the characters removed?
#   Yes
# Is it possible to use a hashmap/dictionary?
#   No

# Initial answer coudl be to just go for each of the letters and check for duplicates, removing any characters that are duplicate
# But that would have an O(N^2) time complexity

def remove_dup(word):

    l = len(word)
    i = 0

    while(i < l-1):
        j = i+1
        let1 = word[i]

        while(j < l):
            let2 = word[j]

            if let1 == let2:
                word = word[:j] + word[j+1:]
            else:
                j += 1

            l = len(word)

        i += 1

    return word

# Now you can use extra buffer with constant memory

def remove_dup_const(word):
    i = 0
    letters = set()

    while(i < len(word)):

        curr = word[i]
        if not curr in letters:
            letters.add(curr)
            i += 1
        else:
            word = word[:i] + word[i+1:]

    return word

# Correct remove
# So we start i on 1, tail on 1, and length

#
def CORRECT_remove_dup(w):
    if len(w) < 2: return w

    word = list(w)

    # We initialise tail and index i to start at 1 (instead of 0)
    #   to be able to start checking for duplicates at index 0
    length = len(word)
    tail = 1
    i = 1

    # We go through all the elements of the array
    #   starting with index 1 to check if previous ones are repeated
    while i < length:
        j = 0
        # We now want to start checking one element by one starting from 0.
        # If we find that word[i] equals to word[j] then
        #   we want to keep the index where we found the duplicate
        #   otherwise we want to make sure that the index j equals the tail
        while j < tail:
            if word[i] == word[j]:
                break
            j += 1

        # Now, if we didn't find a duplicate, we want to copy the
        #   current element to the tail, as we know that, we have found our
        #   new ending, and given that this element wasn't a dupplicate, we
        #   can append it. Then we move the tail to the right as we know that
        #   the tail is now longer.
        #
        # Otherwise, we don't move the tail, and we only move the index i,
        #   which means that we skip that element and it's not added back
        #   to the actual list
        if j == tail:
            word[tail] = word[i]
            tail += 1

        i += 1

    return ''.join(word[:tail])


if __name__ == "__main__":
    print(remove_dup("a"))
    print(remove_dup(""))
    print(remove_dup("aa"))
    print(remove_dup("abc"))
    print(remove_dup("abbc"))
    print(remove_dup("aabbcccllasfeell"))

    print(remove_dup_const("a"))
    print(remove_dup_const(""))
    print(remove_dup_const("aa"))
    print(remove_dup_const("abc"))
    print(remove_dup_const("abbc"))
    print(remove_dup_const("aabbcccllasfeell"))

    print(CORRECT_remove_dup("a"))
    print(CORRECT_remove_dup(""))
    print(CORRECT_remove_dup("aa"))
    print(CORRECT_remove_dup("abc"))
    print(CORRECT_remove_dup("abbc"))
    print(CORRECT_remove_dup("aabbcccllasfeell"))

