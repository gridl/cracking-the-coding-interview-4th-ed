
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

