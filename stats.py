def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def count_the_words(path_to_file):
    return len(get_book_text(path_to_file).split())


def count_the_characters(path_to_file):
    letter_dict = {}
    for t in get_book_text(path_to_file).lower():
        if t in letter_dict:
            letter_dict[t] += 1
        else:
            letter_dict[t] = 1
    return letter_dict


def return_num_value(items):
    return items["num"]


def sort_the_char_count(path_to_file):
    sorted_char_list = []
    char_count = count_the_characters(path_to_file)

    for ch in char_count:
        num = char_count[ch]
        sorted_char_list.append({"char": ch, "num": num})

    sorted_char_list.sort(reverse=True, key=return_num_value)
    return sorted_char_list


def print_report(path_to_file):
    word_count = count_the_words(path_to_file)
    sorted_list = sort_the_char_count(path_to_file)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")
