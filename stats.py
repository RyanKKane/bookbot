def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    character_count = {}
    for char in text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(items):
    return items["num"]

def sort_list(char_count):
    sorted_count = []
    for i in char_count:
        temp_dict = {"char": i, "num": char_count[i]}
        sorted_count.append(temp_dict)
    
    sorted_count.sort(reverse=True, key=sort_on)
    return sorted_count
