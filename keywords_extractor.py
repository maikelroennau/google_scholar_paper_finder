import re
import sys

import textrank
from rake_nltk import Rake


def __remove_special_characters(text):
    formated_text = []

    for i in range(len(text)):
        formated_text.append(re.sub('[^A-Za-z0-9]+', '', text[i]))

    return formated_text

def __extract_keywords(text):
    keywords = textrank.extract_key_phrases(text)
    return keywords

def __extract_sentences(text):
    sentences = textrank.extract_sentences(text)
    return sentences

def __list_to_single_string(keywords):
    single_string = ""

    for word in keywords:
        single_string += word + " "

    single_string = single_string[:-1]

    return single_string

def get_keywords_from_text(text):
    text = text.lower()

    words_list = text.split(' ')
    formated_words = __remove_special_characters(words_list)

    phrase = __list_to_single_string(formated_words)
    keywords = __extract_keywords(phrase)

    return __list_to_single_string(keywords)
