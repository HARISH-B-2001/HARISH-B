import re
import string
from collections import Counter
n = 5

def read_text_file():
    file1 = open("stopwords", "r")
    text_lines = file1.readlines()
    stop_words = []
    for element in text_lines:
        stop_words.append(element.strip())
    return stop_words



def get_statistics(data):
    lines = get_lines(data)
    words = get_words(lines)
    unique_words = list(set(words))
    stop_words = read_text_file()
    cleaned_words = clean_words(words,stop_words)
    top_n_words = get_top_n_words(cleaned_words,n)
    statistics = {'Line_count':len(lines),'word_count':len(words),'unique_words':len(unique_words),
                  'top_words':top_n_words}
    return statistics

def get_lines(data):
    lines = []
    for para in data:
        para_lines = re.split('[.!?]+',para)
        lines.extend(para_lines)
    cleaned_lines = clean_string(lines)
    return cleaned_lines

def clean_string(lines):
    cleaned_lines = []
    st = str.maketrans("","", string.punctuation)
    for line in lines:
        new_line = line.translate(st).lower().strip()
        if new_line:
            cleaned_lines.append(new_line)
    return cleaned_lines

def get_words(lines):
    words = []
    for line in lines:
        words.extend(line.split())
    return words

def get_top_n_words(words,n):
    top_n_words = Counter(words).most_common(n)
    top_words = []
    for x,y in top_n_words:
        top_words.append(x)
    return top_words

def clean_words(words,stop_words):
    cleaned_words = []
    for i in words:
        if i not in stop_words:
            cleaned_words.append(i)
    return cleaned_words