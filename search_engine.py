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
    formated_articles = ""

    for article in articles:
        formated_articles += "{}{}".format(article.get('Title'), ",").lower().title()
        formated_articles += "{}{}".format(article.get('Year'), ",")
        formated_articles += "{}{}".format(article.get('URL'), ";")

    print formated_articles


if __name__ == '__main__':
    main()
