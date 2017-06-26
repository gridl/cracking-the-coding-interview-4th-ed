
# Write code to reverse a C-Style String

# Does space complexity matter?
#   Yes, to an extent
# Does time complexity matter?
#   Yes
# Can I use native python utils?
#   No
# What is the minimmum length of the string?
#   It is 1 character


# This is wrong
# The time complexity of adding a string every time is O(N^2)
def WRONG_reverse_c_string(c):
    reversed = ""
    for l in c[:-1]:
        reversed = l + reversed

    return reversed + "\0"

# This is the correct
def CORRECT_reverse_c_string(c_str):
    r_arr = []
    l = len(c_str)
    i = 0

    while i < (l - 1):
        r_i = (l - 1) - (i+1)
        r_char = c_str[r_i]
        r_arr.append(r_char)

        i += 1

    r_str = ''.join(r_arr)
    r_c_str = r_str + "\0"

    return r_c_str

# This is also correct because slice sorts everything out for
# us with good time complexity
# All of the functions below are maximum O(N)
def CORRECT_reverse_c_string_functional(c_str):

    list_c_str = list(c_str)
    list_str = list_c_str[:-1]
    r_list_str = reversed(list_str)
    r_str = ''.join(r_list_str)
    r_c_str = r_str + '\0'

    return r_c_str



if __name__ == "__main__":
    print(WRONG_reverse_c_string("test1\0"))
    print(CORRECT_reverse_c_string("test1\0"))
    print(CORRECT_reverse_c_string_functional("test1\0"))

