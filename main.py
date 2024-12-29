def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_number_of_words(file_contents):
    words = file_contents.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_chars_dict(text):
    chars={}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(dict):
    sorted_list = [{"char": k, "num": v} for k,v in dict.items()]
    sorted_list.sort(reverse = True, key = sort_on)
    print(sorted_list)
    return sorted_list
main()