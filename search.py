import textrank
from rake_nltk import Rake
import scholar
import sys
import os.path
import re


def list_to_single_string(keywords):
    single_string = ""

    for word in keywords:
        single_string += word + " "

    single_string = single_string[:-1]

    return single_string


def extract_keywords(text):
    keywords = textrank.extract_key_phrases(text)
    return keywords


def extract_sentences(text):
    sentences = textrank.extract_sentences(text)
    return sentences


def remove_special_characters(text):
    formated_text = []

    formated_text.append("")

    for word in text:
        formated_text[0] += re.sub('[!@#$%&*()_+,.;:/?]+', '', word).rstrip()

    return formated_text


def read_text(path):
    if os.path.isfile(path):
        text = ""
        with open(path, 'r') as file:
            text = file.readlines()
    else:
        print "File not found.\n"
        sys.exit(0)

    text = remove_special_characters(text)

    return list_to_single_string(text)


def show_results(articles):
    for article in articles:
        print 'Title \t\t{}'.format(article.get('Title'))
        print 'Year \t\t{} '.format(article.get('Year'))
        print 'Citations \t{}'.format(article.get('Citations'))
        print 'PDF Link \t{} \n'.format(article.get('PDF Link'))


def main():
    if len(sys.argv) == 1:
        print 'Inform the text file path.\n'
        sys.exit(0)
    elif len(sys.argv) > 2:
        print 'Too many arguments.\n'
        sys.exit(0)

    path = sys.argv[1]
    text = read_text(path)

    if len(text) == 0:
        print 'Text is too small.\n'
        sys.exit(0)

    extracted_keywords = extract_keywords(text)
    extracted_sentences = []

    if len(extracted_keywords) == 0:
        print 'No keywords found. Searching for sentences...\n'

        extracted_sentences = extract_sentences(text)

        if len(extracted_sentences) == 0:
            print 'No sentences found. Not able to continue.\n'
            sys.exit(0)

        extracted_keywords = extract_keywords(extracted_sentences)

    single_line = list_to_single_string(extracted_keywords)

    max_results = 4

    sys.argv += ['-A "' + single_line + '"', '-c ' + str(max_results)]

    print single_line

    print '\nSearching articles...\n'
    articles = scholar.main()

    print '{} article(s) found\n'.format(len(articles))

    show_results(articles)


if __name__ == '__main__':
    main()
