def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_chars(text)
    book_report(num_letters, num_words, book_path)

def book_report(letters, words, book_path):
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
    print(" --- End report ---")

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