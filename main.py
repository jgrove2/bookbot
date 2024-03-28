def main():
    file_path = './books/frankenstein.txt'
    frankenstein = open_book(file_path)
    word_len = get_number_of_words(frankenstein)
    char_freq = get_char_frequency(frankenstein)
    report = char_report(char_freq)
    for i in report:
        print(f"The '{i['name']}' character was found {i['num']} times")


def open_book(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def get_number_of_words(book_string):
    return len(book_string.split())

def get_char_frequency(book_string):
    char_dict = dict()
    for i in book_string:
        char = i.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def char_report(char_dictionary):
    report = []
    for char in char_dictionary:
        if char.isalpha():
            number = char_dictionary[char]
            report.append({"name": char, "num": number})
    report.sort(reverse=True, key=sort_on)
    return report
main()
