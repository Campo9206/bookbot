from collections import Counter
def get_num_words(file_contents):
    word_count =0
    file_count = file_contents.split()
    word_count =len(file_count) 
    return word_count

def get_letter_count(file_contents):
        sorted_char = dict(sorted(Counter(file_contents.lower()).items(), key=lambda x:x[1], reverse=True))
        return(sorted_char)