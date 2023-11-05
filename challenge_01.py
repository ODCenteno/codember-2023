
dict_counter = []

def get_words():
    words = []
    with open('./data/message_01.txt', "r", encoding='UTF-8') as data:
        text = data.readlines()
        for line in text:
            words.extend(line.strip().split(" "))
    return [word.lower() for word in words]

def print_result():
    result = ""
    for word, count in dict_counter.items():
        result += f'{word}{count}'
    print(result)


def run():
    global dict_counter
    dict_counter = {}

    words = get_words()

    for word in words:
        if word in dict_counter:
            dict_counter[word] += 1
        else:
            dict_counter[word] = 1

    print_result()


if __name__ == '__main__':
    run()
