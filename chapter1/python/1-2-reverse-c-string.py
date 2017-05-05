
# Write code to reverse a C-Style String

# Does space complexity matter?
#   Yes, to an extent
# Does time complexity matter?
#   Yes
# Can I use native python utils?
#   No
# What is the minimmum length of the string?
#   It is 1 character


def reverse_c_string(c):
    reversed = ""
    for l in c[:-1]:
        reversed = l + reversed

    return reversed + "\0"

if __name__ == "__main__":
    print(reverse_c_string("test1\0"))
