
# Write a method to decide if two strings are anagrams or not

# Are both words the same size?
#   Yes
# Can I use python native functions like ord()?
#   Yes
# How small or big is the words?
#   Minimum 1 letter
# Does time complexity matter?
#   Yes
# Does space complexity matter?
#   To certain extent

# I'm thinknig of two potential solutions
# The first one is to sum the total ordinal value of both words and compare the result
# The second one is to sort both strings, and then compare them

def anagram_sum(w1, w2):
    sum1 = 0
    sum2 = 0

    l = len(w1)

    for i in xrange(l):
        sum1 += ord(w1[i])
        sum2 += ord(w2[i])

    return sum1 == sum2

if __name__ == "__main__":
    print(anagram_sum("hola", "aloh"))
    print(anagram_sum("alskdjfhg", "ghfjdksla"))
    print(anagram_sum("alskdjfjg", "ghfjdksla"))
