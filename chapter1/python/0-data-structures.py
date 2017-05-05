
def buildMap(students):
    student_map = {}
    for s in students:
        student_map[s.get_id()] = s
    return student_map

def merge(words, more):
    sentence = []
    for(w in words): sentence.append(w)
    for(w in more): sentence.append(w)

def make_sentence(words):
    sentence = ""
    for(w in words): sentence += w + " "
    return sentence


