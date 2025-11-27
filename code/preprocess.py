# preprocess.py
import re

def normalize_whitespace(text):
    return " ".join(text.split())

def remove_control_chars(text):
    return re.sub(r'[\x00-\x1F\x7F]', ' ', text)

def basic_cleanup(text):
    text = remove_control_chars(text)
    text = normalize_whitespace(text)
    return text
