# Assume you have a method isSubstring which checks if one
#   word is a substring of another. Given two strings, s1 and
#   s2, write code to check if s2 is a rotation of s1 using only
#   one call to isSubstring (i.e., "waterbottle" is a rotation of
#   "erbottlewat").
#
# What is the minimum size of both strings?
#   1
# Does space complexity matter?
#   Not initially
# Time complexity is the priority?
#   Yes

def rotated_substr(word, rotat):
    if len(word) != len(rotat):
        return False

    rotat_conc = rotat + rotat

    return word in rotat_conc

if __name__ == "__main__":
    print(rotated_substr("thisis", "isthis"))
    print(rotated_substr("hihiho", "hihole"))