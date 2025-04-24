import sys
from stats import get_num_words
from stats import get_letter_count

def main():
    if len(sys.argv) ==2:
        with open(sys.argv[1]) as f:
            file_contents =f.read()
            num_words = get_num_words(file_contents)
            num_letters= get_letter_count(file_contents)
        print(f"Found {num_words} total words")
        for char in num_letters:
            if char.isalpha():
                print(f"{char}: {num_letters[char]}")
    else:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
main()