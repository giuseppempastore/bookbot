from pathlib import Path

def main():
    current_directory = Path.cwd()
    print(f"current directory is {current_directory}")
    file_content = read_file(current_directory)
    word_num = word_number(file_content)
    char_dic = count_char(file_content)
    sort_dic = sort_dictionary(char_dic)
    print(f"word number is {word_num} and char dictionary is {char_dic} sort dictionary of only alphabet words is {sort_dic}")


def read_file(path_to_file):
    desired_directory = Path("books/frankenstein.txt")
    if(desired_directory != path_to_file):
        path_to_file = "./books/frankenstein.txt"
        with open(path_to_file) as f:
            return f.read()
    else:
        with open(path_to_file) as f:
            return f.read()

def word_number(text):
    text_array = text.split()
    return len(text_array)

def count_char(text):
    text_low = text.lower()
    word_dictionary = {}
    for charac in text_low:
        if(charac in word_dictionary):
            word_dictionary[charac] +=1
        else:
            word_dictionary[charac] = 1
    return word_dictionary

def sort_dictionary(char_dic):
    sort_word_list = []
    for char in char_dic:
        print(f"current char is {char}")
        if(not char.isalpha()):
            print(f"current char is alpha? NOPE {char.isalpha()}")
            continue
        else:
            print(f"current char is alpha? YEP!!!!! {char.isalpha()}")
            char_elem = {}
            char_elem["char"] = char
            char_elem["num"] = char_dic[char]
            sort_word_list.append(char_elem)
    sort_word_list.sort(reverse=True, key=sort_criteria)
    return sort_word_list

def sort_criteria(sort_word_list):
    return sort_word_list["num"]

main()