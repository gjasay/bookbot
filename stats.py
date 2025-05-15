def get_word_count(str):
    return len(str.split())

def get_char_count(str):
    chars = {}

    for word in str.split():
        for char in word:
            lower = char.lower()
            if lower not in chars:
                chars[lower] = 1
            else:
                chars[lower] += 1

    return chars

def sort_dict(dict):
    dicts = []

    for key, value in dict.items():
        dicts.append({"char": key, "num": value})

    def sort_on(dict):
        return dict["num"]

    dicts.sort(reverse=True, key=sort_on)

    return dicts
