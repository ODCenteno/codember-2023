
dict_counter = []

def get_words():
    words = []
    with open('./data/message_01.txt', "r", encoding='UTF-8') as data:
        text = data.readlines()
        for line in text:
            words.extend(line.strip().split(" "))
    return [word.lower() for word in words]

def is_word_in_list(word):
    return word in dict_counter

def print_result():
    result = ""
    for word in dict_counter:
        result += f'{word}{count}'
    print(result)

def plus_one(word):
    for word_dict in dict_counter:
        word_dict[word] += 1

def run():
    words = get_words()

    for word in words:
        if is_word_in_list(word):
            plus_one(word)
        else:
            dict_counter.append({word: 1})

    print_result()


if __name__ == '__main__':
    run()
