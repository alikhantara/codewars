ooo = 2
minlen = 6
def maybe_replace(word, length=5):
    if len(word) < length:
        return word
    else:
        return word[::-1]

def spin_words(a):
        split_line = a.split()
        new_split_line = [maybe_replace(word) for word in split_line]
        new_line = ' '.join(new_split_line)
        return(new_line)