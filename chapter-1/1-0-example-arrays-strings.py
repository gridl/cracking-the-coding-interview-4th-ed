# Hash Tables
def build_map(students):
    hash_map = {}
    for s in students:
        hash_map[s.get_id()] = s
    return hash_map

# Arraylist
# An ArrayList, or a dynamically resizing array, is an array that resizes itself as needed while still providing O(1) access. A typical implementation is that when a vector is full, the array doubles in size. Each doubling takes O(n) time, but happens so rarely that its amortized time is still O(1).
def merge_lists(words, more):
    new_array = []
    new_array.extend(words)
    new_array.extend(more)
    return new_array


def make_sentence(words):
    sentence = " ".join(words)
    return sentence

