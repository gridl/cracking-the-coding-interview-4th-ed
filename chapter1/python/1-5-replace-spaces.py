
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

def replace_spaces(s):
    string = ""
    for l in s:
        if l == " ":
            string += "%20"
        else:
            string += l

    return string

if __name__ == "__main__":
    print(replace_spaces(""))
    print(replace_spaces(" asdf e"))
    print(replace_spaces("asdf asdf we ee"))
    print(replace_spaces("         "))
