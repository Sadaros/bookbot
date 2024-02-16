import sys

def main():
    print("bookbot, a tool for checking words and letters in a text file")
    if len(sys.argv) == 1:
        book_path = input("Relative Path to book: ")
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_chars(text)
    if len(sys.argv) <= 2:
        book_report_print(num_letters, num_words, book_path)
    else:
        book_report_write(num_letters, num_words, book_path)

def book_report_print(letters, words, book_path):
    reported_letters = []
    for letter in letters:
        this_letter = {}
        this_letter["letter"] = letter
        this_letter["num"] = letters[letter]
        reported_letters.append(this_letter)
    reported_letters.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(" ")
    print(f"There are a total of {words} words in the document")
    print(" ")
    for letter in reported_letters:
        print(f"The letter {letter['letter']} is found {letter['num']} times in the document")
    print("--- End report ---")

def book_report_write(letters, words, book_path):
    output = open(sys.argv[2], "a")
    reported_letters = []
    for letter in letters:
        this_letter = {}
        this_letter["letter"] = letter
        this_letter["num"] = letters[letter]
        reported_letters.append(this_letter)
    reported_letters.sort(reverse=True, key=sort_on)

    output.write(f"--- Begin report of {book_path} ---\n")
    output.write("\n")
    output.write(f"There are a total of {words} words in the document\n")
    output.write("\n")
    for letter in reported_letters:
        output.write(f"The letter {letter['letter']} is found {letter['num']} times in the document\n")
    output.write("--- End report ---\n")

def sort_on(dict):
    return dict["num"]
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    lower_text = text.lower()
    num_chars = {}
    for char in lower_text:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    filtered_chars = filter_special_characters(num_chars)
    return filtered_chars

def filter_special_characters(dict):
    return {k:v for (k,v) in dict.items() if k.isalpha()}

main()