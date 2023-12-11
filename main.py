def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    letter_count_dict = get_letter_count(text)
    letter_count_list = list(letter_count_dict)
    letter_count_list.sort(key=lambda x: letter_count_dict[x], reverse=True)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    
    for alpha in letter_count_list:
        print(f"The '{alpha}' was found {letter_count_dict[alpha]} times")
        
    print("--- End report ---")

def get_letter_count(text):
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            low_letter = letter.lower()
            if low_letter in letter_count:
                letter_count[low_letter] += 1
            else:
                letter_count[low_letter] = 1
    return letter_count

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()