def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_dict = count_the_letters(text)
    char_list = []
    for char in char_dict:
       new_dict = {}
       new_dict["char"] = char
       new_dict["num"] = char_dict[char]
       char_list.append(new_dict)
    char_list.sort(reverse = True, key = sort_on)
    for i in char_list:
        print(f"The '{i["char"]}' character was found {i["num"]} times")

def sort_on(dict):
    return dict["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def count_the_letters(text):
    l_text = text.lower()
    char_count = {}
    for char in l_text:
        if char.isalpha():
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] +=1
    return char_count


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()

