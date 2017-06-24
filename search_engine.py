import sys

import keywords_extractor
import scholar


def main():
    text = sys.argv[1]

    keywords = keywords_extractor.get_keywords_from_text(text)

    max_results = 4
    sys.argv += ['-A "' + keywords + '"', '-c ' + str(max_results)]

    articles = scholar.main()

    return format_results(articles)

def format_results(articles):
    formated_articles = []

    for article in articles:
        line = ''

        line += 'Title: {}{}'.format(article.get('Title'), ',').lower().title()
        line += 'Year: {}{}'.format(article.get('Year'), ',')
        line += 'Citations {}{}'.format(article.get('Citations'), ',')
        line += 'PDF Link {}{}'.format(article.get('URL'), ';')

        formated_articles.append(line)

    return formated_articles


if __name__ == '__main__':
    main()
