
# Write a method to replace all spaces in a string with %20

# Does space complexity matter?
#   Initially no
# Does time complexity matter?
#   Yes
# What is the smallest string?
#   1 char
# Can I use python native string functions?
#   No

# I would just create a new string, iterate through the string, and just append the same exept for spaces

# THIS IS WRONG
# because using the += in strings is terrible in
# time complexity computation
def WRONG_replace_spaces(s):
    string = ""
    for l in s:
        if l == " ":
            string += "%20"
        else:
            string += l

    return string


def CORRECT_replace_spaces_array(s):
    new_s = []
    for c in s:
        if c == " ":
            new_s.append("%20")
        else:
            new_s.append(c)

    return "".join(new_s)

def CORRECT_replace_spaces(s):
    return s.replace(" ", "%20")

if __name__ == "__main__":
    print(CORRECT_replace_spaces_array(""))
    print(CORRECT_replace_spaces_array(" asdf e"))
    print(CORRECT_replace_spaces_array("asdf asdf we ee"))
    print(CORRECT_replace_spaces_array("         "))
